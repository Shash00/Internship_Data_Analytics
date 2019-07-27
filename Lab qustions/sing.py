while True:
    inp = input('Question:')
    if inp == 'exit':
        break
    else:
        rep = inp[-1]
        res = inp.replace(rep,'ies')
    
    print(res)