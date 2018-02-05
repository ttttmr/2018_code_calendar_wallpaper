import datetime
import os

from wand.image import Image

BASE = os.getcwd()  # now path
PDF_SOURCE = BASE + '/2018_code_calendar.pdf[{}]'  # PDF path
BACKGROUND_SOURCE = BASE + '/wallpaper.jpg'  # wallpaper
OUTPUT = BASE + '/2018_code_calendar_wallpaper.jpg'  # new wallpaper

PAGE_OFFSET = 6  # PDF start page
MARGIN_LEFT = 200
MARGIN_TOP = 180

current_week = datetime.datetime.now().isocalendar()[1]
page = PAGE_OFFSET + current_week

with Image(filename=PDF_SOURCE.format(page), resolution=200) as calendar:
    with Image(filename=BACKGROUND_SOURCE) as background:
        background.composite_channel(
            'default_channels', calendar, 'blend', MARGIN_LEFT, MARGIN_TOP)
        background.save(filename=OUTPUT)
