import matplotlib.pyplot as plt
import numpy as np
import time

def selection_sort(arr, draw_array, time_interval):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
            draw_array(arr, min_idx, j)
            time.sleep(time_interval)
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
        draw_array(arr, i, min_idx)
        time.sleep(time_interval)

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
    plt.title("Selection Sort Visualization")

    selection_sort(array, draw_array, 0.1)

    plt.show()

if __name__ == "__main__":
    main()
