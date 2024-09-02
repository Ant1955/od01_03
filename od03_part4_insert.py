import time, random

# a = [-3, 5, 0, -8, 1, 10, 11, 12, 22, 25, 64, 5, 2, 9, 0, 1, 5, 3, 5, 7, 4, 3, 8, 2]
a = [random.randint(0, 1000) for _ in range(100)]

def insert_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

start_time = time.time()
insert_sort(a)
end_time = time.time()
print(a)
print(f"Insert время выполнения: {(end_time-start_time) * 1000000:.12f} наносекунд")
# Результат: [-8, -3, 0, 1, 5, 10]