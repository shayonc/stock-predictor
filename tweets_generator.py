import os, sys
import subprocess
from datetime import datetime, timedelta
import csv

if __name__ == '__main__':
    later_date = datetime.today()
    past_date = datetime.today() - timedelta(days=365)

    fd = open('appended_output.csv','w')
    fd.write("")
    fd.close()

    for i in range(0, 365):
        later_date_string = later_date.strftime("%Y-%m-%d")
        past_date_string = past_date.strftime("%Y-%m-%d")

        print later_date_string
        print past_date_string

        #subprocess.Popen(["python", "Exporter.py", "--querysearch", '"tesla"', "--since", past_date_string, "--until", later_date_string, "--maxtweets", "10"])
        os.system('python Exporter.py --querysearch "tesla"  --since ' + past_date_string + ' --until ' + later_date_string + ' --maxtweets 100')

        reader = csv.reader(open('output_got.csv', 'r'))
        writer = csv.writer(open('appended_output.csv', 'a'), delimiter=',')
        for row in reader:
            if not row[0].startswith('user'):
                writer.writerow(row)
        
        past_date = past_date - timedelta(days=1)
        later_date = later_date - timedelta(days=1)
        
