from monotone_chain import get_convex_hull
from collect_data import get_data
from plot_function import scatter_plot
from plot_function import contours_plot
from plot_function import show_image
import matplotlib.pyplot as plt

if __name__ == '__main__':
    data_sheet_name = input('Please input data sheet name')
    x, y, data = get_data(data_sheet_name)
    contours = get_convex_hull(data)
    print(contours)
    
    scatter_plot(x,y,'raw_data')
    contours_plot(contours, 'contours_plot')
    show_image()

