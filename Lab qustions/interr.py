li = []
qus = ['do', 'does', 'is', 'are']

while True:
    inp = input('Question:')
    if inp == 'exit':
        break
    else:
        if inp.endswith('?'):
            print('Interrogative question')
        else:
            print('Assertive')


