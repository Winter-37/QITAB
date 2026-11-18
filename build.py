#!/usr/bin/env python3
"""Build index.html from tree.txt and the Markdown notes in notes/.

    python3 build.py            build once
    python3 build.py --watch    rebuild whenever a note, tree.txt or the page template changes

Needs one package:  pip install markdown
Viewing the result needs nothing: open index.html in any browser.
"""
import argparse
import html
import json
import re
import sys
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parent
NOTES = ROOT / "notes"
TREE = ROOT / "tree.txt"
PAGE = ROOT / "src" / "page.html"
OUT = ROOT / "index.html"
CONV = ROOT / "conventions.txt"

STATUSES = ("not-started", "in-progress", "complete", "needs-revision")
WORDS_PER_MIN = 260


# ----------------------------------------------------------------------------
# folder tree
# ----------------------------------------------------------------------------
def read_tree():
    """Folder keys in tree order, e.g. '04_X/03_Y/RHF' (parents come before children)."""
    keys, path = [], []
    for n, raw in enumerate(TREE.read_text(encoding="utf-8").splitlines(), 1):
        t = raw.strip()
        if not t or t.startswith("#"):
            continue
        if "\t" in raw:
            sys.exit(f"tree.txt line {n}: use two spaces for indentation, not tabs")
        indent = len(raw) - len(raw.lstrip(" "))
        if indent % 2:
            sys.exit(f"tree.txt line {n}: indentation must be a multiple of two spaces")
        depth = indent // 2
        if depth > len(path):
            sys.exit(f"tree.txt line {n}: '{t}' is indented too deeply; a folder can only sit one level below its parent")
        del path[depth:]
        path.append(t)
        key = "/".join(path)
        if key in keys:
            print(f"  warning: tree.txt line {n}: duplicate folder {key}")
            continue
        keys.append(key)
    return keys


def ensure_dirs(keys):
    NOTES.mkdir(exist_ok=True)
    for k in keys:
        (NOTES / k).mkdir(parents=True, exist_ok=True)


# ----------------------------------------------------------------------------
# front matter
# ----------------------------------------------------------------------------
def slug(s):
    return re.sub(r"[^a-z0-9]+", "-", str(s).lower()).strip("-")


def _clean(v):
    v = v.strip()
    if len(v) >= 2 and v[0] == v[-1] and v[0] in "\"'":
        v = v[1:-1]
    return v


def _split_commas(s):
    out, cur, depth = [], "", 0
    for ch in s:
        if ch == "," and depth == 0:
            out.append(cur)
            cur = ""
            continue
        if ch in "[(":
            depth += 1
        elif ch in "])":
            depth -= 1
        cur += ch
    if cur.strip():
        out.append(cur)
    return [_clean(x) for x in out if x.strip()]


def parse_front(text):
    """Tiny YAML subset: 'key: value', 'key: [a, b]', and 'key:' followed by '- item' lines."""
    text = text.lstrip("﻿")
    m = re.match(r"^---[ \t]*\r?\n(.*?)\r?\n---[ \t]*(?:\r?\n|$)", text, re.S)
    if not m:
        return {}, text
    meta, key = {}, None
    for line in m.group(1).splitlines():
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        li = re.match(r"^\s+-\s+(.*)$", line)
        if li and key:
            if not isinstance(meta.get(key), list):
                meta[key] = []
            meta[key].append(_clean(li.group(1)))
            continue
        k, _, v = line.partition(":")
        key = k.strip().lower()
        v = v.strip()
        if v == "":
            meta[key] = []
        elif v.startswith("[") and v.endswith("]"):
            meta[key] = _split_commas(v[1:-1])
        else:
            meta[key] = _clean(v)
    return meta, text[m.end():]


def as_list(v):
    if v is None or v == "":
        return []
    return v if isinstance(v, list) else [v]


def as_str(v):
    if isinstance(v, list):
        return v[0] if v else ""
    return v or ""


# ----------------------------------------------------------------------------
# Markdown + math
# ----------------------------------------------------------------------------
FENCE = re.compile(r"(?ms)^([ \t]*)(`{3,}|~{3,})[^\n]*\n.*?^\1\2[ \t]*$")
INLINE_CODE = re.compile(r"(?<!`)(`+)(?!`)(.+?)(?<!`)\1(?!`)")
DISPLAY_DOLLAR = re.compile(r"(?ms)^(?P<ind>[ \t]*(?:>[ \t]*)*)\$\$(?P<m>.+?)\$\$")
DISPLAY_BRACKET = re.compile(r"(?ms)^(?P<ind>[ \t]*(?:>[ \t]*)*)\\\[(?P<m>.+?)\\\]")
DISPLAY_LOOSE = re.compile(r"(?s)\$\$(.+?)\$\$")
INLINE_PAREN = re.compile(r"(?s)(?<!\\)\\\((.+?)\\\)")
INLINE_DOLLAR = re.compile(r"(?<![\\$])\$(?=[^\s$])((?:\\.|[^$\\\n])+?)(?<=[^\s\\])\$(?![\d$])")
WIKILINK = re.compile(r"\[\[([^\[\]|]+)(?:\|([^\[\]]+))?\]\]")
LABEL = re.compile(r"\\label\{([^{}]+)\}")
DISPLAY_ANY = re.compile(r"(?s)(?<!\\)\$\$(.+?)\$\$|\\\[(.+?)\\\]")


def norm_label(s):
    """Equation label as used in ids and links: lowercase letters, digits, '_' and '-'."""
    return re.sub(r"[^a-z0-9_-]+", "-", str(s).strip().lower()).strip("-")


def eq_labels(body):
    """Labels of display equations, in the order they appear (code blocks ignored)."""
    body = FENCE.sub("", body)
    body = INLINE_CODE.sub("", body)
    out = []
    for m in DISPLAY_ANY.finditer(body):
        found = LABEL.findall(m.group(1) or m.group(2) or "")
        if found:
            out.append(norm_label(found[0]))
    return out
FILE_EXT = r"pdf|png|jpe?g|svg|gif|webp|txt|csv|py|ipynb|zip|json|xyz|cif|mol|log|out"


class Renderer:
    def __init__(self, resolver):
        import markdown  # imported here so new_note.py can reuse read_tree() without it

        self.md = markdown.Markdown(
            extensions=["tables", "fenced_code", "admonition", "sane_lists", "md_in_html"],
            output_format="html",
        )
        self.resolver = resolver

    def render(self, body, note_dir, links, unresolved, self_id=None, eqs=None, labels_of=None, problems=None):
        """eqs: dict filled with label -> TeX of each labelled display equation.
        labels_of(note_id): the set of equation labels of a note, to check [[note#label]] links.
        self_id None (folder introductions): labels are dropped and equations stay unnumbered."""
        stash = {"code": [], "disp": [], "inl": []}
        problems = problems if problems is not None else []
        seen_labels = set()

        def label_disp(tex):
            """Turn \\label{x} into a placeholder tag the page fills with the section-based number."""
            found = LABEL.findall(tex)
            if not found:
                return (tex, None)
            tex = LABEL.sub("", tex).strip()
            lab = norm_label(found[0])
            if len(found) > 1:
                problems.append(f"more than one \\label in one display equation ({', '.join(found)}); only '{lab}' is used")
            if self_id is None or not lab:
                return (tex, None)
            if lab in seen_labels:
                problems.append(f"equation label '{lab}' is used twice")
                return (tex, None)
            seen_labels.add(lab)
            if eqs is not None:
                eqs[lab] = tex
            if "\\tag" in tex:
                problems.append(f"equation '{lab}' already has a \\tag; the label is linkable but not numbered")
                return (tex, lab)
            return (tex + " \\tag{@@EQ:" + lab + "@@}", lab)

        def put(kind, value, token):
            stash[kind].append(value)
            return f"Z{token}{len(stash[kind]) - 1}Z"

        # 1. code (so nothing inside it is touched)
        body = FENCE.sub(lambda m: put("code", m.group(0), "CODE"), body)
        body = INLINE_CODE.sub(lambda m: put("code", m.group(0), "CODE"), body)

        # 2. math
        def disp_at_line_start(m):
            ind = m.group("ind")
            return f"\n{ind}\n{ind}" + put("disp", label_disp(m.group("m").strip()), "MATHDISP") + f"\n{ind}\n"

        body = DISPLAY_DOLLAR.sub(disp_at_line_start, body)
        body = DISPLAY_BRACKET.sub(disp_at_line_start, body)
        body = DISPLAY_LOOSE.sub(lambda m: put("disp", label_disp(m.group(1).strip()), "MATHDISP"), body)
        body = INLINE_PAREN.sub(lambda m: put("inl", m.group(1).strip(), "MATHINL"), body)
        body = INLINE_DOLLAR.sub(lambda m: put("inl", m.group(1), "MATHINL"), body)

        # any '$' left over is a plain dollar sign (prices, shell prompts): escape it so MathJax
        # in the browser does not pair it with another one and typeset the text between them
        body = re.sub(r"(?<!\\)\$", r"\\$", body)

        # 3. [[wiki links]]
        def wiki(m):
            ref, label = m.group(1).strip(), (m.group(2) or "").strip()
            if "#" in ref:
                # [[note#label]] or [[#label]]: a link to a numbered equation
                target, _, lab = ref.partition("#")
                lab = norm_label(lab)
                if target.strip():
                    note = self.resolver(target.strip())
                    nid = note["id"] if note is not None else None
                else:
                    nid = self_id
                if nid is None:
                    unresolved.add(target.strip() or ref)
                    return f'<span class="planned" title="Not written yet">{html.escape(label or ref)}</span>'
                if labels_of is not None and lab not in labels_of(nid):
                    problems.append(f"[[{ref}]]: note '{nid}' has no equation labelled '{lab}'")
                    return f'<span class="planned" title="No equation with this label">{html.escape(label or "Eq. (?)")}</span>'
                if nid != self_id:
                    links.add(nid)
                text = html.escape(label) if label else f"Eq.&nbsp;(@@EQREF:{nid}~{lab}@@)"
                return (f'<a class="xref eqref" href="#n.{nid}~eq-{lab}" data-n="{nid}" data-eq="{lab}">{text}</a>')
            note = self.resolver(ref)
            if note is not None:
                links.add(note["id"])
                return f'<a class="xref" href="#n.{note["id"]}">{html.escape(label or note["title"])}</a>'
            unresolved.add(ref)
            return f'<span class="planned" title="Not written yet">{html.escape(label or ref)}</span>'

        body = WIKILINK.sub(wiki, body)

        # 4. code back, then Markdown
        body = re.sub(r"ZCODE(\d+)Z", lambda m: stash["code"][int(m.group(1))], body)
        self.md.reset()
        out = self.md.convert(body)

        # 5. tidy the HTML
        out = out.replace("<table>", '<div class="tablewrap"><table>').replace("</table>", "</table></div>")
        out = re.sub(r"<p>\s*(ZMATHDISP\d+Z)\s*</p>", r"\1", out)

        def fix_path(m):
            attr, url = m.group(1), m.group(2)
            if re.match(r"^(?:[a-z][a-z0-9+.-]*:|/|#|notes/)", url, re.I):
                return m.group(0)
            if attr == "href" and not re.search(r"\.(?:%s)(?:[?#].*)?$" % FILE_EXT, url, re.I):
                return m.group(0)
            prefix = f"notes/{note_dir}/" if note_dir else "notes/"
            return f'{attr}="{prefix}{url}"'

        out = re.sub(r'\b(src|href)="([^"]+)"', fix_path, out)

        # 6. math back
        esc = lambda s: html.escape(s, quote=False)
        def disp_back(m):
            tex, lab = stash["disp"][int(m.group(1))]
            ident = f' id="eq-{lab}"' if lab else ""
            return f'<div class="eq"{ident}>$$' + esc(tex) + "$$</div>"

        out = re.sub(r"ZMATHDISP(\d+)Z", disp_back, out)
        out = re.sub(r"ZMATHINL(\d+)Z", lambda m: "$" + esc(stash["inl"][int(m.group(1))]) + "$", out)
        return out


def plain_words(htm):
    return len(re.sub(r"<[^>]+>", " ", htm).split())


# ----------------------------------------------------------------------------
# conventions (conventions.txt)
# ----------------------------------------------------------------------------
def read_conventions():
    """{'axes': {axis: {'about', 'see', 'values': [ids]}}, 'values': {value: {'axis', 'label'}}}."""
    axes, values = {}, {}
    if not CONV.exists():
        return {"axes": axes, "values": values}
    axis = None
    for n, raw in enumerate(CONV.read_text(encoding="utf-8").splitlines(), 1):
        if not raw.strip() or raw.lstrip().startswith("#"):
            continue
        if raw[0] not in " \t":
            name, _, about = raw.partition(":")
            axis = slug(name)
            see = re.search(r"\(see\s+([^)\s]+)\s*\)", about)
            check = not re.search(r"\(not checked\)", about)
            about = re.sub(r"\((?:see\s+[^)]*|not checked)\)", "", about).strip()
            axes[axis] = {"about": about, "see": see.group(1) if see else "", "check": check, "values": []}
            continue
        v, eq, label = raw.strip().partition("=")
        if not eq or axis is None:
            print(f"  warning: conventions.txt line {n}: expected 'value-id = label' under an axis")
            continue
        v = slug(v)
        if v in values:
            print(f"  warning: conventions.txt line {n}: value '{v}' is already defined")
            continue
        values[v] = {"axis": axis, "label": label.strip()}
        axes[axis]["values"].append(v)
    return {"axes": axes, "values": values}


# ----------------------------------------------------------------------------
# sources (the '## Source' section of each note)
# ----------------------------------------------------------------------------
SOURCE_HEAD = re.compile(r"(?ms)^##[ \t]+(?:Sources?|References)[ \t]*\r?\n(.*?)(?=^##[ \t]|\Z)")
WORK = re.compile(r"(?<![*\w])\*(?!\*)([^*\n]{3,160}?)\*(?!\*)")
JOURNAL = re.compile(r"^(?:J\.|Phys\.|Chem\.|Nat\.|Sci\.|Ann\.|Mol\.|Int\.|Nucl\.|Rev\.|Proc\.|Acc\.|Theor\.|"
                     r"Comput\.|PRX|PNAS|WIREs|IEEE|npj|Faraday|arXiv|(?:Nature|Science|Quantum)$)")
LOCATION = re.compile(r"\b(Secs?|Sections?|Chs?|Chap|Chapters?|Appendix|App)\.?\s+(\d+(?:\.\d+)*(?:\s*[-–]\s*\d+(?:\.\d+)*)?"
                      r"(?:\s*(?:,|and)\s*\d+(?:\.\d+)*(?:\s*[-–]\s*\d+(?:\.\d+)*)?(?![\d.]*\s*(?:pp|p)\.))*)")
DOI = re.compile(r"(?:doi:\s*|https?://(?:dx\.)?doi\.org/)(10\.\d{4,9}/[^\s,;)\]]+)", re.I)


def name_run(head):
    """The run of author names that ends a piece of text: 'drawn from T. D. Crawford and H. F. Schaefer'
    gives 'T. D. Crawford and H. F. Schaefer'. Scans words backwards (no regex backtracking)."""
    words = head.split()
    i = len(words)
    while i > 0:
        w = words[i - 1]
        core = w.rstrip(",")
        if w.endswith((":", ";")) or not (core in ("and", "et", "al.", "al") or core[:1].isupper()):
            break
        i -= 1
    run = words[i:]
    while run and run[0].rstrip(",") in ("and", "et", "al.", "al"):
        run = run[1:]
    return " ".join(run).rstrip(",") if run else ""


def paper_label(prefix):
    """'Authors, "Title", *Journal* vol, pages (year)' from the text that precedes a DOI."""
    prefix = re.sub(r"[\s,]*(?:doi:?)?[\s,]*$", "", prefix, flags=re.I)
    journals = list(re.finditer(r"(?<!\*)\*(?!\*)[^*]+?\*(?!\*)", prefix))
    if not journals:
        return ""
    jm = journals[-1]
    head, tail, title = prefix[:jm.start()].rstrip(" ,"), prefix[jm.start():], ""
    qm = re.search(r'"[^"]+"$', head)
    if qm:
        title, head = qm.group(0), head[:qm.start()].rstrip(" ,")
    authors = name_run(head)
    return ", ".join(x for x in (authors, title, tail) if x) if authors else ""


def source_text(body):
    m = SOURCE_HEAD.search(body)
    return m.group(1).strip() if m else ""


def parse_sources(text):
    """Books (italic title followed by '(... year ...)') with the sections cited, and DOIs."""
    books, papers = [], []
    works = [m for m in WORK.finditer(text)]
    for i, m in enumerate(works):
        title = m.group(1).strip()
        after = text[m.end():m.end() + 160]
        pm = re.match(r"\s*(\([^()]*\d{4}[^()]*\))", after)
        if not pm or JOURNAL.match(title):
            continue
        # where this citation ends: the next italic title, a blank line, or the end
        end = works[i + 1].start() if i + 1 < len(works) else len(text)
        blank = text.find("\n\n", m.end())
        if 0 <= blank < end:
            # 'Book (ed.):' followed by a bullet list of sections belongs to the same citation
            bullets = re.match(r"\n\n((?:[ \t]*[-*+][ \t].*(?:\n|$))+)", text[blank:]) if text[:blank].rstrip().endswith(":") else None
            end = min(end, blank + bullets.end()) if bullets else blank
        chunk = text[m.end():end]
        start = max(text.rfind("\n", 0, m.start()), text.rfind(";", 0, m.start()), text.rfind(". ", 0, m.start()), -1) + 1
        before = text[start:m.start()].rstrip()
        authors = name_run(before[:-1]) if before.endswith(",") else ""
        locs = []
        for lm in LOCATION.finditer(chunk):
            g = lm.group(1).lower()
            kind = "Ch." if g.startswith("ch") else ("App." if g.startswith("app") else "Sec.")
            for part in re.split(r"\s*(?:,|and)\s*", lm.group(2)):
                part = re.sub(r"\s*[-–]\s*", "–", part.strip())
                if part:
                    locs.append(f"{kind} {part}")
        books.append({"title": re.split(r":\s", title)[0].strip(), "authors": authors,
                      "edition": pm.group(1), "locs": locs})
    for line in re.split(r"\n|;\s", text):
        for dm in DOI.finditer(line):
            doi = dm.group(1).rstrip(".").lower()
            label = paper_label(line[:dm.start()])
            papers.append({"doi": doi, "label": label})
    return books, papers


def md_inline(s):
    """Minimal inline Markdown for source labels: escape, then *italic* and **bold**."""
    s = html.escape(s, quote=False)
    s = re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", s)
    s = re.sub(r"(?<![*\w])\*(?!\*)(.+?)\*(?!\*)", r"<i>\1</i>", s)
    return re.sub(r"\[\[([^\]|]+)(?:\|([^\]]+))?\]\]", lambda m: m.group(2) or m.group(1), s)


def loc_key(loc):
    nums = re.findall(r"\d+", loc.split("–")[0])
    return [{"Ch.": 0, "Sec.": 1}.get(loc.split()[0], 2)] + [int(x) for x in nums]


# ----------------------------------------------------------------------------
# build
# ----------------------------------------------------------------------------
def read_private():
    """Folder paths (relative to notes/) listed in .privatebuild, one per line; '#' comments."""
    f = ROOT / ".privatebuild"
    if not f.exists():
        return []
    return [l.strip().strip("/") for l in f.read_text(encoding="utf-8").splitlines()
            if l.strip() and not l.strip().startswith("#")]


def build(public=False):
    t0 = time.time()
    warnings = []
    keys = read_tree()
    ensure_dirs(keys)
    private = read_private() if public else []

    def is_private(path):
        return any(path == q or path.startswith(q + "/") for q in private)

    keys = [k for k in keys if not is_private(k)]
    private_ids = set()
    for q in private:
        for pp in (NOTES / q).rglob("*.md"):
            m0, _ = parse_front(pp.read_text(encoding="utf-8"))
            private_ids.add(slug(m0.get("id") or re.sub(r"^\d+_", "", pp.stem)))
    known = set(keys)
    extra_keys = []

    def add_folder(key, why):
        parts = key.split("/")
        for i in range(1, len(parts) + 1):
            k = "/".join(parts[:i])
            if k not in known:
                known.add(k)
                extra_keys.append(k)
                warnings.append(f"folder '{k}' is not in tree.txt ({why}); added at the end of the tree")

    # ---- pass 1: read every note
    records, intros_raw = [], {}
    used_ids = {}
    for p in sorted(NOTES.rglob("*.md")):
        rel = p.relative_to(NOTES)
        if any(part.startswith((".", "_")) for part in rel.parts):
            continue
        if is_private(rel.as_posix()):
            continue
        key = rel.parent.as_posix()
        key = "" if key == "." else key
        meta, body = parse_front(p.read_text(encoding="utf-8"))
        if public:
            body = re.sub(r"<!--private-->.*?<!--/private-->\n?", "", body, flags=re.S)
            body = re.sub(r"^## [^\n]+\n\s*(?=^## |\Z)", "", body, flags=re.M)
            for fld in ("related", "prerequisites"):
                if isinstance(meta.get(fld), list):
                    meta[fld] = [x for x in meta[fld] if slug(x) not in private_ids]
        if key and key not in known:
            add_folder(key, f"notes/{rel.as_posix()}")
        if p.name.lower() == "index.md":
            intros_raw[key] = (body, meta)
            continue
        title = as_str(meta.get("title"))
        m = re.match(r"\s*#[ \t]+(.+?)[ \t]*\r?\n", body)
        if m:
            if not title:
                title = m.group(1).strip()
            body = body[m.end():]
        if not title:
            title = p.stem.replace("_", " ").replace("-", " ")
        nid = slug(as_str(meta.get("id"))) or slug(re.sub(r"^\d+[_-]", "", p.stem)) or slug(title)
        base, n = nid, 2
        while nid in used_ids:
            nid = f"{base}-{n}"
            n += 1
        if nid != base:
            warnings.append(f"duplicate note id '{base}' ({rel.as_posix()}); using '{nid}'")
        used_ids[nid] = rel.as_posix()
        status = slug(as_str(meta.get("status")))
        if status and status not in STATUSES:
            warnings.append(f"{rel.as_posix()}: unknown status '{status}' (use: {', '.join(STATUSES)})")
        order = as_str(meta.get("order"))
        try:
            order = float(order) if order != "" else None
        except ValueError:
            order = None
        records.append({
            "path": rel, "key": key, "meta": meta, "body": body, "id": nid, "title": title,
            "stem": p.stem, "status": status, "order": order,
        })

    # ---- equation labels of every note (needed before rendering, to check [[note#label]] links)
    labels_by_id = {}
    for r in records:
        r["eqs"] = []
        for lab in eq_labels(r["body"]):
            if lab and lab not in r["eqs"]:
                r["eqs"].append(lab)
        labels_by_id[r["id"]] = set(r["eqs"])

    # ---- resolver for ids, titles and file names
    lookup = {}
    for r in records:
        for k in (r["id"], slug(r["title"]), slug(r["stem"])):
            lookup.setdefault(k, r)

    def resolver(ref):
        return lookup.get(slug(ref))

    renderer = Renderer(resolver)
    conv = read_conventions()

    # ---- pass 2: render
    notes_out = []
    unresolved_all = {}
    book_cites, paper_cites = {}, {}
    for r in records:
        meta = r["meta"]
        links, unresolved = set(), set()
        eqs, problems = {}, []
        htm = renderer.render(r["body"], r["key"], links, unresolved, self_id=r["id"], eqs=eqs,
                              labels_of=lambda nid: labels_by_id.get(nid, set()), problems=problems)
        for pr in problems:
            warnings.append(f"{r['path'].as_posix()}: {pr}")
        key_eq = norm_label(as_str(meta.get("key")))
        if key_eq and key_eq not in eqs:
            warnings.append(f"{r['path'].as_posix()}: key: '{key_eq}' is not the label of an equation in this note")
            key_eq = ""
        conv_ids = []
        for v in as_list(meta.get("conventions")):
            v = slug(v)
            if v in conv["values"]:
                conv_ids.append(v)
            elif v:
                warnings.append(f"{r['path'].as_posix()}: unknown convention '{v}' (add it to conventions.txt)")
        books, papers = parse_sources(source_text(r["body"]))
        for b in books:
            k = slug(b["title"])
            e = book_cites.setdefault(k, {"title": b["title"], "authors": {}, "edition": {}, "locs": {}, "notes": []})
            if b["authors"]:
                e["authors"][b["authors"]] = e["authors"].get(b["authors"], 0) + 1
            e["edition"][b["edition"]] = e["edition"].get(b["edition"], 0) + 1
            if r["id"] not in e["notes"]:
                e["notes"].append(r["id"])
            for loc in (b["locs"] or [""]):
                ids = e["locs"].setdefault(loc, [])
                if r["id"] not in ids:
                    ids.append(r["id"])
        for pp in papers:
            e = paper_cites.setdefault(pp["doi"], {"labels": [], "notes": []})
            if pp["label"]:
                e["labels"].append(pp["label"])
            if r["id"] not in e["notes"]:
                e["notes"].append(r["id"])

        def refs(field_names):
            out = []
            for f in field_names:
                for ref in as_list(meta.get(f)):
                    note = resolver(ref)
                    if note is None:
                        unresolved.add(ref)
                        out.append(ref)
                    elif note["id"] != r["id"] and note["id"] not in out:
                        out.append(note["id"])
            return out

        prereq = refs(["prerequisites", "prerequisite", "prereq"])
        related = refs(["related"])
        if as_list(meta.get("also")):
            warnings.append(f"{r['path'].as_posix()}: 'also:' is no longer supported (each note has one home); ignored")
        cite = {k: as_str(meta.get(k)) for k in ("authors", "journal", "year", "doi") if as_str(meta.get(k))}
        for ref in sorted(unresolved):
            unresolved_all.setdefault(ref, []).append(r["id"])
        notes_out.append({
            "id": r["id"], "title": r["title"], "summary": as_str(meta.get("summary")),
            "date": as_str(meta.get("date")), "status": r["status"],
            "level": slug(as_str(meta.get("level"))), "kind": slug(as_str(meta.get("kind"))),
            "tags": [t for t in as_list(meta.get("tags")) if t],
            "prereq": prereq, "related": related, "links": sorted(links - {r["id"]}),
            "home": r["key"], "order": r["order"], "cite": cite,
            "mins": max(1, round(plain_words(htm) / WORDS_PER_MIN)), "html": htm,
            "eqs": [[lab, eqs.get(lab, "")] for lab in r["eqs"] if lab in eqs],
            "key": key_eq, "conv": conv_ids,
        })

    intros = {}
    for key, (body, _meta) in intros_raw.items():
        intros[key] = renderer.render(body, key, set(), set(), labels_of=lambda nid: labels_by_id.get(nid, set()))

    # ---- conventions: a note and a direct prerequisite with disjoint values on one axis
    conv_warnings = []
    by_id = {n["id"]: n for n in notes_out}

    def per_axis(n):
        out = {}
        for v in n["conv"]:
            out.setdefault(conv["values"][v]["axis"], set()).add(v)
        return out

    for n in notes_out:
        mine = per_axis(n)
        if not mine:
            continue
        for pid in n["prereq"]:
            p = by_id.get(pid)
            if p is None:
                continue
            theirs = per_axis(p)
            for axis, vals in mine.items():
                if not conv["axes"][axis]["check"]:
                    continue
                if axis in theirs and not (vals & theirs[axis]):
                    lab = lambda vs: " + ".join(conv["values"][v]["label"] for v in sorted(vs))
                    conv_warnings.append(f"{n['id']} uses {lab(vals)} ({axis}), its prerequisite {pid} uses "
                                         f"{lab(theirs[axis])}; if the switch is deliberate, list both values in the note that makes it")

    # ---- sources: books by sections cited, papers by DOI
    paper_notes = {n["cite"]["doi"].lower(): n["id"] for n in notes_out if n["cite"].get("doi")}
    books_out = []
    for k, e in book_cites.items():
        authors = max(e["authors"], key=e["authors"].get) if e["authors"] else ""
        edition = max(e["edition"], key=lambda x: (e["edition"][x], len(x)))
        locs = sorted(((loc, ids) for loc, ids in e["locs"].items() if loc), key=lambda x: loc_key(x[0]))
        general = [i for i in e["locs"].get("", [])]
        books_out.append({"key": k, "title": e["title"], "authors": authors, "edition": edition,
                          "notes": e["notes"], "locs": [[loc, ids] for loc, ids in locs], "general": general})
    books_out.sort(key=lambda b: (-len(b["notes"]), b["title"]))
    papers_out = []
    for doi, e in paper_cites.items():
        label = max(e["labels"], key=len) if e["labels"] else doi
        papers_out.append({"doi": doi, "label": md_inline(label), "notes": e["notes"], "note": paper_notes.get(doi, "")})
    for doi, nid in paper_notes.items():
        if doi not in paper_cites:
            c = by_id[nid]["cite"]
            papers_out.append({"doi": doi, "label": html.escape(", ".join(x for x in (c.get("authors"), c.get("journal"), c.get("year")) if x)),
                               "notes": [], "note": nid})
    papers_out.sort(key=lambda x: (-len(x["notes"]) - (1 if x["note"] else 0), x["label"]))

    for ref, who in sorted(unresolved_all.items()):
        warnings.append(f"not written yet: '{ref}' (linked from {', '.join(sorted(set(who)))})")

    data = {"folders": keys + extra_keys, "notes": notes_out, "intros": intros,
            "conventions": conv, "sources": {"books": books_out, "papers": papers_out}}
    blob = json.dumps(data, ensure_ascii=False, separators=(",", ":")).replace("<", "\\u003c")
    page = PAGE.read_text(encoding="utf-8")
    if "__SITE_DATA__" not in page:
        sys.exit("src/page.html has no __SITE_DATA__ placeholder")
    OUT.write_text(page.replace("__SITE_DATA__", blob), encoding="utf-8")

    n_unres = len(unresolved_all)
    shown = [w for w in warnings if not w.startswith("not written yet")]
    if public:
        print(f"  PUBLIC build: left out {', '.join(private) or '(nothing: .privatebuild missing)'}")
    print(f"Built index.html: {len(notes_out)} notes, {len(keys) + len(extra_keys)} folders "
          f"({(time.time() - t0) * 1000:.0f} ms)")
    for w in shown:
        print("  warning:", w)
    if conv_warnings:
        print(f"  {len(conv_warnings)} convention mismatch(es) between a note and its prerequisite:")
        for w in conv_warnings[:15]:
            print("   -", w)
        if len(conv_warnings) > 15:
            print(f"   ... and {len(conv_warnings) - 15} more")
    n_eq = sum(len(n["eqs"]) for n in notes_out)
    n_conv = sum(1 for n in notes_out if n["conv"])
    print(f"  {n_eq} labelled equation(s); conventions declared in {n_conv} note(s); "
          f"sources: {len(books_out)} book(s), {len(papers_out)} paper(s) with a DOI")
    if n_unres:
        planned = [w for w in warnings if w.startswith("not written yet")]
        print(f"  {n_unres} linked note(s) not written yet (shown greyed out as 'planned'):")
        for w in planned[:15]:
            print("   -", w[len("not written yet: "):])
        if len(planned) > 15:
            print(f"   ... and {len(planned) - 15} more")


def fingerprint():
    files = [TREE, PAGE, CONV] + [p for p in NOTES.rglob("*") if p.is_file()]
    return sorted((str(p), p.stat().st_mtime_ns) for p in files if p.exists())


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--public", action="store_true",
                    help="leave out the folders listed in .privatebuild (use before committing index.html)")
    ap.add_argument("--watch", action="store_true", help="rebuild on every change (Ctrl+C to stop)")
    args = ap.parse_args()
    try:
        import markdown  # noqa: F401
    except ImportError:
        sys.exit("The 'markdown' package is missing. Install it with:  pip install markdown")
    build(args.public)
    if args.watch:
        print("Watching for changes. Press Ctrl+C to stop.")
        last = fingerprint()
        try:
            while True:
                time.sleep(1)
                cur = fingerprint()
                if cur != last:
                    last = cur
                    try:
                        build(args.public)
                    except SystemExit as e:
                        print("  error:", e)
        except KeyboardInterrupt:
            print()


if __name__ == "__main__":
    main()
