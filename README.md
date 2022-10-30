# doccano2spacy-format-converter

A CLI tool to convert Doccano's format to the Spacy's compatible format produced by Prodigy.

## Abstract
This project aims to converter the `.jsonl` format returned by the free annotation tool
[Doccano](https://doccano.herokuapp.com/) to the `.jsonl` format returned by the pay option and recommended annotation
tool used by [Spacy](https://spacy.io/): [Prodigy](https://prodi.gy/).

## Rationale
### Is really necessary a custom converter?
With a spaCy's format compatible text annotation tool of 400+ dollars and the fact that handmade annotations are time
expensive and prone to errors, is clear that I need the power of text annotation tools and the advantages that spaCy
provides over other NLP libraries. Free text annotation tools that are available **must** be usable in the same workflow
where spaCy is being used, that is, compatible in format, which is not the case. So a format converter is needed between free
text annotation tools and spaCy.

## Usage
Use the following command to know how the format converter can be used with its available supported arguments:
```
d2s
```
(Executing the `d2s` command without any arguments displays the help message by default as it were used `d2s --help`. Feel free to use both interchangeably)
