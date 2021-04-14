import time

    

def FindMultiples(number):
    sumFinal = 0
    for i in range(1, number):
        if i % 3 == 0 or i % 5 == 0:
            sumFinal += i
    return sumFinal

start_time = time.time()

print(FindMultiples(1000))

end_time = time.time()

final_time = end_time - start_time

print(final_time)
