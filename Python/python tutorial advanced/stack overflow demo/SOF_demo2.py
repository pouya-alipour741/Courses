import csv
from collections import Counter


with open('data/survey_results_public.csv') as f:
    csv_reader = csv.DictReader(f)
    total = 0

    language_counter = Counter()
    for line in csv_reader:
        languages = line['LanguageWorkedWith'].split(';')

        language_counter.update(languages)

        # for language in languages:   ##work exactly as language_counter.update(languages)
        #     language_counter[language] += 1
        if line['LanguageWorkedWith'] == 'NA':  ##for clearing data from NA replies
            continue
        total += 1

# print(language_counter)
# print(total)

for language,value in language_counter.most_common(10):
    lang_pct = round((value/total*100),2)
    print(f'{language}:{lang_pct}')



