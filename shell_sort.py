import matplotlib.pyplot as plt
import numpy as np
import time

def shell_sort(arr, draw_array, time_interval):
    n = len(arr)
    gap = n // 2

    while gap > 0:
        for i in range(gap, n):
            temp = arr[i]
            j = i
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap
                draw_array(arr, j, i)
                time.sleep(time_interval)
            arr[j] = temp
            draw_array(arr, j, i)
            time.sleep(time_interval)
        gap //= 2

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
    plt.title("Shell Sort Visualization")

    shell_sort(array, draw_array, 0.1)

    plt.show()

if __name__ == "__main__":
    main()
