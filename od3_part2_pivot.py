import time, random
def quick_sort(s):
   if len(s) <= 1:
       return s

   element = s[0]
   left = list(filter(lambda i: i < element, s))
   center = [i for i in s if i==element]
   right = list(filter(lambda i: i > element, s))

   return quick_sort(left) + center + quick_sort(right)

a = [random.randint(0, 1000) for _ in range(100)]
start_time = time.time()
quick_sort(a)
end_time = time.time()
print(a)
print(f"Pivot время выполнения: {(end_time-start_time) * 1000000:.12f} наносекунд")

