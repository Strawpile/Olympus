import re
import time

lst = []
d = {}
word_list = []
def_list = []
known_words = {}
unknown_words = {}

fhand = open('vocab.txt')

#get the first n vocab words from the file, and put them in a list
n = 0
for line in fhand:
    if n > 10:
        break
    else:
        lst.append(line)
        n+=1

#join the elements of the list into a string
for item in lst:
    s = ' '.join([str(elem) for elem in lst])


#parse out the vocab words and their defintions
wrds_defs = re.findall(r'\b\w+\s+\([vna]d*j*\.\)\s+.*\n*.*\.', s)
print(wrds_defs)
for item in wrds_defs:
    vocab_word = item.split()
    word = vocab_word[0]
    word_list.append(word)
    vocab_word.pop(0)
    vocab_word.pop(0)

    definition = ' '.join([str(elem) for elem in vocab_word])

    d[word] = definition
    def_list.append(d[word])
    print ('The word is: ' + word)
    print('The definition of the word is: ' + definition)


for key, val in d.items():
    print ('Think about the word: '+ key)
    time.sleep(3)
    print('Definition: ' + val)
    answr = input('Did you know the word? ').lower().rstrip()
    if answr[0] == 'y':
        known_words[key] = val


print('These are the words you know: ')
for key, val in known_words.items():
    print(key)





#for line in wrds_defs:
    #print(line)
    #print('\n')
    #build a dictionary of the word with its def.
    #w = re.match(r'\b\w+\s', line)
    #if w:
        #print((w.groups(w)))
    #word = re.findall(r'\b\w+\s', line)
    #meaning = re.findall(r'\)\s\w+\.$', line)
    #print(word)
    #print(meaning)
