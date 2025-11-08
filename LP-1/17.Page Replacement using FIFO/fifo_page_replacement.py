# Page Replacement Algorithm: FIFO

def fifo_page_replacement(pages, frame_count):
    frames = []
    page_faults = 0
    index = 0

    print("\n=== FIFO Page Replacement Algorithm ===\n")
    print(f"Pages: {pages}")
    print(f"Number of Frames: {frame_count}\n")
    print("Page\tFrames\t\tPage Fault")

    for page in pages:
        if page not in frames:
            if len(frames) < frame_count:
                frames.append(page)
            else:
                frames[index] = page
                index = (index + 1) % frame_count
            page_faults += 1
            print(f"{page}\t{frames}\t\tYes")
        else:
            print(f"{page}\t{frames}\t\tNo")

    print("\nTotal Page Faults:", page_faults)


if __name__ == "__main__":
    # Sample Input
    pages = [2, 3, 2, 1, 5, 2, 4, 5, 3, 2, 5, 2]
    frame_count = 3

    fifo_page_replacement(pages, frame_count)
