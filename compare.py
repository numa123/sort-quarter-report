from bubblesort import bubbleSort;
from insertionsort import insertionSort;
from mergesort import mergeSort;
from quicksort import quickSort;
from heapsort import heapSort;
from radixsort import radixSort;
from shellsort import shellSort;
from selectionsort import selectionSort;
import pandas as pd
import time
from decimal import Decimal, getcontext


def format_time(elapsed_time, significant_figures=5):
    """Format the elapsed time to the specified number of significant figures."""
    # Create a Decimal with the given elapsed time
    elapsed_decimal = Decimal(elapsed_time)

    # Adjust the precision to the significant figures needed
    formatted_time = f"{elapsed_decimal:.{significant_figures}g}"

    return formatted_time

def sort_and_time(sort_function, data, file_size, sort_name):
    # if sort_name == 'quickSort':
    #     copy_data = data.copy()
    #     start_time = time.time()
    #     sorted_arr = sort_function(copy_data, 0, file_size-1)
    #     end_time = time.time()
    #     elapsed_time = end_time - start_time
    #     formatted_time = format_time(elapsed_time)
    #     print(f"{sort_name}: {formatted_time} seconds")
    #     # print(sorted_arr)
    # else:
        copy_data = data.copy()
        start_time = time.time()
        sorted_arr = sort_function(copy_data, file_size)
        end_time = time.time()
        elapsed_time = end_time - start_time
        formatted_time = format_time(elapsed_time)
        print(f"{sort_name}: {formatted_time} seconds")
        # print(sorted_arr)


def main(input_file_path, file_size):
    df = pd.read_csv(input_file_path)
    data = df.values.tolist()

    # heap sort
    sort_and_time(heapSort, data, file_size, 'heapSort')

    # quick sort
    sort_and_time(quickSort, data, file_size, 'quickSort')

    # merge sort
    sort_and_time(mergeSort, data, file_size, "insertionSort")

    # bubble sort
    sort_and_time(bubbleSort, data, file_size, "bubbleSort")

    # insertion sort
    sort_and_time(insertionSort, data, file_size, "insertionSort")

    # shell sort
    sort_and_time(shellSort, data, file_size, 'shellSort')

    # selection sort
    sort_and_time(shellSort, data, file_size, 'selectionSort')

    # radix sort
    sort_and_time(radixSort, data, file_size, 'radixSort')





file_sizes = [100000]

for file_size in file_sizes:
    input_file_path = f"./movie_dataset_subset{file_size}.csv"
    print(f"File size: {file_size}...")
    main(input_file_path, file_size)
