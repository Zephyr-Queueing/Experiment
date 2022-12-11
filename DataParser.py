import matplotlib.pyplot as plt
import numpy as np

def plotQueueSize(dm, exp):
    name = "data/" + dm + "/" + exp + "/q/log.log"
    print(name)
    n=int(exp[exp.rindex('n')+1:exp.rindex('t')])
    t=int(exp[exp.rindex('t')+1:])
    time, q1, q2, q3 = [], [], [], []
    time_0 = 0
    file = open(name, 'r').readlines()
    for line in range(len(file)):
        data = file[line].split(',')
        if line == 0:
            time_0 = int(data[0])
        time.append(int(data[0]) - time_0)
        q1.append(int(data[1]))
        q2.append(int(data[2]))
        q3.append(int(data[3]))
    plt.plot(time, q1, label="Q1 Size")
    plt.plot(time, q2, label="Q2 Size")
    plt.plot(time, q3, label="Q3 Size")
    plt.xlim(0, np.max(time))
    sizeMax = [np.max(q1), np.max(q2), np.max(q3)]
    plt.ylim(0, np.max(sizeMax))
    plt.legend()
    title_n = "Node"
    title_t = "Thread"
    if n != 1:
        title_n += "s"
    if t != 1:
        title_t += "s"
    plt.title("Time vs Queue Size with " + 
              str(n) + " " + title_n + " " + 
              str(t) + " " + title_t)
    plt.xlabel("Time (ms)")
    plt.ylabel("Size")
    plt.savefig("plots/QueueSize_" + exp + ".png")
    plt.cla()
    plt.clf()

def plotWeights(dm, exp):
    name = "data/" + dm + "/" + exp + "/q/log.log"
    print(name)
    n=int(exp[exp.rindex('n')+1:exp.rindex('t')])
    t=int(exp[exp.rindex('t')+1:])
    time, w1, w2, w3 = [], [], [], []
    time_0 = 0
    file = open(name, 'r').readlines()
    for line in range(len(file)):
        data = file[line].split(',')
        if line == 0:
            time_0 = int(data[0])
        time.append(int(data[0]) - time_0)
        w1.append(float(data[4]))
        w2.append(float(data[5]))
        w3.append(float(data[6]))
    plt.plot(time, w1, label="Weight 1 Size")
    plt.plot(time, w2, label="Weight 2 Size")
    plt.plot(time, w3, label="Weight 3 Size")
    plt.xlim(0, np.max(time))
    plt.ylim(0, 1)
    plt.legend()
    title_n = "Node"
    title_t = "Thread"
    if n != 1:
        title_n += "s"
    if t != 1:
        title_t += "s"
    plt.title("Time vs Weights with " + 
              str(n) + " " + title_n + " " + 
              str(t) + " " + title_t)
    plt.xlabel("Time (ms)")
    plt.ylabel("Weight")
    plt.savefig("plots/Weight_" + exp + ".png")
    plt.cla()
    plt.clf()

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
            time_0 = 0
            for line in range(len(file)):
                data = file[line].split(',')
                if line == 0:
                    time_0 = int(data[2])
                    prev = time_0
                if prev != int(data[2]):
                    time.append((int(data[2]) - time_0))
                    lat.append((int(data[2]) - int(data[3])))
                prev = int(data[2])
    plt.plot(time, lat)
    plt.xlim(0, np.max(time))
    plt.ylim(0, np.max(lat))
    title_n = "Node"
    title_t = "Thread"
    if n != 1:
        title_n += "s"
    if t != 1:
        title_t += "s"
    plt.title("Time vs End to End Queue Latency with " + 
              str(n) + " " + title_n + " " + 
              str(t) + " " + title_t)
    plt.xlabel("Time (ms)")
    plt.ylabel("Latency (ms)")
    plt.savefig("plots/E2ELatency_" + exp + ".png")
    plt.cla()
    plt.clf()


if True:
    print("Plot queue size:")
    plotQueueSize("standard", "n1t1")
    # plotQueueSize("standard", "n3t4")
    # plotQueueSize("zephyr", "n1t1")
    # plotQueueSize("zephyr", "n3t4")
    
    print("Plot weights:")
    plotWeights("standard", "n1t1")
    # plotWeights("standard", "n3t4")
    # plotWeights("zephyr", "n1t1")
    # plotWeights("zephyr", "n3t4")

    print("Plot end-to-end latency:")
    plotE2ELatency("standard", "n1t1")
    # plotE2ELatency("standard", "n3t4")
    # plotE2ELatency("zephyr", "n1t1")
    # plotE2ELatency("zephyr", "n3t4")
