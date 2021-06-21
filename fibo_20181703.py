import time


def fibo(num):
    if num <= 1:
        return num
    return fibo(num - 1) + fibo(num - 2)

def interfibo(num):
    first_num =1
    second_num = 1
    result = 0
    if num ==1:
        return  first_num
    elif num ==2:
        return second_num
    else :
        for i in range(num-2):
            result = first_num +second_num
            first_num = second_num
            second_num = result
        return result
while True:
    nbr = int(input("Enter a number: "))
    if nbr == -1:
        break
    ts = time.time()
    fibonumber = interfibo(nbr)
    ts = time.time() - ts
    print("iterfibo(%d)=%d, time %.6f" %(nbr, fibonumber, ts))
    ts = time.time()
    fibonumber = fibo(nbr)
    ts = time.time() - ts
    print("fibo(%d) = %d, time %.6f"%(nbr , fibonumber ,ts))
