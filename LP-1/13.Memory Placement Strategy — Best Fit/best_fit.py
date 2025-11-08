# Memory Placement Strategy: Best Fit

def best_fit(block_size, process_size):
    n = len(block_size)
    m = len(process_size)

    allocation = [-1] * m  # -1 means process not allocated

    # Pick each process and find the best fit block for it
    for i in range(m):
        best_index = -1
        for j in range(n):
            if block_size[j] >= process_size[i]:
                if best_index == -1 or block_size[j] < block_size[best_index]:
                    best_index = j

        # If we found a block for the process
        if best_index != -1:
            allocation[i] = best_index
            block_size[best_index] -= process_size[i]

    # Display results
    print("\n=== Memory Allocation using Best Fit ===\n")
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

    best_fit(block_size, process_size)
