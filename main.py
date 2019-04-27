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
    contours = [get_convex_hull(data) for data in data_set]
    for index, item in enumerate(contours):
        contours_plot(contours[index], 'contours_plot'+ str(index), index, 3.0)
    show_image()

