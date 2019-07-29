class MaxError(Exception):

    def __init__(self,message):
        self.message = message

    def __str__(self):
        return f"{self.__class__.__name__} : {self.message}"

c = 0
def user(username, password):
    global c

    if username == 'abc' and password == 123:
        print('Login successfull')
    
    else:
        print('Wrong credentials please try again')
    c += 1

    if c >2:
        raise MaxError('Max amount of transactions')

user(123,'abc')
user(12,'ab')
user(231,'fab')
user('fbg',123)
user('sfsa',123)