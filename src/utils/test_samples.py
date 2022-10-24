"""
Creation: 2022/10/21
Author: https://github.com/smv7
Description: Samples of the Deccano and spaCy .jsonl formats."""


from custom_typehints import (
	DoccanoJsonlLabelTH, DoccanoJsonlEntryTH, DoccanoJsonlDataTH,
	SpacyJsonlTokenTH, SpacyJsonlSpanTH, SpacyJsonlEntryTH, SpacyJsonlDataTH)


#NOTE: The Doccano's .jsonl format examples were extracted from custom sources and then processed by Doccano.
doccano_jsonl_data = [
{"id":2,"text":"Componentes necesarios para jugar la expansión de La Isla. Por si perdió alguno o todos *guiño guino*","label":[[0,12,"PRODUCT_TYPE"],[37,57,"BOARDGAME_NAME"]]},
{"id": 1, "text": "Les traemos un nuevo producto para hacer más amenas sus partidas. Prácticos recipientes para fichas \
  diseñados para poder sacar tus fichas de manera cómoda en partida y facilitar su almacenamiento. Costo del set $4990",
  "label": [[76,99,"PRODUCT_TYPE"], [211,216,"PRODUCT_PRICE"]]},
{"id":6,"text":"Torre de dados de cthulhu. Tenemos cupos inmediato para impresión en filamentos, consulta por tu idea","label":[[0,25,"PRODUCT_TYPE"],[18,25,"BOARDGAME_NAME"],[56,79,"PRODUCT_MATERIAL"]]}
]

#NOTE: The spaCy's .jsonl compatible format examples were extracted from https://github.com/explosion/projects.
spacy_jsonl_data = [{
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
},
{
  "text": "Where do you get the mock duck?",
  "meta": { "section": "Cooking", "utc": "1364690064" },
  "tokens": [
    { "text": "Where", "start": 0, "end": 5, "id": 0 },
    { "text": "do", "start": 6, "end": 8, "id": 1 },
    { "text": "you", "start": 9, "end": 12, "id": 2 },
    { "text": "get", "start": 13, "end": 16, "id": 3 },
    { "text": "the", "start": 17, "end": 20, "id": 4 },
    { "text": "mock", "start": 21, "end": 25, "id": 5 },
    { "text": "duck", "start": 26, "end": 30, "id": 6 },
    { "text": "?", "start": 30, "end": 31, "id": 7 }
  ],
  "spans": [
    {
      "start": 21,
      "end": 30,
      "token_start": 5,
      "token_end": 6,
      "label": "INGRED"
    }
  ],
  "answer": "accept",
  "_input_hash": -768143800,
  "_task_hash": -1459747024
},
{
  "text": "Idk if that Xanax or ur just an ass hole",
  "tokens": [
    { "text": "Idk", "start": 0, "end": 3, "id": 0 },
    { "text": "if", "start": 4, "end": 6, "id": 1 },
    { "text": "that", "start": 7, "end": 11, "id": 2 },
    { "text": "Xanax", "start": 12, "end": 17, "id": 3 },
    { "text": "or", "start": 18, "end": 20, "id": 4 },
    { "text": "ur", "start": 21, "end": 23, "id": 5 },
    { "text": "just", "start": 24, "end": 28, "id": 6 },
    { "text": "an", "start": 29, "end": 31, "id": 7 },
    { "text": "ass", "start": 32, "end": 35, "id": 8 },
    { "text": "hole", "start": 36, "end": 40, "id": 9 }
  ],
  "spans": [
    {
      "start": 12,
      "end": 17,
      "token_start": 3,
      "token_end": 3,
      "label": "DRUG"
    }
  ],
  "_input_hash": -2128862848,
  "_task_hash": -334208479,
  "answer": "accept"
}]

#=============================================================#
# Samples used by the integration test for custom exceptions. #
#=============================================================#
# NOTE: Variables prefixed with "good_" are samples correctly formatted and those prefixed with "bad_" the opposite.

bad_doccano_jsonl_label_samples: list[DoccanoJsonlLabelTH] = [
	(),
    ('label', 1, 1),
    (1, 1, 1),
    (1, 'label', 1),
    ('1', '1', 'label'),
    ('1', 1, 'label'),
    (1, 1, ['label'])]
