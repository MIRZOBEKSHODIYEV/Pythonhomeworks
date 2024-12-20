#convert_cel_to_far()
#C=float(input("Temperaturani kiriting(celsiy shkalasida): "))
#F = C * 9/5 + 32
#print(f"havo harorati {F} farangey")
#convert_far_to_cel(
#F=float(input("Temperaturani kiriting(celsiy shkalasida): "))
#C = (F - 32) * 5/9
#print(f"havo harorati {C} farangey")


def convert_celsiy_to_farangey(celsiy):
    return (celsiy * 9/5) + 32
def convert_far_to_cel(farangey):
    return (farangey - 32) * 5/9
def main():
    temp_c=float(input("Enter the temperature in Celsiy: "))
    temp_f=convert_celsiy_to_farangey(temp_c)
    print(f"{temp_c} celsiy : {temp_f} farangey")
    temp_f=float(input("Enter the temperature in farangey: "))
    temp_c=convert_celsiy_to_farangey(temp_f)
    print(f"{temp_f} Farangey : {temp_c} Celsiy \n ")

if __name__== "__main__":
    main()
