from monotone_chain import get_convex_hull
from collect_data import get_data

if __name__ == '__main__':
    data_sheet_name = input('Please input data sheet name')
    x, y, data = get_data(data_sheet_name)
    contours = get_convex_hull(data)
    print(contours)

