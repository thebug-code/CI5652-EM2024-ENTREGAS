import random

def power(x, y, p):
     
    # Initialize result
    res = 1; 
     
    # Update x if it is more than or
    # equal to p
    x = x % p; 
    while (y > 0):
         
        # If y is odd, multiply
        # x with result
        if (y & 1):
            res = (res * x) % p;
 
        # y must be even now
        y = y>>1; # y = y/2
        x = (x * x) % p;
     
    return res;

def BTest(a, n):
    s = 0
    t = n - 1
    
    while True:
        s = s + 1
        t = t // 2
        if t % 2 == 1:
            break
    
    print(f"s: {s}, t: {t}")
    print(f"n - 1 = {n - 1} = 2^{s} * {t}")

    x =  power(a, t, n)
    print(f"x = {a}^{t} mod {n} = {x}")
    if x == 1 or x == n - 1:
        return True

    for i in range(1, s):
        x = power(x, 2, n)
        t = t * 2
        print(f"x = {a}^{t} mod {n} = {x}")
        if x == 1:
            return False
        if x == n - 1:
            return True
    return False

def millRab(n, k):
    a = random.randint(2, n - 2)
    print(f"k = {k}")
    print(f"Rabbit test para n = {n} using a = {a}")
    return BTest(a, n)
    
def millRabRep(n, k):
    for i in range(k):
        if millRab(n, i) == False:
            print("Rabbit test determina que n es compuesto")
        else:
            print("Rabbit test determina que n es probablemente primo")
    return
n = 181053518105351810535
millRabRep(n, 10)