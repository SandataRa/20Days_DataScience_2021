#Day 16
import openpyxl

from openpyxl.formatting.rule import ColorScaleRule
color_scale_rule = ColorScaleRule(start_type = "min",
                                 start_color = colors.COLOR_INDEX[5],
                                 end_type = "max",
                                 end_color = colors.COLOR_INDEX[6])

work_book = openpyxl.load_workbook('AirLineBumps_16_17.xlsx')
sheet = work_book.active

for row in sheet['B2:C13']:
    for cell in row: 
        cell.number_format = numbers.FORMAT_NUMBER_COMMA_SEPARATED1

sheet.conditional_formatting.add("B2:B13", color_scale_rule)
work_book.save('AirLineBumps_16_17_formatted.xlsx')

from openpyxl.formatting.rule import IconSetRule
icon_set_rule = IconSetRule(icon_style = "4Arrows",
                           type = "num",
                           values = [1,2,3,4])
sheet.conditional_formatting.add("F2:F13", icon_set_rule)

from openpyxl.formatting.rule import DataBarRule

data_bar_rule = DataBarRule(start_type = "num",
                           start_value = 1,
                           end_type = "num",
                           end_value = 4,
                           color = colors.COLOR_INDEX[3])

sheet.conditional_formatting.add("F2:F13", data_bar_rule)

work_book.save('AirLineBumps_16_17_formatted.xlsx')

# Working with images
from openpyxl import Workbook
from openpyxl.drawing.image import Image

work_book = Workbook()
work_sheet = work_book.active
img = Image("Hannya.png")
work_sheet.add_image(img, 'C11')
work_book.save('workbook_image.xlsx')
small_img = Image("Hannya.png")
small_img.width = 225
small_img.height = 225
work_sheet.add_image(small_img, 'L11')
work_book.save('workbook_image.xlsx')
