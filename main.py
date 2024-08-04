import sys
import time
import random
import numpy as np
import matplotlib.pyplot as plt
from linked_list import LinkedList
from merge_sort import MergeSort
from insertion_sort import InsertionSort

sys.setrecursionlimit(40000)

def measure_sort_time(sorter, sort_method):
    start_time = time.time()
    sorter.sort()
    end_time = time.time()
    sort_time = end_time - start_time
    print(f"Time taken to sort using {sort_method} Sort: {sort_time:.6f} seconds")
    return sort_time

def measure_reversing_time(list_to_rev):
    start_time = time.time()
    list_to_rev.reverse()
    end_time = time.time()
    sort_time = end_time - start_time
    print(f"Time taken to reverse list: {sort_time:.6f} seconds")
    return sort_time

n_values = []
m_times = []
i_times = []

for k in range(0, 20001, 1000):
    n_values.append(k)
    linked_list = LinkedList()
    for i in range(k):
        j = random.randint(1,100000)
        linked_list.make_list(j)

    print("Original List")
    linked_list.display()
    print("\n")

    print("Merge Sort")
    merge_list = linked_list.copy()
    merge_sorter = MergeSort(merge_list)
    merge_time = measure_sort_time(merge_sorter, "merge")
    m_times.append(merge_time)
    merge_list.display()
    print("\n")

    print("Insertion Sort")
    insertion_list = linked_list.copy()
    insertion_sorter = InsertionSort(insertion_list)
    insertion_time = measure_sort_time(insertion_sorter, "insertion")
    i_times.append(insertion_time)
    insertion_list.display()
    print("\n")

    print("Reverse List")
    list_to_rev = merge_list.copy()
    reverse_time = measure_reversing_time(list_to_rev)
    list_to_rev.display()
    print("\n")
    print("\n")

# Create a new figure
plt.figure(figsize=(10, 6))
# Plot Merge Sort times
plt.plot(n_values, m_times, marker='o', linestyle='-', color='b', label='Merge Sort')
# Plot Insertion Sort times
plt.plot(n_values, i_times, marker='x', linestyle='--', color='r', label='Insertion Sort')

# Add labels and title
plt.xlabel('Number of Elements')
plt.ylabel('Time (seconds)')
plt.title('Sorting Time Comparison')
plt.legend()
# Show grid
plt.grid(True)
# Display the plot
plt.show()
