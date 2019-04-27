from monotone_chain import get_convex_hull
from collect_data import get_data
from collect_data import get_several_data_as_csv
from plot_function import setting_axis
from plot_function import scatter_plot
from plot_function import contours_plot
from plot_function import show_image

if __name__ == '__main__':
    file_path = input("Please input path to files")
    path = file_path + '/*.csv'
    data_set, data_set_num = get_several_data_as_csv(path)
    #x, y, data = get_data(data_sheet_name)
    contours = [get_convex_hull(data) for data in data_set]
    #print(contours)
    #setting_axis(left_x, rigth_x, up_y, down_y)
    #scatter_plot(x,y,'raw_data')
    contours_plot(contours[0], 'contours_plot', 'red', 3.0)
    contours_plot(contours[1], 'contours_plot2', 'blue', 3.0)
    show_image()

