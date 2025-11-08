# CPU Scheduling Algorithm: SJF (Preemptive) / Shortest Remaining Time First

def sjf_preemptive(processes):
    n = len(processes)
    remaining_time = [bt for _, at, bt in processes]
    complete = 0
    t = 0
    minm = float('inf')
    shortest = 0
    check = False
    completion_time = [0] * n

    gantt = []  # To store execution order

    while complete != n:
        # Find process with minimum remaining time at time t
        for j in range(n):
            if (processes[j][1] <= t) and (remaining_time[j] > 0) and (remaining_time[j] < minm):
                minm = remaining_time[j]
                shortest = j
                check = True

        if not check:
            gantt.append("-")
            t += 1
            continue

        # Process execution for 1 unit
        gantt.append(processes[shortest][0])
        remaining_time[shortest] -= 1
        minm = remaining_time[shortest]
        if minm == 0:
            minm = float('inf')

        # If a process gets completely executed
        if remaining_time[shortest] == 0:
            complete += 1
            check = False
            completion_time[shortest] = t + 1

        t += 1

    # Calculate Turnaround Time and Waiting Time
    tat = [0] * n
    wt = [0] * n
    for i in range(n):
        tat[i] = completion_time[i] - processes[i][1]
        wt[i] = tat[i] - processes[i][2]

    avg_tat = sum(tat) / n
    avg_wt = sum(wt) / n

    # Print Results
    print("\n=== SJF (Preemptive) CPU Scheduling ===\n")
    print("Process\tAT\tBT\tCT\tTAT\tWT")
    for i in range(n):
        print(f"{processes[i][0]}\t{processes[i][1]}\t{processes[i][2]}\t{completion_time[i]}\t{tat[i]}\t{wt[i]}")

    print(f"\nAverage Turnaround Time: {avg_tat:.2f}")
    print(f"Average Waiting Time: {avg_wt:.2f}")

    # Print Gantt Chart
    print("\nGantt Chart (Execution Order):")
    print(" → ".join(gantt))


if __name__ == "__main__":
    # Sample Input
    processes = [
        ['P1', 0, 6],
        ['P2', 1, 4],
        ['P3', 4, 8],
        ['P4', 3, 3]
    ]

    sjf_preemptive(processes)
