import settings, requests, os, csv, statistics, datetime, sys

from utilities import create_path_if_not_exists
from dateutil import parser

def download_data(start_date, end_date, delta, sensor_id):
    sd = start_date
    filenames = list()

    while sd <= end_date:
        date_part = sd.strftime("%Y-%m-%d")
        url = settings.url_pattern.format(date_part = date_part, sensor_id = sensor_id)
        
        r = requests.get(url, allow_redirects = True)
        filename = os.path.join(settings.csv_folder, settings.filename_pattern.format(date_part = date_part))
        create_path_if_not_exists(settings.csv_folder)
        open(filename, 'wb').write(r.content)

        filenames.append(filename)

        sd += delta

    return filenames

def process(filenames, start_date, ):
    pm25_values = list()
    day_medians = list()
    dates = list()

    window_start = start_date
    window_size = datetime.timedelta(hours = 1)
    window_values = list()
    median_values = list()

    min_value = sys.maxsize
    min_date = None
    max_value = -1
    max_date = None

    for fname in filenames:
        with open(fname, newline = "") as csvfile:
            reader = csv.reader(csvfile, delimiter=';')
            _ = next(reader, None)

            for row in reader:
                try:
                    pm25 = float(row[settings.PM25_INDEX])

                    pm25_values.append(pm25)

                    current_date = parser.parse(row[0])

                    # Update min
                    if pm25 < min_value:
                        min_value = pm25
                        min_date = current_date

                    # Update max
                    if pm25 > max_value:
                        max_value = pm25
                        max_date = current_date

                    if current_date > window_start + window_size:
                        window_median = statistics.median(window_values)
                        median_values.append(window_median)

                        window_values.clear()

                    window_values.append(pm25)

                    dates.append(current_date)
                except Exception as ex:
                    print(ex)

            day_median = statistics.median(pm25_values)
            day_medians.append(day_median)
            
            pm25_values.clear()
    
    return (day_medians, min_date, min_value, max_date, max_value)
