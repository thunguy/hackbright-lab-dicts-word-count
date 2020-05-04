import sys

def word_count(filename):

    file = open(sys.argv[1])

    counter = {}

    for line in file:
        line = line.rstrip()
        words = line.split(" ")

        for word in words:
            counter[word] = counter.get(word, 0) + 1

    return counter

def display_word_count(counter):

    for word, count in counter.items():
        # print (word, count)
        print (f"{word}: {count}")

# print(word_count(sys.argv))
print(display_word_count(word_count(sys.argv)))

