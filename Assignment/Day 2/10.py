import string

s = input("Enter a paragraph:\n>> ")
s = s.translate(str.maketrans('', '', string.punctuation))
s = s.lower() 
words = s.split()
word_counts = dict()
for word in words : 
    word_counts[word] = word_counts.get(word, 0) + 1

print(f"Number of unique words : {len(word_counts.keys())}")
for word, count in word_counts.items():
    print(f"{word} : {count} times")
    
