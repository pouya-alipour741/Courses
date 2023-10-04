import logging

# set this seperately unlike basic config
logger = logging.getLogger(__name__)   ###you can hardcode any name but by convention we use __name__
logger.setLevel(logging.Info)

formatter = logging.Formatter('%(levelname)s:%(name)s:%(message)s')
filehandler = logging.FileHandler('employee.log')
filehandler.setFormatter(formatter)

logger.addHandler(filehandler)

# logging.basicConfig(filename='employee.log', level=logging.INFO,   #we dont need this anymore
#                     format='%(levelname)s:%(name)s:%(message)s')

class Employee:
    """A sample Employee class"""

    def __init__(self, first, last):
        self.first = first
        self.last = last

        logger.info('Created Employee: {} - {}'.format(self.fullname, self.email))

    @property
    def email(self):
        return '{}.{}@email.com'.format(self.first, self.last)

    @property
    def fullname(self):
        return '{} {}'.format(self.first, self.last)


emp_1 = Employee('John', 'Smith')
emp_2 = Employee('Corey', 'Schafer')
emp_3 = Employee('Jane', 'Doe')
