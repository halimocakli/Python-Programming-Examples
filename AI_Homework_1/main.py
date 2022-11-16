from random import randint


def bubble_sort_algorithm(friends: list):
    list_length = len(friends)

    for i in range(list_length - 1, -1, -1):
        swapped = False
        for j in range(i):
            if friends[j][1] > friends[j + 1][1]:
                friends[j], friends[j + 1] = friends[j + 1], friends[j]
                swapped = True
        if not swapped:
            break

    sorted_friends_dict = dict(friends)
    print(f"Bubble Sorted Dict: {sorted_friends_dict}")


def insertion_sort_algorithm(friends: list):
    list_length = len(friends)

    for step in range(1, list_length):
        key = friends[step]
        j = step - 1

        while j >= 0 and key[1] < friends[j][1]:
            friends[j + 1] = friends[j]
            j = j - 1

        friends[j + 1] = key

    sorted_friends_dict = dict(friends)
    print(f"Insertion Sorted Dict: {sorted_friends_dict}")


def merge_sort_algorithm(friends: list):
    list_length = len(friends)

    if list_length > 1:
        mid = list_length // 2

        left = friends[:mid]
        right = friends[mid:]

        merge_sort_algorithm(left)
        merge_sort_algorithm(right)

        i = 0
        j = 0

        k = 0

        while i < len(left) and j < len(right):
            if left[i][1] <= right[j][1]:
                friends[k] = left[i]
                i += 1
            else:
                friends[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            friends[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            friends[k] = right[j]
            j += 1
            k += 1


def quicksort(friends: list):
    list_length = len(friends)

    if list_length < 2:
        return friends

    low, same, high = [], [], []

    pivot = friends[randint(0, list_length - 1)]

    for item in friends:
        if item[1] < pivot[1]:
            low.append(item)
        elif item[1] == pivot[1]:
            same.append(item)
        elif item[1] > pivot[1]:
            high.append(item)

    return quicksort(low) + same + quicksort(high)


def insertion_sort_for_timsort(friends: list, left=0, right=None):
    list_length = len(friends)

    if right is None:
        right = list_length - 1

    for i in range(left + 1, right + 1):
        key = friends[i]
        j = i - 1

        while j >= left and friends[j][1] > key[1]:
            friends[j + 1] = friends[j]
            j = j - 1

        friends[j + 1] = key

    return friends


def merge_sort_for_timsort(left, right):
    if len(left) == 0:
        return right

    if len(right) == 0:
        return left

    result = []
    index_left = index_right = 0

    while len(result) < len(left) + len(right):
        if left[index_left] <= right[index_right]:
            result.append(left[index_left])
            index_left += 1
        else:
            result.append(right[index_right])
            index_right += 1

        if index_right == len(right):
            result += left[index_left:]
            break

        if index_left == len(left):
            result += right[index_right:]
            break

    return result


def timsort_algorithm(friends: list):
    min_run = 32
    list_length = len(friends)

    for i in range(0, list_length, min_run):
        insertion_sort_for_timsort(friends, i, min((i + min_run - 1), list_length - 1))

    size = min_run
    while size < list_length:
        for start in range(0, list_length, size * 2):
            midpoint = start + size - 1
            end = min((start + size * 2 - 1), (list_length - 1))

            merged_array = merge_sort_for_timsort(
                left=friends[start:midpoint + 1],
                right=friends[midpoint + 1:end + 1])

            friends[start:start + len(merged_array)] = merged_array

        size *= 2

    sorted_friends_dict = dict(friends)
    print(f"Tim Sorted Dict: {sorted_friends_dict}")


if __name__ == '__main__':
    # Initializing list of dictionaries named "friends"
    friends = [
        {'name': 'Rachel', 'year': '1969'},
        {'name': 'Ross', 'year': '1966'},
        {'name': 'joey', 'year': '1967'},
        {'name': 'Monica', 'year': '1964'}]

    # Extracting each dictionary into one dictionary
    friends_dict = {item["name"]: item["year"] for item in friends}
    friends_list = list(friends_dict.items())
    friends_list_merge_sort = list(friends_dict.items())

    bubble_sort_algorithm(friends_list)
    insertion_sort_algorithm(friends_list)

    merge_sort_algorithm(friends_list_merge_sort)
    sorted_friends_dict = dict(friends_list_merge_sort)
    print(f"Merge Sorted Dict: {sorted_friends_dict}")

    friends_list_quick_sort = quicksort(friends_list)
    sorted_friends_dict = dict(friends_list_quick_sort)
    print(f"Quick Sorted Dict: {sorted_friends_dict}")

    timsort_algorithm(friends_list)
