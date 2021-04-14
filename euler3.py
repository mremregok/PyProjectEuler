import time

def isPrime(num):
    for i in range(2,num):
        if num % i == 0:
            return False
    return True

def FindLargestPrimeFactor(num):
    largestPrimeFactor = 0
    while True:
        check = False,
        if num == 1:
            break
        if isPrime(num):
            if num > largestPrimeFactor:
                largestPrimeFactor = num
            break
        if num % 2 == 1:
            for i in range(3, num//2, 2):
                print(num, " and ", i)
                if num % i == 0:
                    if isPrime(i):
                        if i > largestPrimeFactor:
                            largestPrimeFactor = i
                    num = num // i
                    check = True
                    break
        else:
            for i in range(2, num//2):
                print(num, " and ", i)
                if num % i == 0:
                    if isPrime(i):
                        if i > largestPrimeFactor:
                            largestPrimeFactor = i
                    num = num // i
                    check = True
                    break
        if not check:
            break
    return largestPrimeFactor

start_time = time.time()

print(FindLargestPrimeFactor(600851475143))

end_time = time.time()

total_time = end_time - start_time

print(total_time)
