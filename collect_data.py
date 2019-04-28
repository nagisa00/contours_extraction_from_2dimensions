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



def get_several_data_as_excel(file_name):
    path = 'data/' + file_name + '.xlsx'
    df_list = []
    file = pd.ExcelFile(path, header=None)  # bookを読む
    for sheet in file.sheet_names:
        df_list.append(file.parse(sheet))

    data_set = []
    for item in df_list:
        data_set_dammy = []
        for list_data in item.values:
            data_set_dammy.append(list(list_data))
        data_set.append(data_set_dammy)
    return data_set



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
    data, num = get_several_data_as_csv(file_path)
    #path = 'data/' + file_path + '.xlsx'
    #data = get_several_data_as_excel(path)









