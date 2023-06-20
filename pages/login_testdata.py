from utilities import xl_utils

rows = xl_utils.getRowCount('login')


def loginData():
    result = []
    for r in range(2, rows + 1):
        username = xl_utils.readData('login', r, 1)
        password = xl_utils.readData('login', r, 2)
    return result
