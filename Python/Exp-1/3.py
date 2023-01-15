def vowels(str1, vowel, char):
    newstr = ""
    for i in range(len(str1)):
        if str1[i] in vowel:
            newstr = newstr + char
        else:
            newstr = newstr + str1[i]
    print("New string: ", newstr)


str1 = input("Enter string: ")
char = "*"
vowel = ['A', 'a', 'E', 'e', 'I', 'i', 'O', 'o', 'U', 'u']

vowels(str1, vowel, char)