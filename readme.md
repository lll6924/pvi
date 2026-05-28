## Dependencies

See `requirements.txt`.

## Running the experiments

We provide three scripts to run the experiments:
* `run/run.py`: PVI/VI inference for models under `model/`, except for a flow posterior
* `run/run_flow.py`: PVI/VI inference for models under `model/`, with a flow posterior
* `run/run_pdb.py`: PVI/VI inference for models under `jax_posteriordb/`

To run experiment, the following command may be used:
```
python -m run.run [--arg value] ...
```
where `arg` include:
* `model`: The model name is `value`, and must match a class name under `model/` or `jax_posteriordb`
* `objective`: The training objective name is `value`, and must match a class name under `objective`
* `regularizer`: The regularizer name is `value`, and must match a class name under `objective`
* `posterior`: The parametric posterior name is `value`, and must match a class name under `posterior`
* `seed`: The random seed is `value`
* `lamb`: The regularization strength is `value`
* `alpha`: The interval score parameter is `value`
* `s`: The number of \theta samples in the objective is `value`
* `iterations`: The number of training iterations is `value`
* `learning_rate`: The learning rate is `value`
* `optimizer`: The optimizer name is `value`
