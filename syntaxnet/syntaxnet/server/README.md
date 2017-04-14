## Flask Server Setup

```
sudo apt-get install -y python3-pip

export SYNTAXNET_ROOT=$(pwd)
export PARSER_EVAL_PATH=$SYNTAXNET_ROOT/bazel-bin/syntaxnet/parser_eval
export PARSEY_MODEL_DIR=$SYNTAXNET_ROOT/syntaxnet/models/parsey_mcparseface

pip3 install -r $SYNTAXNET_ROOT/syntaxnet/server/requirements.txt
python3 $SYNTAXNET_ROOT/syntaxnet/server/server.py
```

## Example Output

```
$ curl -H "Content-Type: application/json" -X POST -d '{"q":"The quick brown fox jumped over the lazy dog"}' 'http://127.0.0.1:8000/'
{
  "sentence": "The quick brown fox jumped over the lazzy dog",
  "tree": {
    "ROOT": [
      {
        "index": 5,
        "token": "jumped",
        "label": "VERB",
        "pos": "VBD",
        "tree": {
          "nsubj": [
            {
              "index": 4,
              "token": "fox",
              "label": "NOUN",
              "pos": "NN",
              "tree": {
                "det": [
                  {
                    "index": 1,
                    "token": "The",
                    "label": "DET",
                    "pos": "DT"
                  }
                ],
                "amod": [
                  {
                    "index": 2,
                    "token": "quick",
                    "label": "ADJ",
                    "pos": "JJ"
                  },
                  {
                    "index": 3,
                    "token": "brown",
                    "label": "ADJ",
                    "pos": "JJ"
                  }
                ]
              }
            }
          ],
          "prep": [
            {
              "index": 6,
              "token": "over",
              "label": "ADP",
              "pos": "IN",
              "tree": {
                "pobj": [
                  {
                    "index": 9,
                    "token": "dog",
                    "label": "NOUN",
                    "pos": "NN",
                    "tree": {
                      "det": [
                        {
                          "index": 7,
                          "token": "the",
                          "label": "DET",
                          "pos": "DT"
                        }
                      ],
                      "amod": [
                        {
                          "index": 8,
                          "token": "lazy",
                          "label": "ADJ",
                          "pos": "JJ"
                        }
                      ]
                    }
                  }
                ]
              }
            }
          ]
        }
      }
    ]
  }
}
```


## Credits

Flask Server and syntaxnet modifications originally by @JoshData
