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

## CLI

Using set of the
[`dvc exp`](https://dvc.org/doc/start/experiment-management/experiments)
commands it's possible to iterate on models and compare different iterations
with each other.

```
vim model-1/params.yaml. # change params
dvc exp run              # run an experiment 
dvc exp show             # show all experiments

# Queue multiple experiments and run them:
dvc exp run --queue -S model-1/params.yaml:res=0.8,0.82,0.84,0.86
dvc exp run --run-all

# Show experimnents again:
dvc exp show
```

https://user-images.githubusercontent.com/3659196/198862257-ad0e4cc0-8265-47a2-98ac-cae590f25373.mp4

Also, it's possible to show plots with:

```
dvc plots show
# or
dvc plots diff
```

<img width="1153" alt="Screen Shot 2022-10-29 at 9 18 39 PM" src="https://user-images.githubusercontent.com/3659196/198862370-a7a5bb09-dfcc-4240-8f63-ef52662d7f2f.png">

## VS Code Extension

Can be installed from the
[marketplace](https://marketplace.visualstudio.com/items?itemName=Iterative.dvc)
and provides a visual layer for DVC experiments, plots, and common actions for
data management.

https://user-images.githubusercontent.com/3659196/198889808-488193f9-c4fa-4f7f-9287-dbc4bf8774be.mp4
