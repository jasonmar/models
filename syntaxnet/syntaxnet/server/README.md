Flask Server and syntaxnet modifications originally by @JoshData


sudo apt-get install -y python3-pip

export SYNTAXNET_ROOT=$(pwd)
export PARSER_EVAL_PATH=$SYNTAXNET_ROOT/bazel-bin/syntaxnet/parser_eval
export PARSEY_MODEL_DIR=$SYNTAXNET_ROOT/syntaxnet/models/parsey_mcparseface

pip3 install -r $SYNTAXNET_ROOT/syntaxnet/server/requirements.txt
python3 $SYNTAXNET_ROOT/syntaxnet/server/server.py

