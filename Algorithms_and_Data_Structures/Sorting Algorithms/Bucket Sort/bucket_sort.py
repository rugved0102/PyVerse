def bucket_sort(arr):
    # Create empty buckets
    bucket_count = 10  # Assuming range of input is [0, 1)
    buckets = [[] for _ in range(bucket_count)]
    
    # Distribute input array values into buckets
    for value in arr:
        index = int(bucket_count * value)  # Index in range [0, bucket_count)
        buckets[index].append(value)
    
    # Sort each bucket and concatenate
    sorted_array = []
    for bucket in buckets:
        sorted_array.extend(sorted(bucket))  # You can use any sorting algorithm here
    
    return sorted_array

# Example usage
if __name__ == "__main__":
    arr = [0.78, 0.17, 0.39, 0.26, 0.72, 0.94, 0.21, 0.12, 0.23, 0.68]
    sorted_arr = bucket_sort(arr)
    print("Sorted array:", sorted_arr)
