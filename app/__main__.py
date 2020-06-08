# Round Robin
from tabulate import tabulate
from statistics import mean
from random import randint
import numpy as np


def waiting_time(count, burst_times, waiting_times, quantum):
    remaining_times = burst_times.copy()
    t = 0  # current time

    done = False
    while not done:
        done = True
        for i in range(count):
            if remaining_times[i] > 0:
                done = False
                if remaining_times[i] > quantum:
                    t += quantum
                    remaining_times[i] -= quantum
                # last cycle
                else:
                    t = t + remaining_times[i]
                    waiting_times[i] = t - burst_times[i]
                    # finished
                    remaining_times[i] = 0


def avg_time(tasks, burst_times, quantum):
    waiting_times = [0]*len(tasks)

    waiting_time(len(tasks), burst_times, waiting_times, quantum)
    turnaround_times = burst_times + waiting_times

    print(tabulate({
        "Process number": range(1, len(tasks) + 1),
        "burst time": burst_times,
        "Turnaround time": turnaround_times,
        "Waiting time": waiting_times
    }, headers="keys", tablefmt="html"))
    print(tabulate({
        "Average waiting": [mean(waiting_times)],
        "Average turn around": [mean(turnaround_times)]
    }, headers="keys", tablefmt="html"))


if __name__ == "__main__":
    NUM_PROC = 5
    tasks = np.array([[i, randint(1, 20)] for i in range(1, NUM_PROC)])
    quantum = 2 # time quantum
    avg_time(tasks[:, 0], tasks[:, 1], quantum)
