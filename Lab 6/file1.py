try:
    with open('data.txt') as f ,open('upper.txt','w') as f1:
        lines = f.readlines()
        for line in lines:
            f1.writelines(line.upper())
            
except Exception as e:
    print(f'File not found please check path {e}')
