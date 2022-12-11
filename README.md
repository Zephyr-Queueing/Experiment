# Experiment

TODO: Explain repo purpose

TODO: Explain components

TODO: Explain data file organization

The directory `data/` holds the data generated for each experiment. The directory for each distribution model, `zephyr` or `standard`, is denoted by `data/[dm]` where `dm` is the distribution model. Each experiment directory is denoted in the format `data/[dm]/n[X]t[Y]/` where `X` is the number of nodes and `Y` is the number of threads. Data is logged on each individual node which means each individual node has a directory `data/[dm]/n[X]t[Y]/n[Z]` for the node `Z` that the data was copied from.

Data can be copied for a node Z using the command `scp -r log/ user@host1/com:/path/to/Experiment/data/[dm]/n[X]t[Y]/n[Z]`.
