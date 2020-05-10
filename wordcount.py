import sys
from collections import Counter


def word_count(fnames):
    files = [open(fname) for fname in fnames] 

    all_words = []
    
    for file in files:
        for line in file:
            line = line.rstrip()
            words = line.split(" ")
            words = [word.strip("'\",.!/?-#$%^&();:_").lower() for word in words]
            
            all_words += words
    
    return {word: all_words.count(word) for word in all_words}


# def word_count(fnames):
#     files = [open(fname) for fname in fnames]
#     all_words = []

#     for file in files:
#         for line in file:
#             line = line.rstrip()
#             words = line.split(" ")
#             words = [word.strip("'\",.!/?-#$%^&();:_").lower() for word in words]
#             all_words += words

#     return Counter(all_words)


# def word_count(fnames):
#     counter = {}

#     for fname in fnames:
#         file = open(fname)

#         for line in file:
#             line = line.rstrip()
#             words = line.split(" ")

#             for word in words:
#                 counter[word] = counter.get(word, 0) + 1

#     return counter


def display_word_count(counter):

    for word, count in counter.items():
        print (word, count)
        # print (f"{word} {count}")


print(display_word_count(word_count(sys.argv[1:])))

