class Stack:
    def __init__(self):
        self.st = []

    def push(self):
        inp = input('Enter the element to push: ')
        self.st.append(inp)

    def pop(self):
        if self.is_empty():
            print('Stack is empty')
        else:
            ele = self.st.pop()
            print(f"The deleted element is: {ele}")
        
    def search(self):
        if self.is_empty():
            print('Stack is empty')
        else:
            key = input('Enter key element to search: ')
            for index,ele in enumerate(self.st):
                if ele == key:
                    print(f'The element {key} is in {index}')

    def display(self):
        if self.is_empty():
            print('Stack is empty')
        else:
            for i in self.st:
                print(i)
    
    def is_empty(self):
        if len(self.st) == 0:
            return True
        return False


    
if __name__ == "__main__":
    st = Stack()
    while True:
        options = {1:st.push, 2:st.pop, 3:st.display, 4:st.search, 5:exit}
        print('1.Push 2.Pop 3.Display 4.Search 5.Exit')
        try:
            ch = int(input('Enter your choice: '))
            options[ch]()

        except(KeyError, ValueError):
            print('Enter options from 1-5 only')