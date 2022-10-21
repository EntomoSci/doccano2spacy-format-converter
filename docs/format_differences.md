# Doccanos' and Spacy's Format Differences

## Doccano's format
Annotations made in a *named entity recognition* tasks are returned by [Doccano]() in the following format:
- Each entry is a dictionary (because .jsonl) with 3 keys: `id`, `text` and `label`.
-  `id` is a 1-based integer identifier.
- `text` is the actual text sample as a string.
- `label` is a 2D-array where each array element corresponds to the label metadata of one entity with the format: `[start_char_index, end_char_index, label_name]`.

### Example
```json
{"id":1,"text":"Les traemos un nuevo producto para hacer más amenas sus partidas. Prácticos recipientes para fichas diseñados para poder sacar tus fichas de manera cómoda en partida y facilitar su almacenamiento. Costo del set $4990","label":[[76,99,"PRODUCT_TYPE"],[211,216,"PRODUCT_PRICE"]]}
{"id":2,"text":"Componentes necesarios para jugar la expansión de La Isla. Por si perdió alguno o todos *guiño guino*","label":[[0,12,"PRODUCT_TYPE"],[37,57,"BOARDGAME_NAME"]]}
{"id":3,"text":"Otro héroe listo para cumplir con su aventura.que esperas para tener el tuyo? Consulta por tu idea. thetokensmith","label":[]}
```

## Spacy's compatible format
The annotations returned by [Spacy's Prodigy annotation tool]() for *named entity recognition* tasks follows this format:

### Spacy's compatible *.jsonl* format for annotated corpora.
> The training and evaluation datasets are distributed in Prodigy's simple JSONL (newline-delimited JSON) format.
> Each entry contains a `"text"` and a list of `"spans"` with the `"start"` and `"end"` character offsets and the
> `"label"` of the annotated entities. The data also includes the tokenization.
>
> \- [Tutorials with NER annotation of Spacy's creators, Explosion - Github](https://github.com/explosion/projects/tree/v3/tutorials)

### Example
```json
{
  "text": "Bonobos has some long sizes.",
  "tokens": [
    { "text": "Bonobos", "start": 0, "end": 7, "id": 0 },
    { "text": "has", "start": 8, "end": 11, "id": 1 },
    { "text": "some", "start": 12, "end": 16, "id": 2 },
    { "text": "long", "start": 17, "end": 21, "id": 3 },
    { "text": "sizes", "start": 22, "end": 27, "id": 4 },
    { "text": ".", "start": 27, "end": 28, "id": 5 }
  ],
  "spans": [
    {
      "start": 0,
      "end": 7,
      "token_start": 0,
      "token_end": 0,
      "label": "FASHION_BRAND"
    }
  ],
  "_input_hash": -874614165,
  "_task_hash": 2136869442,
  "answer": "accept"
}
```
