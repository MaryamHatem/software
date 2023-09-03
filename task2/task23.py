def anagram(str1, str2):
    if len(str1) != len(str2):
        return False

    sorted_str1 = sorted(str1)
    sorted_str2 = sorted(str2)
    return sorted_str1 == sorted_str2

str1 = input("Enter the first string: ")
str2 = input("Enter the second string: ")

# Perform anagram check
if anagram(str1, str2):
    print("they are anagrams")
else:
    print("they are not anagrams")
