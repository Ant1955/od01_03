
import time, random
# mas = [5, 7, 4, 3, 8, 2]
mas = [random.randint(0, 1000) for _ in range(100)]
n = 100
start_time = time.time()
for run in range(n-1):
   for i in range(n-1-run):
       if mas[i] > mas[i + 1]:
           mas[i], mas[i + 1] = mas[i + 1], mas[i]
end_time = time.time()
print(mas)
print(f"Bubble время выполнения: {(end_time-start_time) * 1000000:.12f} наносекунд")

