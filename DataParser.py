import matplotlib.pyplot as plt
import numpy as np

def plotTimeVsSize(dm, exp):
    name = "data/" + dm + "/" + exp + "/q"

def plotE2ELatency(dm, exp):
    expDir = "data/" + dm + "/" + exp
    n=int(exp[exp.rindex('n')+1:exp.rindex('t')])
    t=int(exp[exp.rindex('t')+1:])
    time, lat = [], []
    for i in range(n):
        for j in range(t):
            name = expDir + "/n" + str(i) + "/log_T" + str(j) + ".log"
            print(name)
            file = open(name, 'r').readlines()
            for line in range(len(file)):
                data = file[line].split(',')
                time.append(int(data[2]))
                lat.append(int(data[3]) - int(data[2]))
    plt.plot(time, lat)
    plt.savefig("E2ELatency_" + exp + ".png")
    plt.cla()
    plt.clf()


if True:
    print("Plot end-to-end latency:")
    plotE2ELatency("zephyr", "n1t1")
