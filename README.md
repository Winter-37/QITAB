# Scientific Knowledge

A personal reference site. You write notes in Markdown; `build.py` turns them into one
`index.html` that opens by double-click in any browser, with no internet and no server.

```
Scientific_Knowledge/
├── index.html        the site (generated). Open this.
├── vendor/           equation renderer, fonts and graph library, so everything works offline
├── notes/            your notes. Folders mirror tree.txt; one .md file per note
├── templates/        note.md and paper.md
├── tree.txt          the folder structure and its order
├── src/page.html     the site's design (HTML, CSS, JavaScript)
├── build.py          notes + tree  ->  index.html
└── new_note.py       create a note from a template
```

## One-time setup

```bash
pip install markdown
```

That is only needed to build. Opening `index.html` needs nothing.

## Everyday use

```bash
python3 new_note.py 03_Hartree_Fock_Theory "Restricted Hartree-Fock"   # creates the file from the template
# edit notes/.../restricted-hartree-fock.md
python3 build.py                                     # rebuild index.html
python3 build.py --watch                             # or: rebuild automatically on every save
```

Then refresh the browser tab. `new_note.py` takes a folder path from `tree.txt`, or just its last
part when that is unique (`03_Hartree_Fock_Theory`, `06_Reduced_Density_Matrices`). If the name appears in two places
it lists them and asks for the full path. Any folder page in the site shows the exact command to
copy.

You can also create the file by hand: save any `.md` file inside the right folder under `notes/`.
The folder it sits in is the folder it is filed in.

## The book structure

The notebook is arranged like a book with two folder levels:

- **Parts:** the top-level folders, `04_Electronic_Structure_Theory` for example.
- **Chapters:** the folders inside a part, `04_Electronic_Structure_Theory/03_Hartree_Fock_Theory` for example.
- **Sections:** the notes inside a chapter.

**Numbering.** The site numbers everything from the folder prefixes and the `order` field: Part 4, Chapter 4.3, Section 4.3.5. Every section has **Previous / Next** buttons that walk through the whole book in that order, crossing chapter boundaries. The sidebar is a table of contents, and expanding a chapter lists its sections.

**Chapter introductions.** Each chapter has an `index.md` introduction: what the chapter covers, the path through its sections, what it needs and what it leads to, plus the planned sections still to be written. Keep it up to date when you add a section. Empty chapters are kept and shown as planned.

**`tree.txt`** holds one folder per line, children indented by two spaces. Edit it to add, rename or
reorder parts and chapters, then run `build.py`; it creates the matching folders under `notes/`.
Leading numbers (`04_`) become the numbers in the site; unnumbered names sort where you put them.

If you rename or move a folder that already contains notes, rename the same directory under
`notes/` too (`git mv` keeps history). Notes in a directory that is not in `tree.txt` still appear;
the folder is added at the end of the tree and `build.py` warns you.

A file called `index.md` inside a folder is that folder's introduction. It is shown at the top of
the folder page and is not listed as a note.

## Writing a note

Start from `templates/note.md` (or `paper.md` for a literature summary). The block between the
two `---` lines is metadata:

| Field | Meaning |
|---|---|
| `id` | Stable name used in links and in the address (`index.html#n.<id>`). Do not change it once other notes link to it. Default: the file name. |
| `title` | Page title. Default: the first `# Heading`, else the file name. |
| `summary` | One or two sentences for folder lists and search. |
| `status` | `not-started`, `in-progress`, `complete` or `needs-revision`. |
| `kind` | `theory`, `derivation`, `algorithm`, `implementation`, `comparison`, `paper`, `reference`. Each kind gets an index on the home page. |
| `level` | `introductory`, `intermediate` or `advanced`. |
| `tags` | `[a, b]`. Searched, shown on the note. |
| `prerequisites` | Notes to understand first, by id or title. Shown at the top of the note. |
| `related` | Connected notes that are not prerequisites. |
| `conventions` | Conventions the note uses, from `conventions.txt`. Shown as badges; checked against prerequisites. |
| `key` | Label of the equation shown in the note's hover preview. |
| `order` | Position of the section inside its chapter (lower first). Use steps of 10 so a new section can be slotted in between. The template's 999 puts a new section at the end. Default: alphabetical by title. |
| `date` | `YYYY-MM-DD`, optional. |
| `authors`, `journal`, `year`, `doi` | For papers. |

Everything is optional except that a note needs some text. Any field can be left out.

### Links between notes

- `prerequisites` and `related` in the metadata. The page also builds **Required by** (notes that
  list this one as a prerequisite) and **Mentioned in** (notes that relate to or link to it)
  automatically.
- In the text, `[[note id or title]]` or `[[note id|label to show]]`.
- A link to a note you have not written yet is fine. It shows greyed out as "planned", becomes a
  link once the note exists, and `build.py` lists what is still unwritten.

### Equations

- Inline: `$E=mc^2$`. Display: put `$$ ... $$` on its own lines. `\( ... \)` and `\[ ... \]` also work.
- Write LaTeX normally. Underscores, stars and `<` are safe inside math. Math inside code spans or
  code blocks is left alone.
- Inside a table cell, write `|` normally in math (`$\langle a|b\rangle$`). Do not write `\|`, which
  means the double bar $\|$.
- A single `$` that is not math (a price, for example) is shown as a plain dollar sign.

### Other Markdown

Tables, fenced code blocks (` ```python `), lists, images and links work. For boxed blocks use
admonitions, with a blank line before and everything indented four spaces:

```markdown
!!! example "Worked example"
    Text here, and equations if you like.
```

Types: `example`, `note`, `warning`.
Images and file links are relative to the note: `![diagram](rhf.png)` finds `rhf.png` next to the
note. Keep `notes/` next to `index.html` when you move or publish the site.

## One note, one place

Each note lives in exactly one chapter: the folder its file sits in. There are no shortcuts or
duplicate listings. To connect a note to another chapter, use `prerequisites`, `related` or
`[[a link]]`. `build.py` warns if an old `also:` field is still present and ignores it.

When the same subject turns up in several parts (VQE, embedding, potential energy surfaces), split it
by role rather than copying: theory in one chapter, software details in the software chapter, and
link the two.

## Numbered equations

Put `\label{name}` inside a display equation and it gets a number: the section number plus its place
among the labelled equations of that section, so the second labelled equation of Section 4.3.5 is
(4.3.5.2). Unlabelled equations stay unnumbered.

```markdown
$$
\mathbf F\mathbf C = \mathbf S\mathbf C\boldsymbol\varepsilon
\label{roothaan}
$$
```

Link to it from any note with `[[rhf#roothaan]]` ("Eq. (4.3.5.2)", which jumps to the equation), from
the same note with `[[#roothaan]]`, or with your own words: `[[rhf#roothaan|the Roothaan equations]]`.
Numbers follow the notes when they move. `key: roothaan` in a note's metadata picks the equation its
hover preview shows. `build.py` lists any link to a label that does not exist.

## Conventions

`conventions: [ia-letters, spatial-orbitals, chemists-integrals]` in a note's metadata shows those
conventions as badges under its title (each links to the reference note that explains it). The
allowed values are in `conventions.txt`; add new ones there. A note that converts between two
conventions lists both. `build.py` then warns when a note and one of its prerequisites use different
conventions on the same axis and neither says where the switch happens.

## Hover previews and the Sources page

Pointing at a link to another section (or tabbing to it) shows its number, title, summary,
conventions and key equation; pointing at an equation link shows the equation. The **Sources** page
(link on the home page, or `index.html#sources`) lists every book cited in the notes' `## Source`
sections, with the book sections each note uses, and every paper cited with a DOI. Write citations
as `Authors, *Book Title* (edition, publisher, year), Sec. 3.4` and
`Authors, "Title", *Journal* **vol**, page (year), doi:10....` for them to be picked up.

## Searching, keyboard and copying equations

- **Search** (box at the top, or press `/`): every word must appear somewhere in a section; the best
  matches come first (title, then tags, summary and chapter, then the text). Accents and dashes are
  ignored, so `schrodinger` and `hartree fock` work. Chapters whose names match are listed first, and
  results show the matching passage with the words highlighted. `Enter` opens the first result.
- **Jump** (`Ctrl K`, `⌘K` on a Mac, or the Jump button): type part of a title, a note id such as
  `rhf`, a section number such as `4.3` or `4.3.5`, or an equation number; `↑` `↓` and `Enter` open it.
  With nothing typed it offers the last section you read and the parts.
- **`[` and `]`**: previous and next section in reading order (previous and next chapter on a chapter page).
- **Copy LaTeX**: point at a display equation and press the small `TeX` button at its top left. The
  copy has no `$$` and no closing punctuation; a numbered equation gets its `\label{...}` back.

## Topic map and graphs

The site draws your links as graphs; there is nothing extra to write. `prerequisites`, `related` and
`[[links]]` are all it uses.

- **Map** (button at the top, or `index.html#map`): every section, coloured by part. Filter by part and
  by link kind, find a section by title, select one to light up its links, select it again to open it.
- **Graph panel** on each section page (under Prerequisites, folded by default):
  - *Prerequisite chain*: everything you need before this section, top to bottom, with a reading path
    in book order underneath. Links already implied by another route are not drawn.
  - *Neighbours*: sections one or two steps away through any kind of link.

Honest prerequisites make the chain useful: list what a section really needs, not everything related.

## Look and feel

Fonts and colours are the variables at the top of `src/page.html` (`--display`, `--serif`,
`--mono`, and the colour tokens). To use another font offline, put its `.woff2` file in
`vendor/fonts/` and add an `@font-face` line next to the existing ones. Run `build.py` afterwards.

## Backup and publishing

Keep the folder in Git. `index.html` is generated, but keeping it in the repository means the site
works straight after a clone. Git does not track empty folders; `build.py` recreates them from
`tree.txt`.

To publish later, upload `index.html`, `vendor/` and `notes/` to GitHub Pages, Netlify or
Cloudflare Pages.
