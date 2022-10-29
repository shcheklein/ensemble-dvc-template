from dvclive import Live
import dvc.api
import json

params = dvc.api.params_show()
res = params['params.yaml:res']

live = Live("../metrics/model-1")

live.log("acc", res)

