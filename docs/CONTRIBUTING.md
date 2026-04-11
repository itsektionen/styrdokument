# How to contribute

## Writing motions or propositions and using this repository

Depending on whether you have access to the repository or not, you may create a fork or a branch.
For the chapter secretaries and board, it's highly recommended to make changes in branches, as changes voted at the chapter meeting can be fixed by anyone with access.
This is compared to a fork, which relies on that single person to fix.

1. Branch/Fork this repository
2. Perform the changes that are part of the motion _in your own branch/fork_, **not** in the main branch of this repository.
   (It should be locked for all non-pull request merges).
3. Create a pull request in this repository, link to and briefly describe your motion in the pull request.
4. Link to the pull request in your motion.
5. Any additions or changes to the proposed changes should be done as suggested changes in the pull request on GitHub.

### Performing minor changes such as correcting spelling

All chapter secretaries are **strongly** urged to learn how to utilize editorial changes.
This process is known as "redaktionella ändringar" in Swedish.
This greatly cuts down on the deluge of unnecessary propositions from the chapter's board that usually follows any read-through of, or plan to make minuscule changes to, the chapter's regulatory documents.
Especially if the English parts of the statutes do not match the Swedish, then they can be corrected or reworded without unnecessary propositions.
This does, however, **not** exempt you from the repository's rule set.

## Pull requests

### Naming

The pull request should briefly and simply explain what it changes.
It should be followed by the following format to show the SM and date ` - SM#X 20XX - 20XX-XX-XX`.
For example:

- `Add vice JML president role - SM#1 2025 - 2025-01-20`
- `Update §5.3.3 discharge to 6 months - SM#5 2023/SM#1 2024 - 2023-12-05/2024-01-23` if it has been voted on twice.

### Description

In the pull request rescription, add a short explaination of what is changed.
Together with a link to the propositin/motion as well as the signed chapter meeting protocol.

### Labeling

Always assign the related labels to the pull request.
This includes if the statutes, memos or if it includes editorial changes.
This is to more easily see which pull request has changed what types of files.

To be able to label the pull request, you might need specific access to the repository.
Therefore, those who have it need to add these labels if they are missing.

### Reviewing

It's highly recommended that someone reviews your pull request before it gets merged.
Small errors might not be found for years and can be hard to track down whether they were intended or not.
Double check the points in the PR reminder comment if all things are correct.

Every time something has been voted to be changed with a proposition or a motion at a chapter meeting, the revision date of the affected documents needs to be changed.
This is often missed, so always double-check this before merging.

### Mergning

All pull requests **must** be merged _in chronological order_ of the dates they got approved by a chapter meeting.
If multiple pull requests were voted on at the same chapter meeting, the internal order is not important.

In order for a pull request to be merged, it needs to be approved by the chapter meeting.

There are formatting rules to follow for this repository that will be checked on every pull request automatically.
These are in place to find blatant errors.
However, some things might slip through and they are not super strict, so you always need to double-check your work.

1. One sentence per line, to make it easier to refer to specific sentences.
2. Do **not** break single sentences onto multiple lines.
3. All files should have a trailing newline to prevent unnecessary whitespace commit changes.
4. Memos should start with formalia sections:
   - Purpose
   - History
   - Revising this Memo
5. Only use normal quotation marks, avoid specially formatted opening and closing quotes.
6. The Swedish and English files should match.
   - Same dates in both files.
   - Same number of lines.
   - Same header numbering.

## Releases

As mentioned in the [README](../README.md) repository rules, all changes will be automatically built to the repository's releases.
As a secretary, you should manage these releases.
If multiple pull requests have been merged, only keep the last one for each SM.
Label the release with the SM and year the changes originate from.
Update the text, explaining what has changed.

- Include the following in the release:
  - SM Protocol
  - Changes
  - Editorial Changes (if any)
  - Pull Requests (linked and named)

As a secretary, you can also create a custom named tag for the release.
This allows everyone to easily find a previous state of the repository.
These tags should be named `20XX-SMX`, like `2025-SM3`.
