x = input()
word = x[:x.find(' ')]
wordsec = x[x.find(' ') + 1:]
print(wordsec + ' ' + word)
