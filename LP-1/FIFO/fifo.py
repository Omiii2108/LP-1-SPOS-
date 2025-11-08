from collections import deque

def fifo_page_replacement(pages, capacity):
    memory = deque()  # Represents the pages currently in memory (FIFO order)
    page_faults = 0
    memory_states = [] # To store the state of memory after each page reference

    for page in pages:
        current_memory_state = list(memory) # Copy current memory state for logging
        
        if page not in memory:
            page_faults += 1
            if len(memory) == capacity:
                # Remove the oldest page (first-in)
                memory.popleft()
            # Add the new page
            memory.append(page)
        
        # Log the memory state after processing the current page
        memory_states.append(list(memory)) 

    return page_faults, memory_states

if __name__ == "__main__":
    # Example usage:
    page_references = [7, 0, 1, 2, 0, 3,]
    frame_capacity = 2

    faults, states = fifo_page_replacement(page_references, frame_capacity)

    print(f"Page references: {page_references}")
    print(f"Frame capacity: {frame_capacity}")
    print(f"Total page faults: {faults}")
    print("\nMemory states after each page reference:")
    for i, state in enumerate(states):
        print(f"  Reference {i+1} ({page_references[i]}): {state}")