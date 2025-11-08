# Memory Placement Strategy: Next Fit

def next_fit(block_size, process_size):
    n = len(block_size)
    m = len(process_size)
    allocation = [-1] * m  # To store block index for each process
    j = 0  # Start from first block

    # Allocate memory to processes as per Next Fit algorithm
    for i in range(m):
        count = 0  # To avoid infinite loop
        while count < n:
            if block_size[j] >= process_size[i]:
                allocation[i] = j
                block_size[j] -= process_size[i]
                break
            # Move to next block (circular manner)
            j = (j + 1) % n
            count += 1

        # Next process will start checking from the last allocated position
        if allocation[i] != -1:
            j = (allocation[i] + 1) % n

    # Display results
    print("\n=== Memory Allocation using Next Fit ===\n")
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

    next_fit(block_size, process_size)
