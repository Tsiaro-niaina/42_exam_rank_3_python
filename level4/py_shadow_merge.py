"""Write a function that merges two sorted lists into one sorted list."""
def shadow_merge(list1: list[int], list2: list[int]) -> list[int]:
    merged = []
    i, j = 0, 0

    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:
            merged.append(list1[i])
            i += 1
        else:
            merged.append(list2[j])
            j += 1


    merged.extend(list1[i:])
    merged.extend(list2[j:])

    return merged


if __name__ == "__main__":
    list1 = [1, 3, 5, 7]
    list2 = [2, 4, 6, 8]
    merged_list = shadow_merge(list1, list2)
    print(f"Merged list: {merged_list}")
