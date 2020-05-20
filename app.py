from flask import Flask, request, render_template, redirect, url_for
import algorithms
import copy

app = Flask(__name__)

board = [
            [3, 0, 6, 5, 0, 8, 4, 0, 0],
            [5, 2, 0, 0, 0, 0, 0, 0, 0],
            [0, 8, 7, 0, 0, 0, 0, 3, 1],
            [0, 0, 3, 0, 1, 0, 0, 8, 0],
            [9, 0, 0, 8, 6, 3, 0, 0, 5],
            [0, 5, 0, 0, 9, 0, 6, 0, 0],
            [1, 3, 0, 0, 0, 0, 2, 5, 0],
            [0, 0, 0, 0, 0, 0, 0, 7, 4],
            [0, 0, 5, 2, 0, 6, 3, 0, 0]]


blankIndex = []


def generateBlankIndex():
    for y in range(9):
        for x in range(9):
            if(board[y][x] == 0):
                index = 9*y + x
                slot = str(index)
                blankIndex.append(slot)


@app.route("/")
def index():
    return redirect(url_for('home'))


@app.route("/home")
def home():
    out = convertToString(board)
    return render_template("index.html", strInput=out)


@app.route("/home", methods=["POST"])
def getInputs():
    inputs = list(map(getEachInput, blankIndex))
    if(isValid(inputs)):
        return "<h1> Correct </h1>"
    else:
        return "<h1> Wrong </h1>"


def getEachInput(index):
    return request.form[index]


def isValid(inputs):
    temp = copy.deepcopy(board)
    for (i, j) in zip(blankIndex, inputs):
        x = int(i) % 9
        y = int((int(i) - x) / 9)
        if (j == ""):
            temp[y][x] = 0
            continue
        temp[y][x] = int(j)
    
    return algorithms.isBoardValid(temp)


def convertToString(target):
    string = ''
    for y in range(9):
        for x in range(9):
            string = string + str(target[y][x])
    return string


@app.route("/solved")
def render_solved():
    (solvedBoard, solvable) = algorithms.solve(board)
    out = convertToString(solvedBoard)
    if(solvable):
        return render_template("index.html", strInput=out)
    else:
        return "<h1> The sudoku board is not solvable </h1>"


if __name__ == '__main__':
    generateBlankIndex()
    app.run(debug=True)
