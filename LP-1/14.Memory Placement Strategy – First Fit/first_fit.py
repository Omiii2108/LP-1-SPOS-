# Memory Placement Strategy: First Fit

def first_fit(block_size, process_size):
    n = len(block_size)
    m = len(process_size)

    allocation = [-1] * m  # -1 means process not allocated

    # Pick each process and find the first block that fits
    for i in range(m):
        for j in range(n):
            if block_size[j] >= process_size[i]:
                allocation[i] = j
                block_size[j] -= process_size[i]
                break

    # Display results
    print("\n=== Memory Allocation using First Fit ===\n")
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

    first_fit(block_size, process_size)
