products = dict()

def add():
    while True:
        inp = input('Key and Value:')
        if inp == 'exit':
            break
        else:
            key,val = inp.split(' ')
            products[key] = val

def search(key):
    if bool(products):
        print()
    else:
        print('Products empty')

    
def display(products):
    for k,v in products.items():
        print(f"{k}:{v}")

add()
display(products)
search(1)
    

    
        