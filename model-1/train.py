import json
import pickle

from dvclive import Live
import dvc.api

params = dvc.api.params_show()
res = params['params.yaml:res']
epochs = params['params.yaml:epochs']

live = Live("../dvclive/model-1")


# Read data, just for the sake of a complete example
# that involves data as well
num_entries = sum(1 for line in open('data/data.csv'))


# Native integration with common ML frameworks is supported:
# https://dvc.org/doc/dvclive/api-reference/ml-frameworks
for epoch in range(epochs):
    # train_model(...)
    live.log("acc", res / (epochs - epoch))
    live.next_step()


# Dump model
model = {'my': 'model-1'}
with open('model.pkl', 'wb') as f:
    pickle.dump(model, f)


# Log summary metrics
live.summary["best_acc"] = res
live.summary["num_entries"] = num_entries
live.make_summary()

