import csv

with open('daily_weather.tsv', 'rb') as tsvin:
    with open('daily_weather_fix.tsv', 'wb') as tsvout:

        tsvin = csv.reader(tsvin, delimiter='\t')
        tsvout = csv.writer(tsvout, delimiter='\t')

        # write out the header row first
        tsvout.writerow(tsvin.next())

        for row in tsvin:
            if row[2] == '1':
                row[3] = 'Winter'
            elif row[2] == '2':
                row[3] = 'Spring'
            elif row[2] == '3':
                row[3] = 'Summer'
            elif row[2] == '4':
                row[3] = 'Fall'
            else:
                continue

            tsvout.writerow(row)