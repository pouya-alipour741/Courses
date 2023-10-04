import csv
import os
os.chdir(r'C:\Users\pouya\Desktop\python\csv')

with open('ds_salaries.csv','r') as csv_file:
    csv_reader = csv.DictReader(csv_file)  #can use csv.Reader but can't use fieldnames=
    # next(csv_reader) #skip first line
    with open('ds_salaries_copy.csv','w') as copy_csv:
        field_names = ['work_year', 'experience_level', 'employment_type', 'job_title', 'salary', 'salary_currency', 'salary_in_usd',
                       'employee_residence', 'remote_ratio', 'company_location', 'company_size']
        csv_writer = csv.DictWriter(copy_csv,fieldnames=field_names,delimiter='\t')

        csv_writer.writeheader()
        for line in csv_reader:
            del line['']
            csv_writer.writerow(line)




