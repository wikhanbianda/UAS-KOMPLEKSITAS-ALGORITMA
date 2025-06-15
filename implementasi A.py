import time
import random
import matplotlib.pyplot as plt

# --- Sorting Algorithms ---
def bubble_sort(arr):
    arr = arr.copy()
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

def insertion_sort(arr):
    arr = arr.copy()
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        L = merge_sort(arr[:mid])
        R = merge_sort(arr[mid:])
        return merge(L, R)
    else:
        return arr

def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[0]
    less = [x for x in arr[1:] if x < pivot]
    equal = [x for x in arr if x == pivot]
    greater = [x for x in arr[1:] if x > pivot]
    return quicksort(less) + equal + quicksort(greater)

# --- Searching Algorithms ---
def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

def binary_search(arr, target):
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1

# --- Dataset Sizes ---
sizes = [100, 1000, 10000]
sorting_algorithms = {
    "Bubble Sort": bubble_sort,
    "Insertion Sort": insertion_sort,
    "Merge Sort": merge_sort,
    "Quicksort": quicksort
}
searching_algorithms = {
    "Linear Search": linear_search,
    "Binary Search": binary_search
}

# --- Time Measurement ---
sorting_times = {name: [] for name in sorting_algorithms}
searching_times = {name: [] for name in searching_algorithms}

for size in sizes:
    data = random.sample(range(size * 10), size)
    target = data[size // 2]

    # Sorting
    for name, func in sorting_algorithms.items():
        start = time.time()
        sorted_data = func(data)
        end = time.time()
        sorting_times[name].append((end - start) * 1000)  # in ms

    # Searching
    sorted_for_search = sorted(data)
    for name, func in searching_algorithms.items():
        start = time.time()
        if name == "Binary Search":
            func(sorted_for_search, target)
        else:
            func(data, target)
        end = time.time()
        searching_times[name].append((end - start) * 1000)

# --- Visualization ---
# Sorting Graph
plt.figure(figsize=(10, 5))
for name, times in sorting_times.items():
    plt.plot(sizes, times, label=name)
plt.title('Perbandingan Waktu Eksekusi Sorting')
plt.xlabel('Jumlah Elemen')
plt.ylabel('Waktu (ms)')
plt.legend()
plt.grid(True)
plt.show()

# Searching Graph
plt.figure(figsize=(10, 5))
for name, times in searching_times.items():
    plt.plot(sizes, times, label=name)
plt.title('Perbandingan Waktu Eksekusi Searching')
plt.xlabel('Jumlah Elemen')
plt.ylabel('Waktu (ms)')
plt.legend()
plt.grid(True)
plt.show()
