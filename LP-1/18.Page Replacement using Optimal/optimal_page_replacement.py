# Page Replacement Algorithm: Optimal

def optimal_page_replacement(pages, frame_count):
    frames = []
    page_faults = 0

    print("\n=== Optimal Page Replacement Algorithm ===\n")
    print(f"Pages: {pages}")
    print(f"Number of Frames: {frame_count}\n")
    print("Page\tFrames\t\tPage Fault")

    for i in range(len(pages)):
        page = pages[i]
        if page not in frames:
            if len(frames) < frame_count:
                frames.append(page)
            else:
                # Predict future use for each page in frames
                future_uses = []
                for f in frames:
                    if f in pages[i + 1:]:
                        next_use = pages[i + 1:].index(f)
                    else:
                        next_use = float('inf')  # Not used again
                    future_uses.append(next_use)

                # Replace the page with the farthest next use
                replace_index = future_uses.index(max(future_uses))
                frames[replace_index] = page
            page_faults += 1
            print(f"{page}\t{frames}\t\tYes")
        else:
            print(f"{page}\t{frames}\t\tNo")

    print("\nTotal Page Faults:", page_faults)


if __name__ == "__main__":
    # Sample Input
    pages = [2, 3, 2, 1, 5, 2, 4, 5, 3, 2, 5, 2]
    frame_count = 3

    optimal_page_replacement(pages, frame_count)
