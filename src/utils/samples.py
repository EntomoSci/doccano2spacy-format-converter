"""
Creation: 2022/10/21
Author: https://github.com/smv7
Description: Samples of the Deccano and spaCy .jsonl formats."""


deccano_entry = {"id": 1,
                 "text": "Les traemos un nuevo producto para hacer más amenas sus partidas. Prácticos recipientes para \
                    fichas diseñados para poder sacar tus fichas de manera cómoda en partida y facilitar su \
                    almacenamiento. Costo del set $4990",
                 "label": [
                    [76,99,"PRODUCT_TYPE"],
                    [211,216,"PRODUCT_PRICE"]
                    ]
                }

spacy_entry = {
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