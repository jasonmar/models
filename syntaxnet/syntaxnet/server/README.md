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


## Startup Log

This is what Parsey McParseface outputs when starting up.

```
$ python3 /home/syntaxnet/models/syntaxnet/syntaxnet/server/server.py
 * Running on http://0.0.0.0:8000/ (Press CTRL+C to quit)
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: XXX-XXX-XXX
2017-04-14 04:32:39.931021: I syntaxnet/term_frequency_map.cc:101] Loaded 46 terms from syntaxnet/models/parsey_mcparseface/label-map.
2017-04-14 04:32:39.931233: I syntaxnet/embedding_feature_extractor.cc:35] Features: input.digit input.hyphen; input.prefix(length="2") input(1).prefix(length="2") input(2).prefix(length="2") input(3).prefix(length="2") input(-1).prefix(length="2") input(-2).prefix(length="2") input(-3).prefix(length="2") input(-4).prefix(length="2"); input.prefix(length="3") input(1).prefix(length="3") input(2).prefix(length="3") input(3).prefix(length="3") input(-1).prefix(length="3") input(-2).prefix(length="3") input(-3).prefix(length="3") input(-4).prefix(length="3"); input.suffix(length="2") input(1).suffix(length="2") input(2).suffix(length="2") input(3).suffix(length="2") input(-1).suffix(length="2") input(-2).suffix(length="2") input(-3).suffix(length="2") input(-4).suffix(length="2"); input.suffix(length="3") input(1).suffix(length="3") input(2).suffix(length="3") input(3).suffix(length="3") input(-1).suffix(length="3") input(-2).suffix(length="3") input(-3).suffix(length="3") input(-4).suffix(length="3"); input.token.word input(1).token.word input(2).token.word input(3).token.word input(-1).token.word input(-2).token.word input(-3).token.word input(-4).token.word
2017-04-14 04:32:39.931256: I syntaxnet/embedding_feature_extractor.cc:36] Embedding names: other;prefix2;prefix3;suffix2;suffix3;words
2017-04-14 04:32:39.931262: I syntaxnet/embedding_feature_extractor.cc:37] Embedding dims: 8;16;16;16;16;64
2017-04-14 04:32:39.948595: I syntaxnet/term_frequency_map.cc:101] Loaded 46 terms from syntaxnet/models/parsey_mcparseface/label-map.
2017-04-14 04:32:39.948818: I syntaxnet/embedding_feature_extractor.cc:35] Features: stack.child(1).label stack.child(1).sibling(-1).label stack.child(-1).label stack.child(-1).sibling(1).label stack.child(2).label stack.child(-2).label stack(1).child(1).label stack(1).child(1).sibling(-1).label stack(1).child(-1).label stack(1).child(-1).sibling(1).label stack(1).child(2).label stack(1).child(-2).label; input.token.tag input(1).token.tag input(2).token.tag input(3).token.tag stack.token.tag stack.child(1).token.tag stack.child(1).sibling(-1).token.tag stack.child(-1).token.tag stack.child(-1).sibling(1).token.tag stack.child(2).token.tag stack.child(-2).token.tag stack(1).token.tag stack(1).child(1).token.tag stack(1).child(1).sibling(-1).token.tag stack(1).child(-1).token.tag stack(1).child(-1).sibling(1).token.tag stack(1).child(2).token.tag stack(1).child(-2).token.tag stack(2).token.tag stack(3).token.tag; input.token.word input(1).token.word input(2).token.word input(3).token.word stack.token.word stack.child(1).token.word stack.child(1).sibling(-1).token.word stack.child(-1).token.word stack.child(-1).sibling(1).token.word stack.child(2).token.word stack.child(-2).token.word stack(1).token.word stack(1).child(1).token.word stack(1).child(1).sibling(-1).token.word stack(1).child(-1).token.word stack(1).child(-1).sibling(1).token.word stack(1).child(2).token.word stack(1).child(-2).token.word stack(2).token.word stack(3).token.word
2017-04-14 04:32:39.948842: I syntaxnet/embedding_feature_extractor.cc:36] Embedding names: labels;tags;words
2017-04-14 04:32:39.948858: I syntaxnet/embedding_feature_extractor.cc:37] Embedding dims: 32;32;64
2017-04-14 04:32:39.950199: I syntaxnet/term_frequency_map.cc:101] Loaded 49 terms from syntaxnet/models/parsey_mcparseface/tag-map.
2017-04-14 04:32:40.247908: I syntaxnet/term_frequency_map.cc:101] Loaded 46 terms from syntaxnet/models/parsey_mcparseface/label-map.
2017-04-14 04:32:40.248152: I syntaxnet/embedding_feature_extractor.cc:35] Features: input.digit input.hyphen; input.prefix(length="2") input(1).prefix(length="2") input(2).prefix(length="2") input(3).prefix(length="2") input(-1).prefix(length="2") input(-2).prefix(length="2") input(-3).prefix(length="2") input(-4).prefix(length="2"); input.prefix(length="3") input(1).prefix(length="3") input(2).prefix(length="3") input(3).prefix(length="3") input(-1).prefix(length="3") input(-2).prefix(length="3") input(-3).prefix(length="3") input(-4).prefix(length="3"); input.suffix(length="2") input(1).suffix(length="2") input(2).suffix(length="2") input(3).suffix(length="2") input(-1).suffix(length="2") input(-2).suffix(length="2") input(-3).suffix(length="2") input(-4).suffix(length="2"); input.suffix(length="3") input(1).suffix(length="3") input(2).suffix(length="3") input(3).suffix(length="3") input(-1).suffix(length="3") input(-2).suffix(length="3") input(-3).suffix(length="3") input(-4).suffix(length="3"); input.token.word input(1).token.word input(2).token.word input(3).token.word input(-1).token.word input(-2).token.word input(-3).token.word input(-4).token.word
2017-04-14 04:32:40.248176: I syntaxnet/embedding_feature_extractor.cc:36] Embedding names: other;prefix2;prefix3;suffix2;suffix3;words
2017-04-14 04:32:40.248182: I syntaxnet/embedding_feature_extractor.cc:37] Embedding dims: 8;16;16;16;16;64
2017-04-14 04:32:40.259769: I syntaxnet/term_frequency_map.cc:101] Loaded 46 terms from syntaxnet/models/parsey_mcparseface/label-map.
2017-04-14 04:32:40.260000: I syntaxnet/embedding_feature_extractor.cc:35] Features: stack.child(1).label stack.child(1).sibling(-1).label stack.child(-1).label stack.child(-1).sibling(1).label stack.child(2).label stack.child(-2).label stack(1).child(1).label stack(1).child(1).sibling(-1).label stack(1).child(-1).label stack(1).child(-1).sibling(1).label stack(1).child(2).label stack(1).child(-2).label; input.token.tag input(1).token.tag input(2).token.tag input(3).token.tag stack.token.tag stack.child(1).token.tag stack.child(1).sibling(-1).token.tag stack.child(-1).token.tag stack.child(-1).sibling(1).token.tag stack.child(2).token.tag stack.child(-2).token.tag stack(1).token.tag stack(1).child(1).token.tag stack(1).child(1).sibling(-1).token.tag stack(1).child(-1).token.tag stack(1).child(-1).sibling(1).token.tag stack(1).child(2).token.tag stack(1).child(-2).token.tag stack(2).token.tag stack(3).token.tag; input.token.word input(1).token.word input(2).token.word input(3).token.word stack.token.word stack.child(1).token.word stack.child(1).sibling(-1).token.word stack.child(-1).token.word stack.child(-1).sibling(1).token.word stack.child(2).token.word stack.child(-2).token.word stack(1).token.word stack(1).child(1).token.word stack(1).child(1).sibling(-1).token.word stack(1).child(-1).token.word stack(1).child(-1).sibling(1).token.word stack(1).child(2).token.word stack(1).child(-2).token.word stack(2).token.word stack(3).token.word
2017-04-14 04:32:40.260025: I syntaxnet/embedding_feature_extractor.cc:36] Embedding names: labels;tags;words
2017-04-14 04:32:40.260042: I syntaxnet/embedding_feature_extractor.cc:37] Embedding dims: 32;32;64
2017-04-14 04:32:40.261367: I syntaxnet/term_frequency_map.cc:101] Loaded 49 terms from syntaxnet/models/parsey_mcparseface/tag-map.
2017-04-14 04:32:40.817639: I syntaxnet/term_frequency_map.cc:101] Loaded 64036 terms from syntaxnet/models/parsey_mcparseface/word-map.
2017-04-14 04:32:40.818699: I syntaxnet/term_frequency_map.cc:101] Loaded 49 terms from syntaxnet/models/parsey_mcparseface/tag-map.
INFO:tensorflow:Building training network with parameters: feature_sizes: [2 8 8 8 8 8] domain_sizes: [    5 10665 10665  8970  8970 64038]
2017-04-14 04:32:40.831878: I syntaxnet/term_frequency_map.cc:101] Loaded 46 terms from syntaxnet/models/parsey_mcparseface/label-map.
2017-04-14 04:32:40.832009: I syntaxnet/embedding_feature_extractor.cc:35] Features: input.digit input.hyphen; input.prefix(length="2") input(1).prefix(length="2") input(2).prefix(length="2") input(3).prefix(length="2") input(-1).prefix(length="2") input(-2).prefix(length="2") input(-3).prefix(length="2") input(-4).prefix(length="2"); input.prefix(length="3") input(1).prefix(length="3") input(2).prefix(length="3") input(3).prefix(length="3") input(-1).prefix(length="3") input(-2).prefix(length="3") input(-3).prefix(length="3") input(-4).prefix(length="3"); input.suffix(length="2") input(1).suffix(length="2") input(2).suffix(length="2") input(3).suffix(length="2") input(-1).suffix(length="2") input(-2).suffix(length="2") input(-3).suffix(length="2") input(-4).suffix(length="2"); input.suffix(length="3") input(1).suffix(length="3") input(2).suffix(length="3") input(3).suffix(length="3") input(-1).suffix(length="3") input(-2).suffix(length="3") input(-3).suffix(length="3") input(-4).suffix(length="3"); input.token.word input(1).token.word input(2).token.word input(3).token.word input(-1).token.word input(-2).token.word input(-3).token.word input(-4).token.word
2017-04-14 04:32:40.832029: I syntaxnet/embedding_feature_extractor.cc:36] Embedding names: other;prefix2;prefix3;suffix2;suffix3;words
2017-04-14 04:32:40.832034: I syntaxnet/embedding_feature_extractor.cc:37] Embedding dims: 8;16;16;16;16;64
2017-04-14 04:32:40.834037: I syntaxnet/term_frequency_map.cc:101] Loaded 64036 terms from syntaxnet/models/parsey_mcparseface/word-map.
INFO:tensorflow:Building training network with parameters: feature_sizes: [12 20 20] domain_sizes: [   49    51 64038]
2017-04-14 04:32:40.847380: I syntaxnet/term_frequency_map.cc:101] Loaded 46 terms from syntaxnet/models/parsey_mcparseface/label-map.
2017-04-14 04:32:40.847532: I syntaxnet/embedding_feature_extractor.cc:35] Features: stack.child(1).label stack.child(1).sibling(-1).label stack.child(-1).label stack.child(-1).sibling(1).label stack.child(2).label stack.child(-2).label stack(1).child(1).label stack(1).child(1).sibling(-1).label stack(1).child(-1).label stack(1).child(-1).sibling(1).label stack(1).child(2).label stack(1).child(-2).label; input.token.tag input(1).token.tag input(2).token.tag input(3).token.tag stack.token.tag stack.child(1).token.tag stack.child(1).sibling(-1).token.tag stack.child(-1).token.tag stack.child(-1).sibling(1).token.tag stack.child(2).token.tag stack.child(-2).token.tag stack(1).token.tag stack(1).child(1).token.tag stack(1).child(1).sibling(-1).token.tag stack(1).child(-1).token.tag stack(1).child(-1).sibling(1).token.tag stack(1).child(2).token.tag stack(1).child(-2).token.tag stack(2).token.tag stack(3).token.tag; input.token.word input(1).token.word input(2).token.word input(3).token.word stack.token.word stack.child(1).token.word stack.child(1).sibling(-1).token.word stack.child(-1).token.word stack.child(-1).sibling(1).token.word stack.child(2).token.word stack.child(-2).token.word stack(1).token.word stack(1).child(1).token.word stack(1).child(1).sibling(-1).token.word stack(1).child(-1).token.word stack(1).child(-1).sibling(1).token.word stack(1).child(2).token.word stack(1).child(-2).token.word stack(2).token.word stack(3).token.word
2017-04-14 04:32:40.847555: I syntaxnet/embedding_feature_extractor.cc:36] Embedding names: labels;tags;words
2017-04-14 04:32:40.847565: I syntaxnet/embedding_feature_extractor.cc:37] Embedding dims: 32;32;64
2017-04-14 04:32:40.848586: I syntaxnet/term_frequency_map.cc:101] Loaded 49 terms from syntaxnet/models/parsey_mcparseface/tag-map.
2017-04-14 04:32:41.135265: I syntaxnet/term_frequency_map.cc:101] Loaded 64036 terms from syntaxnet/models/parsey_mcparseface/word-map.
2017-04-14 04:32:41.136329: I syntaxnet/term_frequency_map.cc:101] Loaded 49 terms from syntaxnet/models/parsey_mcparseface/tag-map.
INFO:tensorflow:Building training network with parameters: feature_sizes: [2 8 8 8 8 8] domain_sizes: [    5 10665 10665  8970  8970 64038]
2017-04-14 04:32:41.149817: I syntaxnet/term_frequency_map.cc:101] Loaded 46 terms from syntaxnet/models/parsey_mcparseface/label-map.
2017-04-14 04:32:41.149980: I syntaxnet/embedding_feature_extractor.cc:35] Features: input.digit input.hyphen; input.prefix(length="2") input(1).prefix(length="2") input(2).prefix(length="2") input(3).prefix(length="2") input(-1).prefix(length="2") input(-2).prefix(length="2") input(-3).prefix(length="2") input(-4).prefix(length="2"); input.prefix(length="3") input(1).prefix(length="3") input(2).prefix(length="3") input(3).prefix(length="3") input(-1).prefix(length="3") input(-2).prefix(length="3") input(-3).prefix(length="3") input(-4).prefix(length="3"); input.suffix(length="2") input(1).suffix(length="2") input(2).suffix(length="2") input(3).suffix(length="2") input(-1).suffix(length="2") input(-2).suffix(length="2") input(-3).suffix(length="2") input(-4).suffix(length="2"); input.suffix(length="3") input(1).suffix(length="3") input(2).suffix(length="3") input(3).suffix(length="3") input(-1).suffix(length="3") input(-2).suffix(length="3") input(-3).suffix(length="3") input(-4).suffix(length="3"); input.token.word input(1).token.word input(2).token.word input(3).token.word input(-1).token.word input(-2).token.word input(-3).token.word input(-4).token.word
2017-04-14 04:32:41.150004: I syntaxnet/embedding_feature_extractor.cc:36] Embedding names: other;prefix2;prefix3;suffix2;suffix3;words
2017-04-14 04:32:41.150010: I syntaxnet/embedding_feature_extractor.cc:37] Embedding dims: 8;16;16;16;16;64
2017-04-14 04:32:41.154305: I syntaxnet/term_frequency_map.cc:101] Loaded 64036 terms from syntaxnet/models/parsey_mcparseface/word-map.
INFO:tensorflow:Building training network with parameters: feature_sizes: [12 20 20] domain_sizes: [   49    51 64038]
2017-04-14 04:32:41.167142: I syntaxnet/term_frequency_map.cc:101] Loaded 46 terms from syntaxnet/models/parsey_mcparseface/label-map.
2017-04-14 04:32:41.167274: I syntaxnet/embedding_feature_extractor.cc:35] Features: stack.child(1).label stack.child(1).sibling(-1).label stack.child(-1).label stack.child(-1).sibling(1).label stack.child(2).label stack.child(-2).label stack(1).child(1).label stack(1).child(1).sibling(-1).label stack(1).child(-1).label stack(1).child(-1).sibling(1).label stack(1).child(2).label stack(1).child(-2).label; input.token.tag input(1).token.tag input(2).token.tag input(3).token.tag stack.token.tag stack.child(1).token.tag stack.child(1).sibling(-1).token.tag stack.child(-1).token.tag stack.child(-1).sibling(1).token.tag stack.child(2).token.tag stack.child(-2).token.tag stack(1).token.tag stack(1).child(1).token.tag stack(1).child(1).sibling(-1).token.tag stack(1).child(-1).token.tag stack(1).child(-1).sibling(1).token.tag stack(1).child(2).token.tag stack(1).child(-2).token.tag stack(2).token.tag stack(3).token.tag; input.token.word input(1).token.word input(2).token.word input(3).token.word stack.token.word stack.child(1).token.word stack.child(1).sibling(-1).token.word stack.child(-1).token.word stack.child(-1).sibling(1).token.word stack.child(2).token.word stack.child(-2).token.word stack(1).token.word stack(1).child(1).token.word stack(1).child(1).sibling(-1).token.word stack(1).child(-1).token.word stack(1).child(-1).sibling(1).token.word stack(1).child(2).token.word stack(1).child(-2).token.word stack(2).token.word stack(3).token.word
2017-04-14 04:32:41.167295: I syntaxnet/embedding_feature_extractor.cc:36] Embedding names: labels;tags;words
2017-04-14 04:32:41.167301: I syntaxnet/embedding_feature_extractor.cc:37] Embedding dims: 32;32;64
2017-04-14 04:32:41.168305: I syntaxnet/term_frequency_map.cc:101] Loaded 49 terms from syntaxnet/models/parsey_mcparseface/tag-map.
2017-04-14 04:32:41.727863: I syntaxnet/term_frequency_map.cc:101] Loaded 64036 terms from syntaxnet/models/parsey_mcparseface/word-map.
2017-04-14 04:32:41.728886: I syntaxnet/term_frequency_map.cc:101] Loaded 49 terms from syntaxnet/models/parsey_mcparseface/tag-map.
2017-04-14 04:32:41.740795: I syntaxnet/term_frequency_map.cc:101] Loaded 64036 terms from syntaxnet/models/parsey_mcparseface/word-map.
2017-04-14 04:32:42.054108: I syntaxnet/term_frequency_map.cc:101] Loaded 64036 terms from syntaxnet/models/parsey_mcparseface/word-map.
2017-04-14 04:32:42.055194: I syntaxnet/term_frequency_map.cc:101] Loaded 49 terms from syntaxnet/models/parsey_mcparseface/tag-map.
2017-04-14 04:32:42.080004: I syntaxnet/term_frequency_map.cc:101] Loaded 64036 terms from syntaxnet/models/parsey_mcparseface/word-map.
INFO:tensorflow:Restoring parameters from /home/syntaxnet/models/syntaxnet/syntaxnet/models/parsey_mcparseface/parser-params
INFO:tensorflow:Restoring parameters from /home/syntaxnet/models/syntaxnet/syntaxnet/models/parsey_mcparseface/tagger-params
2017-04-14 04:32:42.737416: I syntaxnet/term_frequency_map.cc:101] Loaded 46 terms from syntaxnet/models/parsey_mcparseface/label-map.
2017-04-14 04:32:42.737485: I syntaxnet/embedding_feature_extractor.cc:35] Features: stack.child(1).label stack.child(1).sibling(-1).label stack.child(-1).label stack.child(-1).sibling(1).label stack.child(2).label stack.child(-2).label stack(1).child(1).label stack(1).child(1).sibling(-1).label stack(1).child(-1).label stack(1).child(-1).sibling(1).label stack(1).child(2).label stack(1).child(-2).label; input.token.tag input(1).token.tag input(2).token.tag input(3).token.tag stack.token.tag stack.child(1).token.tag stack.child(1).sibling(-1).token.tag stack.child(-1).token.tag stack.child(-1).sibling(1).token.tag stack.child(2).token.tag stack.child(-2).token.tag stack(1).token.tag stack(1).child(1).token.tag stack(1).child(1).sibling(-1).token.tag stack(1).child(-1).token.tag stack(1).child(-1).sibling(1).token.tag stack(1).child(2).token.tag stack(1).child(-2).token.tag stack(2).token.tag stack(3).token.tag; input.token.word input(1).token.word input(2).token.word input(3).token.word stack.token.word stack.child(1).token.word stack.child(1).sibling(-1).token.word stack.child(-1).token.word stack.child(-1).sibling(1).token.word stack.child(2).token.word stack.child(-2).token.word stack(1).token.word stack(1).child(1).token.word stack(1).child(1).sibling(-1).token.word stack(1).child(-1).token.word stack(1).child(-1).sibling(1).token.word stack(1).child(2).token.word stack(1).child(-2).token.word stack(2).token.word stack(3).token.word
2017-04-14 04:32:42.737506: I syntaxnet/embedding_feature_extractor.cc:36] Embedding names: labels;tags;words
2017-04-14 04:32:42.737512: I syntaxnet/embedding_feature_extractor.cc:37] Embedding dims: 32;32;64
2017-04-14 04:32:42.738530: I syntaxnet/term_frequency_map.cc:101] Loaded 49 terms from syntaxnet/models/parsey_mcparseface/tag-map.
2017-04-14 04:32:42.783566: I syntaxnet/term_frequency_map.cc:101] Loaded 49 terms from syntaxnet/models/parsey_mcparseface/tag-map.
2017-04-14 04:32:42.784345: I syntaxnet/term_frequency_map.cc:101] Loaded 46 terms from syntaxnet/models/parsey_mcparseface/label-map.
2017-04-14 04:32:42.784378: I syntaxnet/embedding_feature_extractor.cc:35] Features: input.digit input.hyphen; input.prefix(length="2") input(1).prefix(length="2") input(2).prefix(length="2") input(3).prefix(length="2") input(-1).prefix(length="2") input(-2).prefix(length="2") input(-3).prefix(length="2") input(-4).prefix(length="2"); input.prefix(length="3") input(1).prefix(length="3") input(2).prefix(length="3") input(3).prefix(length="3") input(-1).prefix(length="3") input(-2).prefix(length="3") input(-3).prefix(length="3") input(-4).prefix(length="3"); input.suffix(length="2") input(1).suffix(length="2") input(2).suffix(length="2") input(3).suffix(length="2") input(-1).suffix(length="2") input(-2).suffix(length="2") input(-3).suffix(length="2") input(-4).suffix(length="2"); input.suffix(length="3") input(1).suffix(length="3") input(2).suffix(length="3") input(3).suffix(length="3") input(-1).suffix(length="3") input(-2).suffix(length="3") input(-3).suffix(length="3") input(-4).suffix(length="3"); input.token.word input(1).token.word input(2).token.word input(3).token.word input(-1).token.word input(-2).token.word input(-3).token.word input(-4).token.word
2017-04-14 04:32:42.784402: I syntaxnet/embedding_feature_extractor.cc:36] Embedding names: other;prefix2;prefix3;suffix2;suffix3;words
2017-04-14 04:32:42.784416: I syntaxnet/embedding_feature_extractor.cc:37] Embedding dims: 8;16;16;16;16;64
INFO:tensorflow:Restoring parameters from /home/syntaxnet/models/syntaxnet/syntaxnet/models/parsey_mcparseface/parser-params
INFO:tensorflow:Restoring parameters from /home/syntaxnet/models/syntaxnet/syntaxnet/models/parsey_mcparseface/tagger-params
2017-04-14 04:32:43.154374: I syntaxnet/term_frequency_map.cc:101] Loaded 46 terms from syntaxnet/models/parsey_mcparseface/label-map.
2017-04-14 04:32:43.154438: I syntaxnet/embedding_feature_extractor.cc:35] Features: stack.child(1).label stack.child(1).sibling(-1).label stack.child(-1).label stack.child(-1).sibling(1).label stack.child(2).label stack.child(-2).label stack(1).child(1).label stack(1).child(1).sibling(-1).label stack(1).child(-1).label stack(1).child(-1).sibling(1).label stack(1).child(2).label stack(1).child(-2).label; input.token.tag input(1).token.tag input(2).token.tag input(3).token.tag stack.token.tag stack.child(1).token.tag stack.child(1).sibling(-1).token.tag stack.child(-1).token.tag stack.child(-1).sibling(1).token.tag stack.child(2).token.tag stack.child(-2).token.tag stack(1).token.tag stack(1).child(1).token.tag stack(1).child(1).sibling(-1).token.tag stack(1).child(-1).token.tag stack(1).child(-1).sibling(1).token.tag stack(1).child(2).token.tag stack(1).child(-2).token.tag stack(2).token.tag stack(3).token.tag; input.token.word input(1).token.word input(2).token.word input(3).token.word stack.token.word stack.child(1).token.word stack.child(1).sibling(-1).token.word stack.child(-1).token.word stack.child(-1).sibling(1).token.word stack.child(2).token.word stack.child(-2).token.word stack(1).token.word stack(1).child(1).token.word stack(1).child(1).sibling(-1).token.word stack(1).child(-1).token.word stack(1).child(-1).sibling(1).token.word stack(1).child(2).token.word stack(1).child(-2).token.word stack(2).token.word stack(3).token.word
2017-04-14 04:32:43.154460: I syntaxnet/embedding_feature_extractor.cc:36] Embedding names: labels;tags;words
2017-04-14 04:32:43.154474: I syntaxnet/embedding_feature_extractor.cc:37] Embedding dims: 32;32;64
2017-04-14 04:32:43.155527: I syntaxnet/term_frequency_map.cc:101] Loaded 49 terms from syntaxnet/models/parsey_mcparseface/tag-map.
2017-04-14 04:32:43.213254: I syntaxnet/term_frequency_map.cc:101] Loaded 49 terms from syntaxnet/models/parsey_mcparseface/tag-map.
2017-04-14 04:32:43.214825: I syntaxnet/term_frequency_map.cc:101] Loaded 46 terms from syntaxnet/models/parsey_mcparseface/label-map.
2017-04-14 04:32:43.214872: I syntaxnet/embedding_feature_extractor.cc:35] Features: input.digit input.hyphen; input.prefix(length="2") input(1).prefix(length="2") input(2).prefix(length="2") input(3).prefix(length="2") input(-1).prefix(length="2") input(-2).prefix(length="2") input(-3).prefix(length="2") input(-4).prefix(length="2"); input.prefix(length="3") input(1).prefix(length="3") input(2).prefix(length="3") input(3).prefix(length="3") input(-1).prefix(length="3") input(-2).prefix(length="3") input(-3).prefix(length="3") input(-4).prefix(length="3"); input.suffix(length="2") input(1).suffix(length="2") input(2).suffix(length="2") input(3).suffix(length="2") input(-1).suffix(length="2") input(-2).suffix(length="2") input(-3).suffix(length="2") input(-4).suffix(length="2"); input.suffix(length="3") input(1).suffix(length="3") input(2).suffix(length="3") input(3).suffix(length="3") input(-1).suffix(length="3") input(-2).suffix(length="3") input(-3).suffix(length="3") input(-4).suffix(length="3"); input.token.word input(1).token.word input(2).token.word input(3).token.word input(-1).token.word input(-2).token.word input(-3).token.word input(-4).token.word
2017-04-14 04:32:43.214899: I syntaxnet/embedding_feature_extractor.cc:36] Embedding names: other;prefix2;prefix3;suffix2;suffix3;words
2017-04-14 04:32:43.214919: I syntaxnet/embedding_feature_extractor.cc:37] Embedding dims: 8;16;16;16;16;64
2017-04-14 04:32:43.762259: I syntaxnet/term_frequency_map.cc:101] Loaded 64036 terms from syntaxnet/models/parsey_mcparseface/word-map.
2017-04-14 04:32:43.788334: I syntaxnet/term_frequency_map.cc:101] Loaded 64036 terms from syntaxnet/models/parsey_mcparseface/word-map.
2017-04-14 04:32:44.060976: I syntaxnet/term_frequency_map.cc:101] Loaded 64036 terms from syntaxnet/models/parsey_mcparseface/word-map.
2017-04-14 04:32:44.166586: I syntaxnet/term_frequency_map.cc:101] Loaded 64036 terms from syntaxnet/models/parsey_mcparseface/word-map.
INFO:tensorflow:Processed 1 documents
INFO:tensorflow:Total processed documents: 1
INFO:tensorflow:num correct tokens: 0
INFO:tensorflow:total tokens: 9
INFO:tensorflow:Seconds elapsed in evaluation: 13.02, eval metric: 0.00%
2017-04-14 04:32:56.216488: I syntaxnet/embedding_feature_extractor.cc:35] Features: input.digit input.hyphen; input.prefix(length="2") input(1).prefix(length="2") input(2).prefix(length="2") input(3).prefix(length="2") input(-1).prefix(length="2") input(-2).prefix(length="2") input(-3).prefix(length="2") input(-4).prefix(length="2"); input.prefix(length="3") input(1).prefix(length="3") input(2).prefix(length="3") input(3).prefix(length="3") input(-1).prefix(length="3") input(-2).prefix(length="3") input(-3).prefix(length="3") input(-4).prefix(length="3"); input.suffix(length="2") input(1).suffix(length="2") input(2).suffix(length="2") input(3).suffix(length="2") input(-1).suffix(length="2") input(-2).suffix(length="2") input(-3).suffix(length="2") input(-4).suffix(length="2"); input.suffix(length="3") input(1).suffix(length="3") input(2).suffix(length="3") input(3).suffix(length="3") input(-1).suffix(length="3") input(-2).suffix(length="3") input(-3).suffix(length="3") input(-4).suffix(length="3"); input.token.word input(1).token.word input(2).token.word input(3).token.word input(-1).token.word input(-2).token.word input(-3).token.word input(-4).token.word
2017-04-14 04:32:56.216535: I syntaxnet/embedding_feature_extractor.cc:36] Embedding names: other;prefix2;prefix3;suffix2;suffix3;words
2017-04-14 04:32:56.216542: I syntaxnet/embedding_feature_extractor.cc:37] Embedding dims: 8;16;16;16;16;64
INFO:tensorflow:Restoring parameters from /home/syntaxnet/models/syntaxnet/syntaxnet/models/parsey_mcparseface/tagger-params
2017-04-14 04:32:56.694711: I syntaxnet/embedding_feature_extractor.cc:35] Features: input.digit input.hyphen; input.prefix(length="2") input(1).prefix(length="2") input(2).prefix(length="2") input(3).prefix(length="2") input(-1).prefix(length="2") input(-2).prefix(length="2") input(-3).prefix(length="2") input(-4).prefix(length="2"); input.prefix(length="3") input(1).prefix(length="3") input(2).prefix(length="3") input(3).prefix(length="3") input(-1).prefix(length="3") input(-2).prefix(length="3") input(-3).prefix(length="3") input(-4).prefix(length="3"); input.suffix(length="2") input(1).suffix(length="2") input(2).suffix(length="2") input(3).suffix(length="2") input(-1).suffix(length="2") input(-2).suffix(length="2") input(-3).suffix(length="2") input(-4).suffix(length="2"); input.suffix(length="3") input(1).suffix(length="3") input(2).suffix(length="3") input(3).suffix(length="3") input(-1).suffix(length="3") input(-2).suffix(length="3") input(-3).suffix(length="3") input(-4).suffix(length="3"); input.token.word input(1).token.word input(2).token.word input(3).token.word input(-1).token.word input(-2).token.word input(-3).token.word input(-4).token.word
2017-04-14 04:32:56.694757: I syntaxnet/embedding_feature_extractor.cc:36] Embedding names: other;prefix2;prefix3;suffix2;suffix3;words
2017-04-14 04:32:56.694765: I syntaxnet/embedding_feature_extractor.cc:37] Embedding dims: 8;16;16;16;16;64
INFO:tensorflow:Processed 1 documents
INFO:tensorflow:Total processed documents: 1
INFO:tensorflow:num correct tokens: 1
INFO:tensorflow:total tokens: 9
INFO:tensorflow:Seconds elapsed in evaluation: 13.59, eval metric: 11.11%
2017-04-14 04:32:56.738668: I syntaxnet/embedding_feature_extractor.cc:35] Features: stack.child(1).label stack.child(1).sibling(-1).label stack.child(-1).label stack.child(-1).sibling(1).label stack.child(2).label stack.child(-2).label stack(1).child(1).label stack(1).child(1).sibling(-1).label stack(1).child(-1).label stack(1).child(-1).sibling(1).label stack(1).child(2).label stack(1).child(-2).label; input.token.tag input(1).token.tag input(2).token.tag input(3).token.tag stack.token.tag stack.child(1).token.tag stack.child(1).sibling(-1).token.tag stack.child(-1).token.tag stack.child(-1).sibling(1).token.tag stack.child(2).token.tag stack.child(-2).token.tag stack(1).token.tag stack(1).child(1).token.tag stack(1).child(1).sibling(-1).token.tag stack(1).child(-1).token.tag stack(1).child(-1).sibling(1).token.tag stack(1).child(2).token.tag stack(1).child(-2).token.tag stack(2).token.tag stack(3).token.tag; input.token.word input(1).token.word input(2).token.word input(3).token.word stack.token.word stack.child(1).token.word stack.child(1).sibling(-1).token.word stack.child(-1).token.word stack.child(-1).sibling(1).token.word stack.child(2).token.word stack.child(-2).token.word stack(1).token.word stack(1).child(1).token.word stack(1).child(1).sibling(-1).token.word stack(1).child(-1).token.word stack(1).child(-1).sibling(1).token.word stack(1).child(2).token.word stack(1).child(-2).token.word stack(2).token.word stack(3).token.word
2017-04-14 04:32:56.738711: I syntaxnet/embedding_feature_extractor.cc:36] Embedding names: labels;tags;words
2017-04-14 04:32:56.738725: I syntaxnet/embedding_feature_extractor.cc:37] Embedding dims: 32;32;64
INFO:tensorflow:Restoring parameters from /home/syntaxnet/models/syntaxnet/syntaxnet/models/parsey_mcparseface/parser-params
2017-04-14 04:32:57.129121: I syntaxnet/embedding_feature_extractor.cc:35] Features: stack.child(1).label stack.child(1).sibling(-1).label stack.child(-1).label stack.child(-1).sibling(1).label stack.child(2).label stack.child(-2).label stack(1).child(1).label stack(1).child(1).sibling(-1).label stack(1).child(-1).label stack(1).child(-1).sibling(1).label stack(1).child(2).label stack(1).child(-2).label; input.token.tag input(1).token.tag input(2).token.tag input(3).token.tag stack.token.tag stack.child(1).token.tag stack.child(1).sibling(-1).token.tag stack.child(-1).token.tag stack.child(-1).sibling(1).token.tag stack.child(2).token.tag stack.child(-2).token.tag stack(1).token.tag stack(1).child(1).token.tag stack(1).child(1).sibling(-1).token.tag stack(1).child(-1).token.tag stack(1).child(-1).sibling(1).token.tag stack(1).child(2).token.tag stack(1).child(-2).token.tag stack(2).token.tag stack(3).token.tag; input.token.word input(1).token.word input(2).token.word input(3).token.word stack.token.word stack.child(1).token.word stack.child(1).sibling(-1).token.word stack.child(-1).token.word stack.child(-1).sibling(1).token.word stack.child(2).token.word stack.child(-2).token.word stack(1).token.word stack(1).child(1).token.word stack(1).child(1).sibling(-1).token.word stack(1).child(-1).token.word stack(1).child(-1).sibling(1).token.word stack(1).child(2).token.word stack(1).child(-2).token.word stack(2).token.word stack(3).token.word
2017-04-14 04:32:57.129171: I syntaxnet/embedding_feature_extractor.cc:36] Embedding names: labels;tags;words
2017-04-14 04:32:57.129178: I syntaxnet/embedding_feature_extractor.cc:37] Embedding dims: 32;32;64

```