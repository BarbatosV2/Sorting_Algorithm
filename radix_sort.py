import matplotlib.pyplot as plt
import numpy as np
import time

def counting_sort(arr, exp, draw_array, time_interval):
    n = len(arr)
    output = [0] * n
    count = [0] * 10

    for i in range(n):
        index = arr[i] // exp
        count[index % 10] += 1

    for i in range(1, 10):
        count[i] += count[i - 1]

    i = n - 1
    while i >= 0:
        index = arr[i] // exp
        output[count[index % 10] - 1] = arr[i]
        count[index % 10] -= 1
        i -= 1

    for i in range(n):
        arr[i] = output[i]
        draw_array(arr, i, index % 10)
        time.sleep(time_interval)

def radix_sort(arr, draw_array, time_interval):
    max1 = max(arr)
    exp = 1
    while max1 // exp > 0:
        counting_sort(arr, exp, draw_array, time_interval)
        exp *= 10

def draw_array(arr, current_index, digit_place):
    plt.clf()
    colors = ['blue'] * len(arr)
    if current_index >= 0:
        colors[current_index] = 'red'
    plt.bar(range(len(arr)), arr, color=colors)
    plt.pause(0.01)

def main():
    array = np.random.randint(1, 1000, 30)

    plt.figure()
    plt.title("Radix Sort Visualization")

    radix_sort(array, draw_array, 0.1)

    plt.show()

if __name__ == "__main__":
    main()
