import csv
import os
os.chdir(r'C:\Users\pouya\Desktop\python\csv')

with open('ds_salaries.csv','r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    with open('ds_salaries_copy.csv','w') as copy_csv:
        field_names = ['work_year', 'experience_level', 'job_title', 'salary_in_usd',
                       ]
        csv_writer = csv.DictWriter(copy_csv,fieldnames=field_names,delimiter='\t')

        csv_writer.writeheader()
        for line in csv_reader:
            print(line)
            line = {'work_year': line['work_year'],
                    'experience_level': line['experience_level'],
                    'salary_in_usd': line['salary_in_usd'],
                    'job_title':line['job_title'],
                    }
            csv_writer.writerow(line)

