import matplotlib.pyplot as plt
import numpy as np
import time

def heap_sort(arr, draw_array, time_interval):
    n = len(arr)
    
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i, draw_array, time_interval)

    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        draw_array(arr, i, 0)
        time.sleep(time_interval)
        heapify(arr, i, 0, draw_array, time_interval)

def heapify(arr, n, i, draw_array, time_interval):
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2

    if l < n and arr[l] > arr[largest]:
        largest = l

    if r < n and arr[r] > arr[largest]:
        largest = r

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        draw_array(arr, i, largest)
        time.sleep(time_interval)
        heapify(arr, n, largest, draw_array, time_interval)

def draw_array(arr, current_index, comparison_index):
    plt.clf()
    colors = ['blue'] * len(arr)
    if current_index >= 0:
        colors[current_index] = 'red'
    if comparison_index >= 0:
        colors[comparison_index] = 'green'
    plt.bar(range(len(arr)), arr, color=colors)
    plt.pause(0.01)
    
def main():
    array = np.random.randint(1, 100, 30)

    plt.figure()
    plt.title("Heap Sort Visualization")

    heap_sort(array, draw_array, 0.1)

    plt.show()

if __name__ == "__main__":
    main()
