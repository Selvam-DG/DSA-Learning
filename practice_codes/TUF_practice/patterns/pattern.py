def pattern1(n):
    for i in range(n):
        for j in range(n):
            print("* ", end=" ")
        print("")
    
def pattern2(n):
    for i in range(n):
        for j in range(i+1):
            print("*", end=" ")
        print()
 
def pattern3(n):
    for i in range(n):
        for j in range(i+1):
            print(j+1, end=" ")
        print()
        
def pattern4(n):
    for i in range(n):
        for j in range(i+1):
            print(i+1, end=" ")
        print()
     
def pattern5(n):
    for i in range(n):
        for j in range(n-i, 0, -1):
            print("*", end=" ")
        print()

def pattern6(n):
    for i in range(n):
        for j in range(n-i, 0, -1):
            print(n-j-i+1, end=" ")
        print()

def pattern7(n):
    for i in range(n):
        for j in range(n-i-1):
            print(" ", end="")
        for k in range(2*i+1):
            print("*", end="")
        for l in range(n-i-1):
            print(" ", end="")
        print()

def pattern8(n):
    for i in range(n-1, -1 , -1):
        for j in range(n-i-1):
            print(" ", end="")
        for k in range(2*i+1):
            print("*", end="")
        for l in range(n-i-1):
            print(" ", end="")
        print()

def pattern9(n):
    pattern7(n)
    pattern8(n)

def pattern10(n):
    for i in range(1, 2*n-1):
        star = i
        if i > n:
            star = 2*n-i
        for j in range(star):
            print("*", end=" ")
        print()
     
pattern10(5)