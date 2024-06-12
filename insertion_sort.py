import matplotlib.pyplot as plt
import numpy as np
import time

def insertion_sort(arr, draw_array, time_interval):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
            draw_array(arr, j + 1, i)
            time.sleep(time_interval)
        arr[j + 1] = key
        draw_array(arr, j + 1, i)
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
    plt.title("Insertion Sort Visualization")

    insertion_sort(array, draw_array, 0.1)

    plt.show()

if __name__ == "__main__":
    main()
