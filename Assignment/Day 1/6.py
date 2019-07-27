'''
6.	Write a program to accept a number from the user; then display the reverse of the entered number.
'''
def reverse_num(num):
    '''
    Reverses a number and returns it.
    '''
    rev = 0
    while num != 0:
        rev = rev * 10 + num % 10
        num = num // 10
    return rev

num = int(input("Enter a number: "))
rev = reverse_num(num)
print(f"Reverse of {num} is {rev}")
