tex = input("Enter the alphabet: ")

if tex in ('a', 'e', 'i', 'o', 'u'):
	print("%s is a vowel." % tex)
elif tex == 'y':
	print("Sometimes letter y stand for vowel, sometimes stand for consonant.")
else:
	print("%s is a consonant." % tex) 
