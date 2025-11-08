# CPU Scheduling Algorithm: First Come First Serve (FCFS)

def fcfs_scheduling(processes):
    # Sort processes by arrival time
    processes.sort(key=lambda x: x[1])

    start_time = []
    completion_time = []
    turnaround_time = []
    waiting_time = []

    # Calculate all times
    for i in range(len(processes)):
        if i == 0:
            start_time.append(processes[i][1])
        else:
            start_time.append(max(processes[i][1], completion_time[i - 1]))
        completion_time.append(start_time[i] + processes[i][2])
        turnaround_time.append(completion_time[i] - processes[i][1])
        waiting_time.append(turnaround_time[i] - processes[i][2])

    # Calculate averages
    avg_tat = sum(turnaround_time) / len(processes)
    avg_wt = sum(waiting_time) / len(processes)

    # Display results
    print("\n=== FCFS CPU Scheduling ===\n")
    print("Process\tAT\tBT\tST\tCT\tTAT\tWT")
    for i in range(len(processes)):
        print(f"{processes[i][0]}\t{processes[i][1]}\t{processes[i][2]}\t{start_time[i]}\t{completion_time[i]}\t{turnaround_time[i]}\t{waiting_time[i]}")

    print("\nAverage Turnaround Time:", round(avg_tat, 2))
    print("Average Waiting Time:", round(avg_wt, 2))

    # Gantt Chart
    print("\nGantt Chart:")
    for i in range(len(processes)):
        print(f"| {processes[i][0]} ", end="")
    print("|")
    for ct in completion_time:
        print(f"{ct:>3}", end=" ")
    print("\n")


if __name__ == "__main__":
    # Sample Input
    processes = [
        ['P1', 0, 3],
        ['P2', 2, 6],
        ['P3', 4, 4],
        ['P4', 6, 5],
        ['P5', 8, 2]
    ]

    fcfs_scheduling(processes)
