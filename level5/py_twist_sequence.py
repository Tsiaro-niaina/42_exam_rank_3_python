""" 
Write a function that rotates an array to the right by k positions.
Rotating right by k means the last k elements move to the front.
"""
def twist_sequence(arr: list[int], k: int) -> list[int]:
    if not arr or k == 0:
        return arr
    k = k % len(arr)
    return arr[-k:] + arr[:-k]


if __name__ == "__main__":
    test_array = [1, 2, 3, 4, 5]
    k = 2
    rotated_array = twist_sequence(test_array, k)
    print(f"Array after rotating right by {k} positions: {rotated_array}")
