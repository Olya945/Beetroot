sentence = input("Enter a sentence: ")
our_dict = {}

words = sentence.split()

for word in words:
    our_dict.setdefault(word, 0)
    our_dict[word] += 1

print(our_dict)


# Alternative solution

sentence = input("Enter a sentence: ")
our_dict = {}

words = sentence.split()

for word in words:
    if word in our_dict:
        our_dict[word] += 1
    else:
        our_dict[word] = 1

print(our_dict)