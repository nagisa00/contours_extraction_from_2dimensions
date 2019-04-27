import matplotlib.pyplot as plt

def scatter_plot(x,y,label_name):
    plt.scatter(x,y,label=label_name)
    print('scatter_plot')


def contours_plot(contours, label_name, color_name, line_width):
    x_plot = [raw[0] for raw in contours]
    y_plot = [raw[1] for raw in contours]
    x_first_last = [x_plot[0], x_plot[-1]]
    y_first_last = [y_plot[0], y_plot[-1]]

    plt.plot(x_plot,y_plot, label=label_name, color=color_name, linewidth=line_width)
    plt.plot(x_first_last, y_first_last, label=label_name, color = color_name, linewidth=line_width)

    print('contours_plot')

def show_image():
    plt.show()


def change_setting():
    print('change_setting')