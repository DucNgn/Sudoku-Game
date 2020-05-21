from flask import Flask, flash, request, render_template, redirect, url_for

import algorithms
import getSudoku
import copy

app = Flask(__name__)

board = []
example = [
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
    global board, blankIndex
    for y in range(9):
        for x in range(9):
            if(board[y][x] == 0):
                index = 9*y + x
                slot = str(index)
                blankIndex.append(slot)


def convertToString(target):
    string = ''
    for y in range(9):
        for x in range(9):
            string = string + str(target[y][x])
    return string


@app.route("/")
def index():
    return redirect(url_for('home'))


@app.route("/home")
def home():
    return render_template("welcome.html")

@app.route("/sudoku")
def sudoku():
    global board
    boardLevel = request.args.get('level')
    if (boardLevel != "0"):
        print('Generating random')
        (respBoard, respCode) = getSudoku.getResponse(9, 2)
        if respCode is True:
            board = respBoard
    else:
        board = copy.deepcopy(example)

    generateBlankIndex()
    out = convertToString(board)
    return render_template("index.html", strInput=out, visibility="visible")


# Get inputs from user when submitted
@app.route("/sudoku", methods=["POST"])
def getInputs():
    global board, blankIndex
    inputs = list(map(getEachInput, blankIndex))
    print(inputs)
    if(isValid(inputs)):
        flash("Congratulation !! You have solved the Sudoku board", "success")
    else:
        flash("Your solution is incorrect !!", "warning")
    return redirect(request.url)


def getEachInput(index):
    return request.form[index]


# Validate the solution
def isValid(inputs):
    global board, blankIndex
    temp = copy.deepcopy(board)
    for (i, j) in zip(blankIndex, inputs):
        x = int(i) % 9
        y = int((int(i) - x) / 9)
        if (j == ""):
            temp[y][x] = 0
            continue
        temp[y][x] = int(j)
    
    return algorithms.isBoardValid(temp)


# Solve the Sudoku board
@app.route("/solved")
def render_solved():
    global board
    (solvedBoard, solvable) = algorithms.solve(board)
    if(solvable):
        out = convertToString(solvedBoard)
        flash("This Sudoku board is solved", "success")
        return render_template("index.html", strInput=out, visibility="hidden")
    else:
        flash("This Sudoku board is unsolvable !!!", "error")
        out = convertToString(board)
        return render_template("index.html", strInput=out, visibility="hidden")


if __name__ == '__main__':
    app.secret_key = 'secret'
    app.run(debug=True)
