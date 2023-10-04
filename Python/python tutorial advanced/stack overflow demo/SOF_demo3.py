import csv
from  collections import Counter

with open('data/survey_results_public.csv') as f:
    csv_reader = csv.DictReader(f)

    dev_type_info = {}

    for line in csv_reader:
        dev_types = line['DevType'].split(';')

        for dev_type in dev_types:
            dev_type_info.setdefault(dev_type,{
                'total' : 0,
                'language_counter' : Counter()
            })

        languages = line['LanguageWorkedWith'].split(';')
        dev_type_info[dev_type]['total'] += 1
        dev_type_info[dev_type]['language_counter'].update(languages)

    for dev , info in dev_type_info.items():
        if dev == 'NA':
            continue
        print(dev)
        for lang,value in info['language_counter'].most_common(5):
            lang_pct = (value/info['total']) * 100
            lang_pct = round(lang_pct,2)

            print(f'\t{lang}:{lang_pct}%')