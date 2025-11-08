# Page Replacement Algorithm: LRU (Least Recently Used)

def lru_page_replacement(pages, frame_count):
    frames = []
    page_faults = 0
    recent_use = {}

    print("\n=== LRU Page Replacement Algorithm ===\n")
    print(f"Pages: {pages}")
    print(f"Number of Frames: {frame_count}\n")
    print("Page\tFrames\t\tPage Fault")

    for i, page in enumerate(pages):
        if page not in frames:
            if len(frames) < frame_count:
                frames.append(page)
            else:
                # Find least recently used page
                lru_page = min(recent_use, key=recent_use.get)
                lru_index = frames.index(lru_page)
                frames[lru_index] = page
                del recent_use[lru_page]
            page_faults += 1
            print(f"{page}\t{frames}\t\tYes")
        else:
            print(f"{page}\t{frames}\t\tNo")

        # Update recent use
        recent_use[page] = i

    print("\nTotal Page Faults:", page_faults)


if __name__ == "__main__":
    # Sample Input
    pages = [2, 3, 2, 1, 5, 2, 4, 5, 3, 2, 5, 2]
    frame_count = 3

    lru_page_replacement(pages, frame_count)
