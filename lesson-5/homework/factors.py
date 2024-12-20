def factor(n):
    
    for a in range(0, n):
        a += 1
        if n % a ==0:
            print(f" {a} is factor in {n}")

def main():
    factors = int(input("n natural sonni kiriting: "))
    factor(factors)

if __name__ == "__main__":
    main()
