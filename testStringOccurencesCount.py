import numpy as np

#str = 'dhivyakhrishnan'
str='madam'
countsDict = dict()


print()
print('String : ', str)
print()

for i in range(len(str)):
	if ((str[i] in countsDict) == False):
		countsDict[str[i]] = 1
	else:
		countsDict[str[i]] = countsDict[str[i]] + 1

countsList = list(countsDict.values())
nItems = len(countsList)
countsListMod2 = [(countsList[ii] % 2) for ii in range(nItems)]
countsListMod2 = np.array(countsListMod2)
oddOccIndices = np.where(countsListMod2 == 1)
oddOccList = countsListMod2[oddOccIndices]
nOddOcc = len(oddOccList)
print()

if ((nItems % 2) == 0):
	if (nOddOcc == 0):
		print(str, ' can be rearraged as a palindrome')
	else:
		print(str, ' cannot be rearraged as a palindrome')
else:
	if (nOddOcc == 1):
		print(str, ' can be rearraged as a palindrome')
	else:
		print(str, ' cannot be rearraged as a palindrome')

print()
print('countsDict             : ', countsDict)
print('countsList             : ', countsList)
print('countsListMod2         : ', countsListMod2)
print('Odd occurence indices  : ', oddOccIndices)
print('Odd occurences list    : ', oddOccList)
print('nOddOcc                : ', nOddOcc)
print('nItems                 : ', nItems)
print()


