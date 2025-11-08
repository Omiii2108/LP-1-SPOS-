# CPU Scheduling Algorithm: Round Robin (Preemptive)

from collections import deque

def round_robin(processes, time_quantum):
    n = len(processes)
    processes.sort(key=lambda x: x[1])  # Sort by Arrival Time

    remaining_time = [bt for _, at, bt in processes]
    completion_time = [0] * n
    waiting_time = [0] * n
    turnaround_time = [0] * n

    t = 0  # Current time
    ready_queue = deque()
    gantt = []

    # Index to track next process to arrive
    i = 0
    while True:
        # Add all processes that have arrived by current time
        while i < n and processes[i][1] <= t:
            ready_queue.append(i)
            i += 1

        if not ready_queue:
            if i < n:
                # If no process is ready, jump to next arrival
                gantt.append("-")
                t = processes[i][1]
                continue
            else:
                break  # All done

        current = ready_queue.popleft()
        gantt.append(processes[current][0])

        # Execute for one quantum or until completion
        exec_time = min(time_quantum, remaining_time[current])
        remaining_time[current] -= exec_time
        t += exec_time

        # Add new arrivals during this time
        while i < n and processes[i][1] <= t:
            ready_queue.append(i)
            i += 1

        if remaining_time[current] == 0:
            completion_time[current] = t
        else:
            ready_queue.append(current)  # Put back into queue

    # Calculate turnaround and waiting times
    for i in range(n):
        turnaround_time[i] = completion_time[i] - processes[i][1]
        waiting_time[i] = turnaround_time[i] - processes[i][2]

    avg_tat = sum(turnaround_time) / n
    avg_wt = sum(waiting_time) / n

    # Print results
    print("\n=== Round Robin Scheduling (Preemptive) ===\n")
    print(f"Time Quantum = {time_quantum}\n")
    print("Process\tAT\tBT\tCT\tTAT\tWT")
    for i in range(n):
        print(f"{processes[i][0]}\t{processes[i][1]}\t{processes[i][2]}\t{completion_time[i]}\t{turnaround_time[i]}\t{waiting_time[i]}")

    print(f"\nAverage Turnaround Time: {avg_tat:.2f}")
    print(f"Average Waiting Time: {avg_wt:.2f}")

    # Gantt Chart
    print("\nGantt Chart (Execution Order):")
    print(" → ".join(gantt))


if __name__ == "__main__":
    # Sample Input
    time_quantum = 2
    processes = [
        ['P1', 0, 6],
        ['P2', 1, 4],
        ['P3', 4, 8],
        ['P4', 3, 3]
    ]

    round_robin(processes, time_quantum)
