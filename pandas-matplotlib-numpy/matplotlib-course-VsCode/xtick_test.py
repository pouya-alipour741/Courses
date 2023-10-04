from contextlib import contextmanager
import os
import pandas as pd
from collections import Counter,defaultdict
import matplotlib.pyplot as plt

@contextmanager
def change_dir(directory):
    try:
        cwd = os.getcwd()
        os.chdir(directory)
        yield

    finally:
        os.chdir(cwd)


my_dir = r'C:\Users\pouya\vsCodeProjects\matplotlib-course\02-CoreySchafer'

plt.style.use("fivethirtyeight")

with change_dir(my_dir):
    data = pd.read_csv("data.csv")


ids = data["Responder_id"]
language_responses = data["LanguagesWorkedWith"]

####1
# lang_counter = Counter()
# for response in language_responses:
#     lang_counter.update(response.split(";"))


###2 same as 1 but with defaultdict
lang_counter = defaultdict(int)
for response in language_responses:
    split_langs = response.split(";")
    for lang in split_langs:
        lang_counter[lang] += 1

# # print(lang_counter)


languages = [i for i in lang_counter.keys()]
popularity = [i for i in lang_counter.values()]

plt.barh(languages,popularity)
plt.title("Most Popular Languages")
# plt.ylabel("Programming Languages")
plt.xlabel("Number of People Who Use")
plt.yticks(ticks=languages,labels=range(len(languages)))
plt.ylim(0,len(popularity))
plt.tight_layout()

plt.show()




