import matplotlib.pyplot as plt
import numpy as np
import time

def bubble_sort(arr, draw_array, time_interval):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                draw_array(arr, j, j+1)
                time.sleep(time_interval)
    draw_array(arr, -1, -1)

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
    plt.title("Bubble Sort Visualization")

    # Run the sorting algorithm with visualization
    bubble_sort(array, draw_array, 0.1)

    # Show the final sorted array
    plt.show()

if __name__ == "__main__":
    main()
