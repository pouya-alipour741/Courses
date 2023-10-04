import memory_profiler
import random
import time
names = ['John', 'Corey', 'Adam', 'Steve', 'Rick', 'Thomas']
majors = ['Math', 'Engineering', 'CompSci', 'Arts', 'Business']

print(f'Memory (Before): {memory_profiler.memory_usage()}Mb')

def people_list(num_people):
    result = []
    for i in range(num_people):
        person = {
            'id': i,
            'name': random.choice(names),
            'major': random.choice(majors),
        }
        result.append(person)
    return result

def people_generator(num_people):
    for i in range(num_people):
        person = {
            'id': i,
            'name': random.choice(names),
            'major': random.choice(majors),
        }
        yield person


t1 = time.perf_counter()  #or time.process_time()
people = people_list(1000)
t2 = time.perf_counter()

# t1 = time.perf_counter()
# people = people_generator(1000)
# t2 = time.perf_counter()

print(f'took {t2 - t1} seconds')
print(f'memory(after): {memory_profiler.memory_usage()}Mb')
