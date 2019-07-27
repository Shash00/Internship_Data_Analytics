s = input("Enter a string: ")
split_s = list(s)
vowels = ['a', 'e', 'i', 'o', 'u']
vowels_in_s = list(filter(lambda x : x in vowels, split_s))

print(f"\n{vowels_in_s} ; {len(vowels_in_s)}")