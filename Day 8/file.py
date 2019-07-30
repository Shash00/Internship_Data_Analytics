lst = [[1001,'abc','mite',2019],[1002,'asf','mite',2019],[1003,'fsa','mite',2019],[1004,'aasg','mite',2019]]
try:
    with open('data.txt','w') as f:
        for d in lst:
            line = f'{d[0]},{d[1]},d{2},d{3},d{4}\n'
            f.write(line)

except Exception as e:
    print(f'{e}')