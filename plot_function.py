import matplotlib.pyplot as plt

dict_color = {0:'red', 1:'blue', 2:'green', 3:'yellow', 4:'pink'}

def setting_axis(x_label, y_label, axis_area, grid_on):
    # 軸の設定
    plt.figure()
    if type(axis_area) is not str:
        plt.axis([axis_area[0], axis_area[1], axis_area[2], axis_area[3]])
        #left right up down
    if grid_on == True:
        plt.grid()
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    #ax = plt.subplot()
    #ax.grid(which="both")


def scatter_plot(x,y,label_name):
    plt.scatter(x,y,label=label_name)
    print('scatter_plot')


def contours_plot(contours, label_name, color_code, line_width):
    x_plot = [raw[0] for raw in contours]
    y_plot = [raw[1] for raw in contours]
    x_first_last = [x_plot[0], x_plot[-1]]
    y_first_last = [y_plot[0], y_plot[-1]]
    color_name = dict_color[color_code]
    plt.plot(x_plot,y_plot, label=label_name, color=color_name, linewidth=line_width)
    plt.plot(x_first_last, y_first_last, label=label_name, color = color_name, linewidth=line_width)

    print('contours_plot')

def show_image():
    plt.show()


def save_image():
    plt.savefig("graph.jpg")


def change_setting():
    print('change_setting')