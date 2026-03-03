def fib(n, k): #n is the month number, k is the number of pairs of rabbits produced by each pair of rabbits each month
    a, b =1, 1 # month 1 and month 2 both have 1 pair initially
    for i in range(2, n):
        #a is the population 2 months ago, b is the population 1 month ago
        new_babies = a * k
        new_total = b + new_babies 

        a = b 
        b = new_total
    return b

n=30
k=2
print(fib(n, k))