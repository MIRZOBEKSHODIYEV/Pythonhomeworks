txt = "abcabcdabcdeabcdefabcdefgAssalomHello"
vowels = "aeiouAEIOU"  
result = ""  

for i, char in enumerate(txt):
    result += char
    if (i + 1) % 3 == 0 or char in vowels:  
        if i < len(txt) - 1:  
            result += "_"

print(result)
