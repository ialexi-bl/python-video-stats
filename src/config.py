from os.path import join, dirname
import json

with open(join(dirname(__file__), "config.json"), "r") as fin:
    _config = json.load(fin)

BLUR_THRESHOLD = _config["blurThreshold"]
