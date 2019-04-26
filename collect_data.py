import pandas as pd

if __name__ == '__main__':
    data_sheet_name = input('Please input data sheet name')
    data = pd.read_csv(data_sheet_name, header=None)


