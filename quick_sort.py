import matplotlib.pyplot as plt
import numpy as np
import time

def quick_sort(arr, low, high, draw_array, time_interval):
    if low < high:
        pi = partition(arr, low, high, draw_array, time_interval)
        quick_sort(arr, low, pi-1, draw_array, time_interval)
        quick_sort(arr, pi+1, high, draw_array, time_interval)

def partition(arr, low, high, draw_array, time_interval):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
            draw_array(arr, i, j)
            time.sleep(time_interval)
    arr[i+1], arr[high] = arr[high], arr[i+1]
    draw_array(arr, i+1, high)
    time.sleep(time_interval)
    return i+1

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
    # Generate an array of random numbers
    array = np.random.randint(1, 100, 30)

    # Set up the plot
    plt.figure()
    plt.title("Quick Sort Visualization")

    # Run the sorting algorithm with visualization
    quick_sort(array, 0, len(array)-1, draw_array, 0.1)

    # Show the final sorted array
    plt.show()

if __name__ == "__main__":
    main()
