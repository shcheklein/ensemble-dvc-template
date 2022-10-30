# DVC Model Ensemble

Skeleton for DVC pipeline to evaluate multiple models together.
An experiment in response to this
[SO question](https://stackoverflow.com/questions/74236782/experiment-tracking-for-multiple-ml-independent-models-using-wandb-in-a-single-m).
There is no actual ML model train code, no frameworks, no actual data. This is
made to showcase the possible project layout, how to run this pipeline to see
metrics, plots, etc.

## Stucture

```
.
├── LICENSE
├── README.md

# Project / pipeline definition (dvc.yaml) and
# project artifacts and dependecies snapshot (dvc.lock)

├── dvc.lock
├── dvc.yaml

# Metrics, plots that are logger via `dvclive` logger
# https://dvc.org/doc/dvclive
# This is similar to TB, W&B, MLFlow, etc loggers

├── dvclive
│   ├── model-1
│   │   ├── metrics.json
│   │   └── plots
│   │       └── metrics
│   │           └── acc.tsv

...  # Any number of models

│   └── model-N

# Evaluation script that can read multiple models or their metrics
# and dumps aggregare metrics

├── evaluate.py
├── evaluation
│   └── metrics.json

# Mode data, train, and model itself.
# If data and model are large they could be tracked and saved to any
# supported remote storage. Here we put them in Git for simplicity.

├── model-1
│   ├── data
│   │   └── data.csv
│   ├── data.dvc
│   ├── model.pkl
│   ├── params.yaml
│   └── train.py

...  # Any number of model

├── model-N
    ...
└── requirements.txt
```
