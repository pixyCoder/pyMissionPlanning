
#sentence = 'My name is pixyCoder'
sentence = 'My name is pixyCoder too'

sentenceLower = sentence.lower()
words = sentenceLower.split()
wordsReversed = words[::-1]

# Alternate approach
nWords = len(words)
for i in range(0,int(0.5*nWords)):
	temp = words[i]
	words[i] = words[nWords-1-i]
	words[nWords-1-i] = temp

# Diplay solution
print()
print(sentence)
print(words)
print(wordsReversed)
print()
