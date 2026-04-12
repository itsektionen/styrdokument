# IT-sektionens styrdokument

Regulatory documents belonging to the Chapter for Information Technology, written in Markdown.  
The compiled documents are available in PDF form under [the repository's "**Releases**" page](https://github.com/insektionen/styrdokument/releases)

- See [Markdown Cheat sheet](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet) for an introduction to Markdown syntax.
- A more in-depth introduction to writing Markdown is provided [here by GitHub](https://docs.github.com/en/get-started/writing-on-github).
- You should conform to GitHub Flavored Markdown (GFM) when editing these documents, [the formal specification for that dialect can be found here](https://github.github.com/gfm/).

## Repository rules

1. **ONE SENTENCE PER LINE** - in order to make it easier to refer to specific changes, sentences, or sections of text in the files.
2. **ONLY PULL REQUESTS MAY CHANGE THE MAIN BRANCH** - in order to make sure that we are _all_ accountable, and that it is easy to audit historic changes.
3. **ALL PULL REQUESTS MUST BE ACCOMPANIED BY A MOTION OR PROPOSITION** - as the chapter meeting must approve all changes to the regulatory documents.
4. **PROPOSED CHANGES ARE MADE BY BRANCHING OR FORKING THE REPO AND THEN CREATING A PULL REQUEST** - in addition to #2, direct changes to this repo should be avoided as far as possible.
5. **PDF VERSIONS OF THE DOCUMENTS ARE PROVIDED AS RELEASES, NOT WITHIN THE REPO** - new changes or additions -> new release, this is automated via GitHub Actions.

Before writing a motion or proposition that changes some regulatory document, read through and follow the full [Contribution guidelines](docs/CONTRIBUTING.md).

## Repository structure

```text
├── .github - workflows for automatic builds and tests
├── docs - documentation on how to contribute and templates
├── archive - old regulatory documents
├── img - images required by the regulatory documents
├── other_documents - regulations for clubs, the chapter's vision plan
│   ├── eng
│   └── swe
├── pm - the chapter's memos
│   ├── eng
│   └── swe
├── stricts - scrips needed for builds and tests
└── stadgar - the chapter's statutes
    ├── eng
    └── swe
```

## And lastly

§2.1.3 of the chapter's statutes clearly state that _all_ of the chapter's regulatory documents must be published on _the chapter's website_.

The release page, that each repository on GitHub has, is _not_ the chapter's website.
Do not use the release page of this repository as the sole storage of the regulatory documents.

In addition, to ensure the longevity and clean history, please review each other's work thoroughly and merge things in cronological order.
Countless hours have gone into getting all this caught up and organized, so please check an extra time to make sure you don't mess it up.

So, **if you lose or mess up these documents again we will find you!** [imagine a photo of Liam Neeson holding a cellphone]  
If you actually need _any_ help with this repo, contact any of us, really.  
Signed, Ordförande 2016 & Sekreterare 2022
