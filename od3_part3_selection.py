import time, random

def selection_sort(arr):
   # Проходим по всему списку
   for i in range(len(arr)):
       # Предполагаем, что первый элемент в неотсортированной части - это минимальный
       min_index = i
       # Ищем минимальный элемент в оставшейся части списка
       for j in range(i+1, len(arr)):
           if arr[j] < arr[min_index]:
               min_index = j
       # Меняем местами найденный минимальный элемент с первым элементом в неотсортированной части
       arr[i], arr[min_index] = arr[min_index], arr[i]

# Пример использования
# numbers = [64, 25, 12, 22, 11]
numbers = [random.randint(0, 1000) for _ in range(100)]
start_time = time.time()
selection_sort(numbers)
end_time = time.time()
print(numbers)  # [11, 12, 22, 25, 64]
print(f"Selection время выполнения: {(end_time-start_time) * 1000000:.12f} наносекунд")
