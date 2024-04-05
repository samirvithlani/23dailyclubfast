isElig = lambda age : print("eligible") if age>=18 else print("not eligible")
isElig(21)



isPalindrome = lambda name: True if name == name[::-1] else False
x = isPalindrome("madam")
print(x)

if isPalindrome("naman"):
    print("palindrome")
else:
    print("not palindrome")    