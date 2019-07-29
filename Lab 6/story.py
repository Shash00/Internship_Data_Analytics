try:
    with open('data.txt') as f:
        con = ['but','how','if','and']
        word = 0
        d = {}
        lines = f.readlines()
        for line in lines:
            for li in line.split(" "):
                word += len(li)
                if li not in d:
                    d[li] = 1
                else:
                    d[li] += 1
        print(d)
        max = max(d.values())
        for k,v in d.items():
            if d[k] == max:
                print(k)
        print(f"Max: {max}")
        for i in d.keys():
            if i in con:
                print(f">{i}:{d[i]}")

except Exception as e:
    print({e})