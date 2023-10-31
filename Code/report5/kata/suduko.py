# 数独背景
# 数独是一种在 9x9 网格上进行的游戏。游戏的目标是用 1 到 9 的数字填充网格的所有单元格，以便每一列、每一行和九个 3x3 子网格（也称为块）中的都包含数字 1 到 9。更多信息请访问：http://en.wikipedia.org/wiki/Sudoku
# # 编写一个函数接受一个代表数独板的二维数组，如果它是一个有效的解决方案则返回 true，否则返回 false。数独板的单元格也可能包含 0，这将代表空单元格。包含一个或多个零的棋盘被认为是无效的解决方案。棋盘总是 9 x 9 格，每个格只包含 0 到 9 之间的整数。

import numpy as np


def validate_sudoku(board):
    sudoku = np.array(board)

    def is_valid_unit(unit):
        unique_numbers = np.unique(unit)
        return len(unique_numbers) == 9 and np.all(unique_numbers[unique_numbers != 0] == np.arange(1, 10))

    # 验证每一行
    for row in sudoku:
        if not is_valid_unit(row):
            return False

    # 验证每一列
    for col in sudoku.T:
        if not is_valid_unit(col):
            return False

    # 验证每个3x3子网格
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            subgrid = sudoku[i:i+3, j:j+3]
            if not is_valid_unit(subgrid):
                return False

    return True


# 测试示例
sudoku_board = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]

print(validate_sudoku(sudoku_board))  # 输出 True
