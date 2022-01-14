from datetime import timedelta
import datetime

base = datetime.datetime.today()
date_list = [base - datetime.timedelta(days=x) for x in range(100)]

for i in range(91):
    date = date_list[i].strftime('%m-%d')

    main_log = open("logs/graylog-search-result-relative-604800.csv", "r")
    current_file = open("logs/graylog-search-result-relative-" + date + ".csv", "w+")

    while True:
        
        line = main_log.readline()
        if not line:
            break

        # line.replace('2021-09-28', '2021-' + date)
        current_file.write(line.replace('2021-09-28', '2021-' + date))


    current_file.close
    main_log.close


