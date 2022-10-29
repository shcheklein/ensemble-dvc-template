from pathlib import Path
from dvclive import Live
import json

live = Live("evaluation")

s = 0
n = 0

for f in Path("metrics").glob("*.json"):
    n += 1
    with open(f) as jsonfile:
        s += json.load(jsonfile)['acc']

live.log('acc', s / n)

