import pandas as pd
import numpy as np
import os
import glob


def get_several_data_as_csv(file_path):
    path = file_path + '/*.csv'
    files = glob.glob(path)
    data = [pd.read_csv(item, header=None) for item in files]
    data_set = []
    for index, item in enumerate(data):
        x_list = item[0].values
        y_list = item[1].values
        data_set_dammy = []
        for x, y in zip(x_list, y_list):
            data_set_dammy.append([x,y])
        data_set.append(data_set_dammy)

    return data_set, len(data_set)



def get_data(data_sheet_name):
    data = pd.read_csv(data_sheet_name + '.csv',header=None)
    print('data')
    print(data)
    x = data[0].values
    y = data[1].values
    points = [[x_item, y_item] for x_item, y_item in zip(x, y)]

    return x, y, points


if __name__ == '__main__':
    file_path = input('Please input path.')
    path = file_path + '/*.csv'
    get_several_data_as_csv(path)

    #data_sheet_name = input('Please input data sheet name')
    #x_data, y_data, data = get_data(data_sheet_name)
    #print(x_data, y_data, data)








