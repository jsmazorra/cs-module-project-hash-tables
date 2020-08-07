import random

# Read in all the words in one go.
with open("input.txt") as f:
    words = f.read().split()

# TODO: analyze which words can follow other words
# Your code here
markdict = {}
startwords = []
stop_words = []
prev_word = None

for word in words:
    # first word
    if prev_word == None:
        prev_word = word
        continue
    # stop words, don't add anything to em
    if prev_word.endswith(('.', '?', '!')):
        markdict[prev_word] = []
        prev_word = word
        continue
    # add words
    if prev_word not in markdict:
        # start words
        if prev_word[0].isupper():
            startwords.append(prev_word)
        markdict[prev_word] = [word]
    # already in, just append
    else:
        markdict[prev_word].append(word)
    prev_word = word

# TODO: construct 5 random sentences
# Your code here
for _ in range(5):
    sentence = [random.choice(startwords)]
    for i in range(100):
        sentence.append(random.choice(markdict[sentence[i]]))
        if sentence[i+1].endswith(('.', '?', '!')):
            break
    print(' '.join(sentence))   
