#!/usr/bin/python3
import json
import os
import subprocess
from collections import OrderedDict
from flask import Flask, request, Response
from multiprocessing import Pool
from typing import List

ROOT_DIR = os.environ.get('SYNTAXNET_ROOT', 'models/syntaxnet')
PARSER_EVAL = os.environ.get('PARSER_EVAL_PATH', 'bazel-bin/syntaxnet/parser_eval')
MODEL_DIR = os.environ.get('PARSEY_MODEL_DIR', 'syntaxnet/models/parsey_mcparseface')


def open_parser_eval(args: List[str]):
  return subprocess.Popen(
    [PARSER_EVAL] + args,
    cwd=ROOT_DIR,
    stdin=subprocess.PIPE,
    stdout=subprocess.PIPE
  )


def send_input(process: subprocess.Popen, input: str):
  process.stdin.write(input.encode("utf8"))
  process.stdin.write(b"\n\n")  # signal end of documents
  process.stdin.flush()
  response = b""
  while True:
    line = process.stdout.readline()
    if line.strip() == b"":
      # empty line signals end of response
      break
    response += line
  return response.decode("utf8")


# Open the part-of-speech tagger.
pos_tagger = open_parser_eval([
  "--input=stdin",
  "--output=stdout-conll",
  "--hidden_layer_sizes=64",
  "--arg_prefix=brain_tagger",
  "--graph_builder=structured",
  "--task_context=" + MODEL_DIR + "/context.pbtxt",
  "--model_path=" + MODEL_DIR + "/tagger-params",
  "--slim_model",
  "--batch_size=1024",
  "--alsologtostderr",
])

# Open the syntactic dependency parser.
dependency_parser = open_parser_eval([
  "--input=stdin-conll",
  "--output=stdout-conll",
  "--hidden_layer_sizes=512,512",
  "--arg_prefix=brain_parser",
  "--graph_builder=structured",
  "--task_context=" + MODEL_DIR + "/context.pbtxt",
  "--model_path=" + MODEL_DIR + "/parser-params",
  "--slim_model",
  "--batch_size=1024",
  "--alsologtostderr",
])


def split_tokens(parse):
  # Format the result.
  def format_token(line):
    x = OrderedDict(zip(
      ["index", "token", "unknown1", "label", "pos", "unknown2", "parent", "relation", "unknown3", "unknown4"],
      line.split("\t")
    ))
    x["index"] = int(x["index"])
    x["parent"] = int(x["parent"])
    del x["unknown1"]
    del x["unknown2"]
    del x["unknown3"]
    del x["unknown4"]
    return x

  return [
    format_token(line)
    for line in parse.strip().split("\n")
  ]


def parse_sentence(sentence):
  if "\n" in sentence or "\r" in sentence:
    raise ValueError()

  # Do POS tagging.
  pos_tags = send_input(pos_tagger, sentence + "\n")

  # Do syntax parsing.
  dependency_parse = send_input(dependency_parser, pos_tags)

  # Make a tree.
  dependency_parse = split_tokens(dependency_parse)
  tokens = {tok["index"]: tok for tok in dependency_parse}
  tokens[0] = OrderedDict([("sentence", sentence)])
  for tok in dependency_parse:
    tokens[tok['parent']] \
      .setdefault('tree', OrderedDict()) \
      .setdefault(tok['relation'], []) \
      .append(tok)
    del tok['parent']
    del tok['relation']

  return tokens[0]


app = Flask(__name__)
host = '0.0.0.0'
port = 80 if os.getuid() == 0 else 8000

pool = Pool(1, maxtasksperchild=50)

@app.route('/')
def index():
  req_dict = request.get_json()
  if req_dict is not None:
    q = req_dict.get('q')
  else:
    q = request.args.get('q')

  if q is None:
    r = Response(
      response='q is required',
      status=400,
      content_type='text/plain'
    )
    return r

  result = pool.apply(parse_sentence, [q])

  r = Response(
    response=json.dumps(result, indent=2),
    status=200,
    content_type='application/json'
  )
  return r

if __name__ == '__main__':
  app.run(debug=True, port=port, host=host)
