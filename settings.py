from sensor import sensor

### NEED TO BE CHANGED REGULARLY ###
start_date = "2021-02-01"
end_date = "2021-02-07"

### LESS LIKELY TO CHANGE ###
pm25_y_label = "PM 2.5 (medijana)"
chart_title_format = "{sensor_name} za nedelju od {start_date} do {end_date}"

all_sensors = [
    sensor(name = "Devet Jugovica", id = "esp8266-8000692"),
    sensor(name = "Starine Novaka", id = "esp8266-8023432")]

delta_in_days = 1
days = ["PON", "UTO", "SRE", "CET", "PET", "SUB", "NED"]

output_folder = "out"

output_image_format = "png"
output_txt_format = "txt"

PM10_INDEX = 7
PM25_INDEX = 8

url_pattern = "https://api-rrd.madavi.de/data_csv/csv-files/{date_part}/data-{sensor_id}-{date_part}.csv"
filename_pattern = "data-{date_part}.csv"

csv_folder = "data"

# Ranges: boundaries and colors
boundary_green = 10
color_green = "green"
boundary_yellow = 20
color_yellow = "yellow"
boundary_orange = 25
color_orange = "orange"
boundary_red = 50
color_red = "red"
boundary_purple = 75
color_purple = "purple"
color_deep_red = "#7e0023"
