import os, datetime
import matplotlib.pyplot as plt

from dateutil import parser

import settings, engine
from utilities import *

# xkcd style
plt.xkcd()

# Read settings
start_date = parser.parse(settings.start_date)
end_date = parser.parse(settings.end_date)
delta = datetime.timedelta(days = settings.delta_in_days)

for sensor in settings.all_sensors:
    # Download CSVs
    filenames = engine.download_data(start_date, end_date, delta, sensor.id)

    # Proces downloaded data
    (day_medians, min_date, min_pm25, max_date, max_pm25) = engine.process(filenames, start_date)

    # Chart settings
    colors = [value_to_color(i) for i in day_medians]
    x_axis = settings.days
    x_pos = [i for i, _ in enumerate(x_axis)]

    # Create chart
    fig, ax = plt.subplots()
    rects = ax.bar(x_axis, day_medians, color = colors)

    # Y axis
    plt.ylabel(settings.pm25_y_label)

    # Create image title
    start_date_pretty = start_date.strftime("%d.%m.%Y")
    end_date_pretty = end_date.strftime("%d.%m.%Y")
    chart_title = settings.chart_title_format.format(sensor_name = sensor.name, start_date = start_date_pretty, end_date = end_date_pretty)
    plt.title(chart_title)

    # X axis
    plt.xticks(x_pos, x_axis)

    # Add bar labels (data points)
    autolabel(rects, ax)

    # Save image
    create_path_if_not_exists(settings.output_folder)
    image_path = os.path.join(settings.output_folder, ".".join([sensor.name, settings.output_image_format]))
    plt.savefig(image_path)

    # Save txt data
    txt_path = os.path.join(settings.output_folder, ".".join([sensor.name, settings.output_txt_format]))
    data_per_day_formatted = format_data_per_day(settings.days, day_medians)
    min_max_formatted = format_min_max(min_date, min_pm25, max_date, max_pm25)
    stream = open(txt_path, 'w')
    stream.write(data_per_day_formatted)
    stream.write("\n")
    stream.write(min_max_formatted)
