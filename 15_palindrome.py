def is_palindrome(s):
    s = s.lower().replace(" ", "")  # Convert to lowercase and remove spaces
    return s == s[::-1]#inja sharte palindrome boodan gharar gerefte

input_string = input()
if is_palindrome(input_string):
    print("palindrome")
else:
    print("not palindrome")