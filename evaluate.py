from pathlib import Path
from dvclive import Live
import json

live = Live("evaluation")

s = 0
n = 0

for f in Path("dvclive").glob("**/*.json"):
    n += 1
    with open(f) as jsonfile:
        s += json.load(jsonfile)['acc']

live.summary['acc'] =  s / n
live.make_summary()

