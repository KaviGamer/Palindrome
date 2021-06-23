def palindrome(s):
    return s == s[::-1]

s = input("WRITE A WORD TO SEE IF IT IS A PALINDROME OR NOT > ")
ans = palindrome(s)
 
if ans:
    print("Yes")
else:
    print("No")