def invest(amount, rate, years):
    
    for year in range( 1, years+1):
        amount += amount* rate
        print(f"year {year} : {amount} ")

def main():
    deposit=float(input("Enter the deposit: "))
    foiz=float(input("Enter the rate years: "))
    yil=int(input("Enter the whole year : "))
    invest(deposit, foiz, yil)
    print
if __name__=="__main__":
    main()
   

