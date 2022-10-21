# Doccano2SpacyFormatConverter

A CLI tool to convert Doccano's format to the Spacy's compatible format produced by Prodigy.

## Abstract
This project aims to converter the `.jsonl` format returned by the free annotation tool
[Doccano](https://doccano.herokuapp.com/) to the `.jsonl` format returned by the pay option and recommended annotation
tool used by [Spacy](https://spacy.io/): [Prodigy](https://prodi.gy/).

## Rationale
### Is really necessary a custom converter?
With a spaCy's format compatible text annotation tool of 400+ dollars and the fact that handmade annotations are time
expensive and prone to errors, is clear that I need the power of text annotation tools and the advantages that spaCy
provides over other NLP libraries.

Free text annotation tools that are available **must** be usable in the same workflow
where spaCy is being used, that is, compatible in format, which is not the case. So a format converter is needed between free
text annotation tools and spaCy.
