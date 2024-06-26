import matplotlib.pyplot as plt
import numpy as np
import time

def comb_sort(arr, draw_array, time_interval):
    def get_next_gap(gap):
        gap = (gap * 10) // 13
        if gap < 1:
            return 1
        return gap

    n = len(arr)
    gap = n
    swapped = True

    while gap != 1 or swapped:
        gap = get_next_gap(gap)
        swapped = False

        for i in range(0, n-gap):
            if arr[i] > arr[i + gap]:
                arr[i], arr[i + gap] = arr[i + gap], arr[i]
                draw_array(arr, i, i + gap)
                time.sleep(time_interval)
                swapped = True

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
    plt.title("Comb Sort Visualization")

    comb_sort(array, draw_array, 0.1)

    plt.show()

if __name__ == "__main__":
    main()
