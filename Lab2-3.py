
# ---------------------------------------------------------------------------
print("1. Write a Python program to reverse a string")
my_string = "Hello Python"[::-1]
print(my_string)

# ---------------------------------------------------------------------------
print("2. Write a Python program to check if a string is a palindrome (reads the same backward as forward)")
false_palindrome = "Haroon"
print(false_palindrome==false_palindrome[::-1])
true_palindrome = "nanan"
print(true_palindrome==true_palindrome[::-1])



# ---------------------------------------------------------------------------
print("3. Write a Python program to remove duplicate characters from a string.")
string = "Hello this is python lab"
s = ""
for char in string:
    if char not in s:
        s = s+char
print(s)


# ---------------------------------------------------------------------------
print("4. Write a Python program to find the longest word in a given string. ")
text = "Python is a great programming language"
longest_word = ''
words = text.split()
for word in words:
        if len(word)>len(longest_word):
                longest_word=word
print("the longest word is "+ str(longest_word))
'''in one line'''
print(max(input("Enter a string: ").split(), key=len))  



# ---------------------------------------------------------------------------
print("5. Write a Python program to find common elements between two tuples. ")
tuple1 = (1, 2, 3) 
tuple2 = (2, 3, 4) 
common = tuple(set(tuple1) & set(tuple2))
print("the common elements are "+ str(common))


# ---------------------------------------------------------------------------
print("6. Write a Python program to find the maximum and minimum value in a dictionary")
my_dict = {"a": 10, "b": 20, "c": 5}  
print("max value is " + str(max(my_dict.values())))
print("min value is " + str(min(my_dict.values())))


# ---------------------------------------------------------------------------
print("7. Write a Python program to merge two dictionaries")
dict1 = {"a": 1, "b": 2} 
dict2 = {"c": 3, "d": 4} 
dict1.update(dict2)
print(dict1)


# ---------------------------------------------------------------------------
print("8. Write a Python program to find common keys in two dictionaries.")
dict1 = {"a": 1, "b": 2, "c": 3} 
dict2 = {"b": 2, "c": 4, "d": 5} 
common = set(dict1).intersection(dict2)
print(common)


# ---------------------------------------------------------------------------
print("9. takes a string and prints the longest alphabetical ordered substring occured")
userInput = input("Enter a string: ")
substring, current = userInput[0], userInput[0]

for char in userInput[1:]:
    if char.lower() >= current[-1].lower():
        current += char
    else:
        substring = max(substring, current, key=len)
        current = char

print(max(substring, current, key=len))