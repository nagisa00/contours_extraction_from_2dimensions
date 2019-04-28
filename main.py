from monotone_chain import get_convex_hull
from collect_data import get_several_data_as_csv
from plot_function import setting_axis
from plot_function import scatter_plot
from plot_function import contours_plot
from plot_function import show_image
from plot_function import save_image

grid_on = True
#グリッド線を入れるかどうか
axis_width = 'default'
#グラフの範囲を指定するかしないか　指定する場合は[left, right, up, down]の順に範囲を設定
x_label = 'x_axis'
y_label = 'y_axis'
#軸ラベルの設定
graph_width = 3.0
#線の太さ


if __name__ == '__main__':
    file_path = input("Please input path to files")
    data_set, data_set_num = get_several_data_as_csv(file_path)
    contours = [get_convex_hull(data) for data in data_set]
    setting_axis(x_label, y_label, axis_width, grid_on)
    for index, item in enumerate(contours):
        contours_plot(contours[index], 'contours_plot'+ str(index), index, graph_width)
    #show_image()
    save_image()

