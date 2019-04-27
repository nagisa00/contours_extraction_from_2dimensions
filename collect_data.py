import pandas as pd
import numpy as np

def get_data(data_sheet_name):
    data = pd.read_csv(data_sheet_name + '.csv', header=None)
    x = data[0].values
    y = data[1].values
    points = [[x_item, y_item] for x_item, y_item in zip(x, y)]

    return x, y, points

if __name__ == '__main__':
    data_sheet_name = input('Please input data sheet name')
    x_data, y_data, data = get_data(data_sheet_name)
    print(x_data, y_data, data)








