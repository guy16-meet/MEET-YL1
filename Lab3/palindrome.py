def palindrome(word):
	b=word[::-1]
	if (b==word):
		print("true")
	else:
		print("false")

word=input("enter a word")
palindrome(word)

