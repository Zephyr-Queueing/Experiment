# Experiment

TODO: Explain repo purpose

TODO: Explain components

TODO: Explain data file organization

The directory 'data/' holds the data generated for each experiment. Each experiment directory is denoted in the format 'data/n[X]t[Y]/' where X is the number of nodes and Y is the number of threads. Data is logged on each individual nodeZ, where Z is the node number, under 'log/log_T0.log' where 0 is the thread number. That means each individual experiment has a directory 'data/n[X]t[Y]/nZ' for the node that the data was copied from.

Data can be copied for a node Z using the command `scp -r log/ user@host1/com:/path/to/Experiment/data/n[X]t[Y]/nZ`.
