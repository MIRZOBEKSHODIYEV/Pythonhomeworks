parol=str(input("parolni kiriting"))
list1=[]
iteam=()
if len(parol)<8:
    print("Parol kamida 8 ta belgidan iborat bo'lishi kerak")
elif not any(char.issupper() for char in parol):
    print("kodda bosh harf qatnashishi kerak")
else:
    print("kod mukammal")
