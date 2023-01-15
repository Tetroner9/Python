def palindrome(str):
    strcheck = str[::-1]
    if strcheck == str:
        print("Its a palindrome")
    else:
        print("Its not a palindrome")


string = input("Enter your string: ")
palindrome(string)
