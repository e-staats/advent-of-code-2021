from rich import print
from icecream import ic


def chunkstring(string, length):
    return (string[0 + i : length + i] for i in range(0, len(string), length))


def check_rows_and_columns(marking_grid):
    for i in range(len(marking_grid)):
        if sum(marking_grid[i]) == 5:
            return True
        column = True
        for j in range(5):
            if marking_grid[j][i] == 0:
                column = False
        if column == True:
            return True
    return False


def check_diagonals(marking_grid):
    down_diag = True
    up_diag = True
    for i in range(len(marking_grid)):
        if marking_grid[i][i] == 0:
            down_diag = False
        if marking_grid[4 - i][4 - i] == 0:
            up_diag = False
    return down_diag or up_diag


def main():
    with open("../inputs/day4.txt", "r") as file:
        numbers = file.readline()
        numbers = numbers.split(",")
        result = [1000,0] #initialize to something that will get replaced by the first value
        reading = True
        while reading == True:
            line = file.readline().split(",")
            if len(line) == 0:
                reading = False
                break
            if len(line) == 1:
                bingo_card = create_bingo_card(file)
                if len(bingo_card[0]) == 0:
                    reading = False
                    break

                # create index and marking gird:
                bingo_index = {}
                marking_grid = []
                for i in range(5):
                    marking_grid.append([])
                    for j in range(5):
                        bingo_index[bingo_card[i][j]] = (i, j)
                        marking_grid[i].append(0)

                # start playing and score card:
                duration, score = play_and_score(bingo_card, bingo_index, marking_grid, numbers)
                if duration < result[0]:
                    result = (duration, score)
    print(result)                


def create_bingo_card(file):
    bingo_card = []
    for i in range(5):
        line = chunkstring(file.readline(), 3)
        bingo_card.append(list(map(str.strip, line)))
    return bingo_card


def play_and_score(bingo_card, bingo_index, marking_grid, numbers):
    num_count = 0
    for number in numbers:
        num_count += 1
        if number in bingo_index.keys():
            i, j = bingo_index[number]
            marking_grid[i][j] = 1
            if check_rows_and_columns(marking_grid) or check_diagonals(marking_grid):
                return (num_count, score_board(bingo_card, marking_grid, number))
    return (num_count, 0)  # if board does not win


def score_board(bingo_card, marking_grid, last_number):
    # sum unmarked numbers:
    sum = 0
    for i in range(5):
        for j in range(5):
            if marking_grid[i][j] == 0:
                sum += int(bingo_card[i][j])

    # multiply by last number:
    return sum * int(last_number)


if __name__ == "__main__":
    main()
    # marking_grid = [
    #     [1, 1, 1, 0, 1],
    #     [0, 1, 0, 1, 1],
    #     [1, 0, 1, 0, 1],
    #     [1, 1, 0, 1, 1],
    #     [1, 0, 0, 0, 0],
    # ]
    # print(check_rows_and_columns(marking_grid))
