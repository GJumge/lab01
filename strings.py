strings = ['This', 'list', 'is', 'now', 'all', 'together']
sentence = ''

#sentence = 'yo ' + 'hello'
#print(sentence)


for word in strings:
    sentence = sentence + ' ' + word
print(sentence[1:])
    