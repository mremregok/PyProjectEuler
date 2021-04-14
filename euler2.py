import time

def Fibonacci(num):
    if num <= 1:
        return 1
    else:
        return (Fibonacci(num-1) + Fibonacci(num-2))

start_time = time.time()

result = 0

limit = 4000000

count = 2

sumOfAll = 0

while True:
    result = Fibonacci(count)
    if result > limit:
        break
    if result % 2 == 0:
        sumOfAll += result
    count += 1

print(sumOfAll)

end_time = time.time()

final_time = end_time - start_time

print(final_time)
