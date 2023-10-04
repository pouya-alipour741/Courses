# try:
#     f = open(r'C:\Users\pouya\Desktop\python\csv\ds_salaries.csv')
#     # f = open(r'C:\Users\pouya\Desktop\python\csv\unpopular_songs.csv')
#     if f.name == r'C:\Users\pouya\Desktop\python\csv\unpopular_songs.csv':
#         raise Exception
#     # var = bad_var
# except FileNotFoundError:
#     print('sorry,file not found')
# except Exception:
#     print('sorry,something went wrong')
# else:
#     read_lines = f.readlines()
#     print(read_lines)
#     # print(f.read(300))
#     f.close()
# finally:
#     print('execute finally...')
#



##define our own exception

class ValueTooHighError(Exception):
    pass

class ValueTooLowError(Exception):
    def __init__(self,message, value):
        self.message = message
        self.value = value

def test_value(x):
    if x > 100:
        raise ValueTooHighError("value is high")
    if x < 5:
        raise ValueTooLowError("value is low", x)

try:
    test_value(1)
except ValueTooHighError as e:
    print(e)
except ValueTooLowError as e:
    print(e.message, e.value)
