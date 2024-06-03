import string

words_count = dict()
with open("text.txt", "r") as text_file:
    for line in text_file:
        # strip lines, lower text, remove punctuation, then split into words
        words = line.strip().lower().translate(line.maketrans("", "", string.punctuation)).split(" ")
        for word in words:
            if word in words_count:
                words_count[word] += 1
            else:
                words_count[word] = 1

for word in list(words_count.keys()):
    print(f"{word}: {words_count[word]}")
