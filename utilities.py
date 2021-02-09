import os, errno
import settings

def value_to_color(value):
    if value < settings.boundary_green:
        return settings.color_green
    elif value < settings.boundary_yellow:
        return settings.color_yellow
    elif value < settings.boundary_orange:
        return settings.color_orange
    elif value < settings.boundary_red:
        return settings.color_red
    elif value < settings.boundary_purple:
        return settings.color_purple
    else:
        return settings.color_deep_red

def autolabel(rects, ax, xpos = "center"):
    xpos = xpos.lower() 
    ha = {"center": "center", "right": "left", "left": "right"}
    offset = {"center": 0.5, "right": 0.57, "left": 0.43} 

    for rect in rects:
        height = round(rect.get_height())
        ax.text(rect.get_x() + rect.get_width()*offset[xpos], 1.01*height,
                "{}".format(height), ha=ha[xpos], va="bottom")

def create_path_if_not_exists(path):
    try:
        os.makedirs(path)
    except OSError as e:
        if e.errno != errno.EEXIST:
            raise

def format_data_per_day(days, data):
    output = ""
    for i in range(0, len(days)):
        row = "{}: {}".format(days[i], data[i]) + "\n"
        output += row

    return output

def format_min_max(min_date, min_val, max_date, max_val):
    output = ""

    min_date_pretty = min_date.strftime("%d.%m.%Y %H:%M")
    max_date_pretty = max_date.strftime("%d.%m.%Y %H:%M")
    
    output += "MIN: {} ({})".format(round(min_val), min_date_pretty) + "\n"
    output += "MAX: {} ({})".format(round(max_val), max_date_pretty) + "\n"

    return output
