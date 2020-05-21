import requests
import json
import algorithms


# Read response from API
def getResponse(size, level):
    url = "http://www.cs.utep.edu/cheon/ws/sudoku/new/?size=" + str(size)
    url = url + "&level=" + str(level)
    resp = requests.get(url)
    print(resp.status_code)
    if resp.status_code == 200:
        return (processData(json.loads(resp.text), size), True)
    else:
        return (None, False)


def processData(data, size=9):
    board = [[0 for y in range(size)] for x in range(size)]
    squares = data['squares']
    for each in squares:
        x = each['x']
        y = each['y']
        value = each['value']
        board[x][y] = value  # Attention
    return board
  

#  board = getResponse(9, 2)
#  print(board)
