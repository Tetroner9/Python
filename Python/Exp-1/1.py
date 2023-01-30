def palindrome(string_pal):
    string_check = string_pal[::-1]
    if string_check == string_pal:
        print("Its a palindrome")
    else:
        print("Its not a palindrome")


string = input("Enter your string: ")
palindrome(string)
