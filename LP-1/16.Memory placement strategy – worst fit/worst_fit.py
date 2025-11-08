# Memory Placement Strategy: Worst Fit

def worst_fit(block_size, process_size):
    n = len(block_size)
    m = len(process_size)
    allocation = [-1] * m  # -1 means process not allocated

    # Pick each process and find the largest block that fits
    for i in range(m):
        worst_idx = -1
        for j in range(n):
            if block_size[j] >= process_size[i]:
                if worst_idx == -1 or block_size[j] > block_size[worst_idx]:
                    worst_idx = j

        # If a suitable block found, allocate it
        if worst_idx != -1:
            allocation[i] = worst_idx
            block_size[worst_idx] -= process_size[i]

    # Display results
    print("\n=== Memory Allocation using Worst Fit ===\n")
    print("Process No.\tProcess Size\tBlock No.")
    for i in range(m):
        if allocation[i] != -1:
            print(f"P{i+1}\t\t{process_size[i]}\t\t{allocation[i]+1}")
        else:
            print(f"P{i+1}\t\t{process_size[i]}\t\tNot Allocated")


if __name__ == "__main__":
    # Sample Input
    block_size = [100, 500, 200, 300, 600]
    process_size = [212, 417, 112, 426]

    worst_fit(block_size, process_size)
