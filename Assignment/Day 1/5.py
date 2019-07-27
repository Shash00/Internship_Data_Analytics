'''
5.	Write a program to print the Fibonacci series up to the number 34.
'''

term_1 = 0
term_2 = 1
term_3 = 0
print(term_1, end=" ")
print(term_2, end=" ")
while term_3 != 34:
    term_3 = term_1 + term_2
    term_1 = term_2
    term_2 = term_3
    print(term_3, end=" ")
print()

    
