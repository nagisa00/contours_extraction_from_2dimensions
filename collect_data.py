import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def det(p, q):
    return p[0]*q[1] - p[1]*q[0]


def sub(p, q):
    return (p[0]-q[0], p[1]-q[1])


def get_convex_hull(points):
    # どの3点も直線上に並んでいないと仮定する。
    n = len(points)
    points.sort()
    size_convex_hull = 0
    ch = []
    for i in range(n):
        while size_convex_hull > 1:
            v_cur = sub(ch[-1], ch[-2])
            v_new = sub(points[i], ch[-2])
            if det(v_cur, v_new) > 0:
                break
            size_convex_hull -= 1
            ch.pop()
        ch.append(points[i])
        size_convex_hull += 1

    t = size_convex_hull
    for i in range(n-2, -1, -1):
        while size_convex_hull > t:
            v_cur = sub(ch[-1], ch[-2])
            v_new = sub(points[i], ch[-2])
            if det(v_cur, v_new) > 0:
                break
            size_convex_hull -= 1
            ch.pop()
        ch.append(points[i])
        size_convex_hull += 1

    return ch[:-1]




if __name__ == '__main__':
    data_sheet_name = input('Please input data sheet name')
    data = pd.read_csv(data_sheet_name + '.csv', header=None)
    x = data[0].values
    y = data[1].values
    print(x)
    print(y)
    print(x[0], y[0])
    points = [[x_item, y_item] for x_item, y_item in zip(x, y)]
    contours = get_convex_hull(points)
    print(contours)
    plot_x = [row[0] for row in contours]
    plot_y = [row[1] for row in contours]

    plt.scatter(x, y, label='raw_data')
    plt.plot(plot_x, plot_y, label='contours')
    plt.show()








