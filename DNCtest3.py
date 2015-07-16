#Name this - Smurf Compression?
#Something about how it's a 5-stage algorihm?

dictNames = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
dictKeys = 'abcdefghijklmnopqrstuvwxyz'

fileString = 'this is some text. this is test text. this is some test text.'

dictKeyIndex = 1
dictNameIndex = 0

longestLen = 3
longestList = []

fileString.replace('<:','<:Aa:>')
A = {'a':'<:'}

while longestLen > 2:
    longest = ''
    i = 0
    while i < len(fileString):
        if fileString[i:i+2] == '<:':
            i += 6
        j = 0
        while j < len(fileString[i+1:]):
            if fileString[i+1:][j:j+2] == '<:':
                j += 6
            else:
                if fileString[i] == fileString[i+1:][j]:
                    candidate = ''
                    matchOver = False
                    if len(fileString[i:i+j]) > len(fileString[i+1+j:]):
                        maxPos = len(fileString[i+j+1:])
                    else:
                        maxPos = len(fileString[i:i+j+1])                         
                    for k in range(maxPos):
                        try:
                            if fileString[i+k] == fileString[i+1:][j+k]:
                                candidate += fileString[i+k]
                            else:
                                matchOver = True
                        except IndexError:
                            print('k is too big :(')
                            pass
                        if matchOver:
                            break
                    if len(candidate) > len(longest):
                        longest = candidate
                j += 1
        i += 1
    dictName = dictNames[dictNameIndex]
    dictKey = dictKeys[dictKeyIndex]
    if len(longest) > 2:
        longestList += [longest]
        fileString = fileString.replace(longest,'<:'+dictName+dictKey+':>')
        dictKeyIndex += 1
        if dictKeyIndex > 25:
            dictNameIndex += 1
            dictKeyIndex = 0
        eval(dictName)[dictKey] = longest
        
    longestLen = len(longest)

#STAGE 2

#Find any instances of dictionary entries occurring within
#other dictionary entries

#First, get rid of unused dictionary names
dictNames = dictNames[:dictNameIndex+1]

for dictName in dictNames:
    for dictKey in eval(dictName).keys():
        for dict2Name in dictNames:
            for dict2Key in eval(dict2Name).keys():
                if (not ((dict2Name == dictName)
                    & (dict2Key == dictKey))
                    & (eval(dict2Name)[dict2Key] != '<:')
                    & ((eval(dict2Name)[dict2Key] in
                       eval(dictName)[dictKey]))):
                    eval(dictName)[dictKey] = \
                    eval(dictName)[dictKey].replace(
                        eval(dict2Name)[dict2Key],
                        '<:'+dict2Name+str(dict2Key)+':>')

#STAGE 3

#Find matching strings longer than 2 characters within
#existing dictionary entries

#This might work if I save the dictionaries as strings an then just
#use the first algorithm?

#USE GENERATORS!!!

#for dictName in dictNames:
#    for dictKey in eval(dictName).keys():
#        for dict2Name in dictNames:
#            for dict2Key in eval(dict2Name).keys():
                
