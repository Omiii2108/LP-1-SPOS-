# CPU Scheduling Algorithm: Priority Scheduling (Non-Preemptive)

def priority_non_preemptive(processes):
    n = len(processes)
    processes.sort(key=lambda x: x[1])  # Sort by arrival time

    completed = []
    t = 0
    gantt = []
    waiting_time = {}
    turnaround_time = {}
    completion_time = {}

    ready_queue = []

    while len(completed) < n:
        # Add all processes that have arrived by time t
        for p in processes:
            if p not in ready_queue and p not in completed and p[1] <= t:
                ready_queue.append(p)

        if ready_queue:
            # Sort ready queue by Priority (lower number = higher priority)
            ready_queue.sort(key=lambda x: x[3])
            current = ready_queue.pop(0)

            gantt.append(current[0])

            start_time = t
            t += current[2]  # Run till completion (non-preemptive)
            completion_time[current[0]] = t
            turnaround_time[current[0]] = t - current[1]
            waiting_time[current[0]] = turnaround_time[current[0]] - current[2]
            completed.append(current)
        else:
            gantt.append("-")  # Idle time
            t += 1

    avg_tat = sum(turnaround_time.values()) / n
    avg_wt = sum(waiting_time.values()) / n

    # Display Results
    print("\n=== Priority Scheduling (Non-Preemptive) ===\n")
    print("Process\tAT\tBT\tPR\tCT\tTAT\tWT")
    for p in processes:
        print(f"{p[0]}\t{p[1]}\t{p[2]}\t{p[3]}\t{completion_time[p[0]]}\t{turnaround_time[p[0]]}\t{waiting_time[p[0]]}")

    print(f"\nAverage Turnaround Time: {avg_tat:.2f}")
    print(f"Average Waiting Time: {avg_wt:.2f}")

    # Gantt Chart
    print("\nGantt Chart (Execution Order):")
    print(" → ".join(gantt))


if __name__ == "__main__":
    # Sample Input
    # Process | Arrival | Burst | Priority
    processes = [
        ['P1', 0, 8, 1],
        ['P2', 0, 6, 2],
        ['P3', 2, 1, 3],
        ['P4', 3, 2, 0]
    ]

    priority_non_preemptive(processes)
