def IsPalindrome(word):
    word = word.lower()
    return word == word[::-1]

def GetPalindromes(input_string):
    words = input_string.split()
    palindromes = [word for word in words if IsPalindrome(word)]
    return palindromes

user_input = input("Enter a string: ")
palindromes_list = GetPalindromes(user_input)

if palindromes_list:
    print(f"Palindromes in the entered string: {', '.join(palindromes_list)}")
else:
    print("No palindromes found in the entered string.")
