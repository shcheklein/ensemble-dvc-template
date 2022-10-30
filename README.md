# DVC Model Ensemble

Skeleton for DVC pipeline to evaluate multiple models together.
An experiment in response to this
[SO question](https://stackoverflow.com/questions/74236782/experiment-tracking-for-multiple-ml-independent-models-using-wandb-in-a-single-m).
There is no actual ML model train code, no frameworks, no actual data. This is
made to showcase the possible project layout, how to run this pipeline to see
metrics, plots, etc.

Explore [CLI](#cli), [VS Code extension](#vs-code-extension),
[Studio](#studio), and [Codespaces](#codespaces) tools to experiments,
visualize, and share the results.

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

<img width="1156" alt="Screen Shot 2022-10-30 at 3 35 23 PM" src="https://user-images.githubusercontent.com/3659196/198904947-02b339eb-8573-4ffe-9430-5c382020a463.png">

## VS Code Extension

Can be installed from the
[marketplace](https://marketplace.visualstudio.com/items?itemName=Iterative.dvc)
and provides a visual layer for DVC experiments, plots, and common actions for
data management.

https://user-images.githubusercontent.com/3659196/198889808-488193f9-c4fa-4f7f-9287-dbc4bf8774be.mp4


## Studio

Open
[public project](https://studio.iterative.ai/user/shcheklein/projects/ensemble-dvc-template-7u1t1fys3z)
for this repository.

[Studio](https://studio.iterative.ai/) (see docs [here](https://dvc.org/doc/studio))
provides a collaborative interface to share experiments, see and manage ML models in
[model registry](https://dvc.org/doc/studio/user-guide/model-registry/what-is-a-model-registry).


https://user-images.githubusercontent.com/3659196/198904752-807a9c8e-7f80-4fea-ba21-efaac4bd91ef.mp4

## Codespaces

Project also can be run in the
[GitHub Codespaces](https://github.com/features/codespaces) for the in browser or descktop
platform that is deployed with one click:

https://user-images.githubusercontent.com/3659196/198906563-b451b951-13f2-45ac-883c-8f03709622c0.mp4


