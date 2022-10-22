"""
Creation: 2022/10/21
Author: https://github.com/smv7
Description: Samples of the Deccano and spaCy .jsonl formats."""


doccano_jsonl_data = [
{"id":2,"text":"Componentes necesarios para jugar la expansión de La Isla. Por si perdió alguno o todos *guiño guino*","label":[[0,12,"PRODUCT_TYPE"],[37,57,"BOARDGAME_NAME"]]},
{"id": 1, "text": "Les traemos un nuevo producto para hacer más amenas sus partidas. Prácticos recipientes para fichas \
  diseñados para poder sacar tus fichas de manera cómoda en partida y facilitar su almacenamiento. Costo del set $4990",
  "label": [[76,99,"PRODUCT_TYPE"], [211,216,"PRODUCT_PRICE"]]},
{"id":6,"text":"Torre de dados de cthulhu. Tenemos cupos inmediato para impresión en filamentos, consulta por tu idea","label":[[0,25,"PRODUCT_TYPE"],[18,25,"BOARDGAME_NAME"],[56,79,"PRODUCT_MATERIAL"]]}
]

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