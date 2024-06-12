import matplotlib.pyplot as plt
import numpy as np
import time

def merge_sort(arr, draw_array, time_interval):
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]

        merge_sort(L, draw_array, time_interval)
        merge_sort(R, draw_array, time_interval)

        i = j = k = 0
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1
            draw_array(arr)
            time.sleep(time_interval)

        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
            draw_array(arr)
            time.sleep(time_interval)

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1
            draw_array(arr)
            time.sleep(time_interval)

def draw_array(arr):
    plt.clf()
    plt.bar(range(len(arr)), arr, color='blue')
    plt.pause(0.01)

def main():
    array = np.random.randint(1, 100, 30)

    plt.figure()
    plt.title("Merge Sort Visualization")

    merge_sort(array, draw_array, 0.1)

    plt.show()

if __name__ == "__main__":
    main()
