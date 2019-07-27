import string

def get_keys_by_value(dictionary, val):
    key_list = list()
    for k, v in dictionary.items():
        if v == val:
            key_list.append(k)
    return key_list


s = input("Enter a paragraph:\n>> ")
s = s.translate(str.maketrans('', '', string.punctuation))
s = s.lower() 
words = s.split()
word_counts = dict()
for word in words : 
    word_counts[word] = word_counts.get(word, 0) + 1

counts = word_counts.values()
max_count = max(counts)
min_count = min(counts)
max_count_words = get_keys_by_value(word_counts, max_count)
min_count_words = get_keys_by_value(word_counts, min_count)
print(f"Word(s) appearing maximum times {max_count_words} ; {max_count} times ")
print(f"Word(s) appearing minimum times {min_count_words} ; {min_count} times ")


