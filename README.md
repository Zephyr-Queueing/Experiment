# Experiment

TODO: Explain repo purpose

TODO: Explain components

TODO: Explain data file organization

The directory `data/` holds the data generated for each experiment. The directory for each distribution model, `zephyr` or `standard`, is denoted by `data/[dm]` where `dm` is the distribution model. Each experiment directory is denoted in the format `data/[dm]/n[X]t[Y]/` where `X` is the number of nodes and `Y` is the number of threads. Data is logged on each individual node which means each individual node has a directory `data/[dm]/n[X]t[Y]/n[Z]` for the node `Z` that the data was copied from. The data from the Quartz server instance is logged in `data/[dm]/n[X]t[Y]/Q` for each experiment.

Assuming the experiment repo is cloned in the the same directory as Quartz or Isopod, data can be moved standing in Quartz or Isopod using the command:
`cp -R log ../Experiment/data/[dm]/n[X]t[Y]/n[Z]` or `cp -R log ../Experiment/data/[dm]/n[X]t[Y]/q`. And then pushed to git as needed from the Experiment repo.
