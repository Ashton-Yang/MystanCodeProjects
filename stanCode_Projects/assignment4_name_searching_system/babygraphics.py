
# input 為 Jennifer時無法順利畫出折線圖

"""
File: babygraphics.py
Name: Ashton Yang
--------------------------------
SC101 Baby Names Project
Adapted from Nick Parlante's Baby Names assignment by
Jerry Liao.
"""

import tkinter
import babynames
import babygraphicsgui as gui

FILENAMES = [
    'data/full/baby-1900.txt', 'data/full/baby-1910.txt',
    'data/full/baby-1920.txt', 'data/full/baby-1930.txt',
    'data/full/baby-1940.txt', 'data/full/baby-1950.txt',
    'data/full/baby-1960.txt', 'data/full/baby-1970.txt',
    'data/full/baby-1980.txt', 'data/full/baby-1990.txt',
    'data/full/baby-2000.txt', 'data/full/baby-2010.txt'
]
CANVAS_WIDTH = 1000
CANVAS_HEIGHT = 600
YEARS = [1900, 1910, 1920, 1930, 1940, 1950,
         1960, 1970, 1980, 1990, 2000, 2010]
GRAPH_MARGIN_SIZE = 20
COLORS = ['red', 'purple', 'green', 'blue']
TEXT_DX = 2
LINE_WIDTH = 2
MAX_RANK = 1000


def get_x_coordinate(width, year_index):
    """
    Given the width of the canvas and the index of the current year
    in the YEARS list, returns the x coordinate of the vertical
    line associated with that year.

    Input:
        width (int): The width of the canvas
        year_index (int): The index where the current year is in the YEARS list
    Returns:
        x_coordinate (int): The x coordinate of the vertical line associated
                            with the current year.
    """
    x_interval = (width - 2*GRAPH_MARGIN_SIZE) // len(YEARS)
    x_coordinate = GRAPH_MARGIN_SIZE + year_index * x_interval
    return x_coordinate


def draw_fixed_lines(canvas):
    """
    Draws the fixed background lines on the canvas.

    Input:
        canvas (Tkinter Canvas): The canvas on which we are drawing.
    """
    canvas.delete('all')            # delete all existing lines from the canvas

    # ----- Write your code below this line ----- #
    x1 = GRAPH_MARGIN_SIZE
    x2 = CANVAS_WIDTH - GRAPH_MARGIN_SIZE
    y1 = GRAPH_MARGIN_SIZE
    y2 = CANVAS_HEIGHT - GRAPH_MARGIN_SIZE
    canvas.create_line(x1, y1, x2, y1)
    canvas.create_line(x1, y2, x2, y2)
    for i in range(len(YEARS)):
        x = get_x_coordinate(CANVAS_WIDTH, i)
        top_y = 0
        bottom_y = CANVAS_HEIGHT
        canvas.create_line(x, top_y, x, bottom_y)
        # creates year label
        year = YEARS[i]
        txt_y = CANVAS_HEIGHT - GRAPH_MARGIN_SIZE
        canvas.create_text(x +TEXT_DX, txt_y, text = year, anchor= tkinter.NW)



def draw_names(canvas, name_data, lookup_names):
    """
    Given a dict of baby name data and a list of name, plots
    the historical trend of those names onto the canvas.

    Input:
        canvas (Tkinter Canvas): The canvas on which we are drawing.
        name_data (dict): Dictionary holding baby name data
        lookup_names (List[str]): A list of names whose data you want to plot

    Returns:
        This function does not return any value.
    """
    draw_fixed_lines(canvas)        # draw the fixed background grid

    # ----- Write your code below this line ----- #
    color_index = -1
    for lookup_name in lookup_names:                   # lookup_names = ['Kylie', 'Nicholas', 'Sonja']
        color_index += 1
        if lookup_name in name_data:                   # 'Kylie'  name_data = {'Kylie':{'1980': '567','1990': '179',...},...}
    # ---------- Create text for rank <= 1,000 -------------------- #
            year_rank = name_data[lookup_name]         # year_rank = {'1980':'567', '1990':'179', '2000':'104', '2010':'57'}
            year_rank_indexes = []                     # [8, 9, 10, 11]
            year_rank_index = 0
            all_coordinatrs = {}
            for key in year_rank:
                year_rank_index = (int(key) - YEARS[0]) // 10
                year_rank_indexes.append(year_rank_index)
                x = get_x_coordinate(CANVAS_WIDTH, year_rank_index) + TEXT_DX
                y = GRAPH_MARGIN_SIZE + int(year_rank[key]) * (CANVAS_HEIGHT - 2*GRAPH_MARGIN_SIZE)/1000
                all_coordinatrs[year_rank_index] = y
                rank = year_rank[key]
                text = ''
                text += lookup_name
                text += ' '
                text += rank
                canvas.create_text(x, y, text=text, anchor=tkinter.SW)
            print(all_coordinatrs)
    # ---------- Create text for rank > 1,000 -------------------- #
            # YEARS = [1900, 1910, 1920, 1930, 1940, 1950, 1960, 1970, 1980, 1990, 2000, 2010]
            indexes = []                               # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
            index = -1
            for year in YEARS:
                index += 1
                indexes.append(index)
            for token in indexes:
                non_data_indexes = []                     # [0, 1, 2, 3, 4, 5, 6, 7]
                if token not in year_rank_indexes:
                    x = get_x_coordinate(CANVAS_WIDTH, token) + TEXT_DX
                    y = CANVAS_HEIGHT - GRAPH_MARGIN_SIZE
                    non_data_indexes.append(token)
                    all_coordinatrs[token] = CANVAS_HEIGHT - GRAPH_MARGIN_SIZE
                    rank = '*'
                    text = ''
                    text += lookup_name
                    text += ' '
                    text +=rank
                    canvas.create_text(x, y, text= text, anchor = tkinter.SW)
            print(all_coordinatrs)
    # ---------- Create lines -------------------- #
            num = -1
            for i in range(len(all_coordinatrs)-1):
                num += 1
                x1 = get_x_coordinate(CANVAS_WIDTH, num)
                y1 = all_coordinatrs[num]
                x2 = get_x_coordinate(CANVAS_WIDTH, num + 1)
                y2 = all_coordinatrs[num + 1]
                canvas.create_line(x1, y1, x2, y2, fill = COLORS[color_index])


# main() code is provided, feel free to read through it but DO NOT MODIFY
def main():
    # Load data
    name_data = babynames.read_files(FILENAMES)

    # Create the window and the canvas
    top = tkinter.Tk()
    top.wm_title('Baby Names')
    canvas = gui.make_gui(top, CANVAS_WIDTH, CANVAS_HEIGHT, name_data, draw_names, babynames.search_names)

    # Call draw_fixed_lines() once at startup so we have the lines
    # even before the user types anything.
    draw_fixed_lines(canvas)

    # This line starts the graphical loop that is responsible for
    # processing user interactions and plotting data
    top.mainloop()


if __name__ == '__main__':
    main()
