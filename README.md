# styrdokument

Regulatory documents belonging to the Chapter for Information- and Nanotechnology, written in Markdown.  
The compiled documents are available in PDF form under [the repository's "**Releases**" page](https://github.com/insektionen/styrdokument/releases)

See [Markdown Cheat sheet](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet) for an introduction to Markdown syntax.

A more in-depth introduction to writing Markdown is provided [here by GitHub](https://docs.github.com/en/get-started/writing-on-github).

You should conform to GitHub Flavored Markdown (GFM) when editing these documents, [the formal specification for that dialect can be found here](https://github.github.com/gfm/).

## Repository rules

1. **ONE SENTENCE PER LINE** - in order to make it easier to refer to specific changes, sentences, or sections of text in the files.
2. **ONLY PULL REQUESTS MAY CHANGE THE MAIN BRANCH** - in order to make sure that we are *all* accountable, and that it is easy to audit historic changes.
3. **ALL PULL REQUESTS MUST BE ACCOMPANIED BY A MOTION OR PROPOSITION** - as the chapter meeting must approve all changes to the regulatory documents.
4. **PROPOSED CHANGES ARE MADE BY CLONING THE REPO AND THEN CREATING A PULL REQUEST** - in addition to #2, direct changes to this repo should be avoided as far as possible.
5. **PDF VERSIONS OF THE DOCUMENTS ARE PROVIDED AS RELEASES, NOT WITHIN THE REPO** - new changes or additions -> new release, this is automated via GitHub Actions.

## Writing motions or propositions and using this repository

When writing a motion or proposition that changes some regulatory document, do the following:

1. Fork this repository
2. Perform the changes that are part of the motion *in your own fork*, **not** in this repository or any of its branches.
3. Create a pull request in this repository, link to and briefly describe your motion in the pull request.
4. Link to the pull request in your motion; and in the motion explicitly state which line(s) in the affected file(s) that you want to change.
5. Any additions or changes to the proposed changes are done as suggested changes in the pull request on GitHub.

## Repository structure

```text
├── archive - old regulatory documents
├── img - images required by the regulatory documents
├── other_documents - regulations for clubs, the chapter's vision plan
│   ├── eng
│   └── swe
├── pm - the chapter's memos
│   ├── eng
│   └── swe
└── stadgar - the chapter's statutes
    ├── eng
    └── swe
```

## Tips and tricks

- If you are using VS Code, the plugin [markdownlint](https://marketplace.visualstudio.com/items?itemName=DavidAnson.vscode-markdownlint) greatly helps the editing process.

## A comment on performing minor changes such as correcting spelling

All chapter secretaries are **strongly** urged to learn how to utilize editorial changes, this process is known as "redaktionella ändringar" in swedish.  
This greatly cuts down on the deluge of unnecessary propositions from the chapter's board that usually follows any read-through of, or plan to make miniscule changes to, the chapter's regulatory documents.  
This does, however, **not** exempt you from the repository's ruleset.

### And lastly

§2.1.3 of the chapter's statutes clearly state that *all* of the chapter's regulatory documents must be published on *the chapter's website*.  
The release page, that each repository on GitHub has, is *not* the chapter's website.  
Do not use the release page of this repository as the sole storage of the regulatory documents.  
So, **if you lose these documents again I will find you!** [imagine a photo of Liam Neeson holding a cellphone]  
If you actually need *any* help with this repo, contact me, really.  
Signed, Ordf 2016
