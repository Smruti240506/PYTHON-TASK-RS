str1 = input("Enter first string: ")
str2 = input("Enter second string: ")

if sorted(str1.lower()) == sorted(str2.lower()):
    print("The strings are Anagrams.")
else:
    print("The strings are Not Anagrams.")