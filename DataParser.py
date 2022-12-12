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
        time.append((int(data[0]) - time_0) / 1000)
        q1.append(int(data[1]))
        q2.append(int(data[2]))
        q3.append(int(data[3]))
    plt.plot(time, q1, label="Priority 1")
    plt.plot(time, q2, label="Priority 2")
    plt.plot(time, q3, label="Priority 3")
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
    plt.title("Size over Time w/ " + 
              dm + " " + str(n) + " " + title_n + " " + 
              str(t) + " " + title_t)
    plt.xlabel("Time (s)")
    plt.ylabel("Size")
    plt.savefig("plots/QueueSize_" + dm + "_" + exp + ".png")
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
        time.append((int(data[0]) - time_0) / 1000)
        w1.append(float(data[4]))
        w2.append(float(data[5]))
        w3.append(float(data[6]))
    plt.plot(time, w1, label="Priority 1")
    plt.plot(time, w2, label="Priority 2")
    plt.plot(time, w3, label="Priority 3")
    plt.xlim(0, np.max(time))
    plt.ylim(0, 1)
    plt.legend()
    title_n = "Node"
    title_t = "Thread"
    if n != 1:
        title_n += "s"
    if t != 1:
        title_t += "s"
    plt.title("Weights over Time w/ " + 
              dm + " " + str(n) + " " + title_n + " " + 
              str(t) + " " + title_t)
    plt.xlabel("Time (s)")
    plt.ylabel("Weight")
    plt.savefig("plots/Weight_" + dm + "_" + exp + ".png")
    plt.cla()
    plt.clf()

def plotE2ELatency(dm, exp):
    expDir = "data/" + dm + "/" + exp
    n=int(exp[exp.rindex('n')+1:exp.rindex('t')])
    t=int(exp[exp.rindex('t')+1:])
    t1, t2, t3, l1, l2, l3 = [], [], [], [], [], []
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
                if int(data[1]) == 1:
                    t1.append((int(data[2]) - time_0) / 1000)
                    l1.append((int(data[2]) - int(data[3])) / 1000)
                elif int(data[1]) == 2:
                    t2.append((int(data[2]) - time_0) / 1000)
                    l2.append((int(data[2]) - int(data[3])) / 1000)
                elif int(data[1]) == 3:
                    t3.append((int(data[2]) - time_0) / 1000)
                    l3.append((int(data[2]) - int(data[3])) / 1000)
    plt.plot(t1, l1, label="Priority 1")
    plt.plot(t2, l2, label="Priority 2")
    plt.plot(t3, l3, label="Priority 3")
    plt.axhline(y=0.5, color='red', linestyle='dotted')
    timeMax = [np.max(t1), np.max(t2), np.max(t3)]
    plt.xlim(0, np.max(timeMax))
    sizeMax = [np.max(l1), np.max(l2), np.max(l3)]
    plt.ylim(0, np.max(sizeMax))
    plt.legend()
    title_n = "Node"
    title_t = "Thread"
    if n != 1:
        title_n += "s"
    if t != 1:
        title_t += "s"
    plt.title("End to End Latency over time w/ " + 
              dm + " " + str(n) + " " + title_n + " " + 
              str(t) + " " + title_t)
    plt.xlabel("Time (s)")
    plt.ylabel("Latency (s)")
    plt.savefig("plots/E2ELatency_" + dm + "_" + exp + ".png")
    plt.cla()
    plt.clf()


if True:
    print("Plot queue size:")
    plotQueueSize("Standard", "n1t1")
    # plotQueueSize("Standard", "n3t4")
    plotQueueSize("Zephyr", "n1t1")
    # plotQueueSize("Zephyr", "n3t4")
    
    print("Plot weights:")
    plotWeights("Standard", "n1t1")
    # plotWeights("Standard", "n3t4")
    plotWeights("Zephyr", "n1t1")
    # plotWeights("Zephyr", "n3t4")

    print("Plot end-to-end latency:")
    plotE2ELatency("Standard", "n1t1")
    # plotE2ELatency("Standard", "n3t4")
    plotE2ELatency("Zephyr", "n1t1")
    # plotE2ELatency("Zephyr", "n3t4")
