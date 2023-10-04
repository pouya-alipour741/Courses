
#1
# print(f'first module name is {__name__}')

#2

def func():
    print(f'run directly from {__name__}')

if __name__ == "__main__":
    func()
else:
    print('run from import')

