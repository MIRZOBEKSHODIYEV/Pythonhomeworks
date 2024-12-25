def check(divided):
    def wrapper(a, b):
        if b == 0:
            return "Denominator can't be zero"
        return divided(a, b)
    return wrapper

@check
def div(a, b):
    return a / b


print(div(25, 5))  
print(div(25, 0))  