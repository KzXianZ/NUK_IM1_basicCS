symbol = {
  0: " ",
  1: "O",
  2: "X",
}

board = [
  [0, 0, 0],
  [0, 0, 0],
  [0, 0, 0],
]

def print_board():
  print(
    symbol[board[0][0]] + "|" + symbol[board[0][1]] + "|" + symbol[board[0][2]] + "\n" +
    "-----\n" +
    symbol[board[1][0]] + "|" + symbol[board[1][1]] + "|" + symbol[board[1][2]] + "\n" +
    "-----\n" +
    symbol[board[2][0]] + "|" + symbol[board[2][1]] + "|" + symbol[board[2][2]] + "\n"
  )


# 回傳 1 代表 O 贏了
# 回傳 2 代表 X 贏了
# 回傳 0 代表沒人贏
# 回傳 3 代表平手
def check_win():
  # AAA
  # ???
  # ???
  if (board[0][0] != 0) and (board[0][0] == board[0][1] == board[0][2]): return board[0][0]

  # ???
  # AAA
  # ???
  if (board[1][0] != 0) and (board[1][0] == board[1][1] == board[1][2]): return board[1][0]

  # ???
  # ???
  # AAA
  if (board[2][0] != 0) and (board[2][0] == board[2][1] == board[2][2]): return board[2][0]

  # A??
  # A??
  # A??
  if (board[0][0] != 0) and (board[0][0] == board[1][0] == board[2][0]): return board[0][0]

  # ?A?
  # ?A?
  # ?A?
  if (board[0][1] != 0) and (board[0][1] == board[1][1] == board[2][1]): return board[0][1]

  # ??A
  # ??A
  # ??A
  if (board[0][2] != 0) and (board[0][2] == board[1][2] == board[2][2]): return board[0][2]

  # A??
  # ?A?
  # ??A
  if (board[0][0] != 0) and (board[0][0] == board[1][1] == board[2][2]): return board[0][0]

  # ??A
  # ?A?
  # A??
  if (board[0][2] != 0) and (board[0][2] == board[1][1] == board[2][0]): return board[0][2]

  # 平手
  if ((board[0][0] != 0) and (board[0][1] != 0) and (board[0][2] != 0) and
      (board[1][0] != 0) and (board[1][1] != 0) and (board[1][2] != 0) and
      (board[2][0] != 0) and (board[2][1] != 0) and (board[2][2] != 0)):
    return 3

  return 0


turn = 1

# 遊戲迴圈
while True:
  print_board()

  # 印出誰的回合
  if turn == 1:
    print("O 的回合")

  else:
    print("X 的回合")

  # 輸入位置
  while True:
    # 取得行
    col = int(input("col: "))

    # 檢查行是否超出範圍
    if 0 > col or col > 2:
      print("超出範圍!")
      continue

    # 取得列
    row = int(input("row: "))

    # 檢查列是否超出範圍
    if 0 > row or row > 2:
      print("超出範圍!")
      continue

    # 檢查是否已經有棋子
    if board[row][col] != 0:
      print("已經有棋子了!")
      continue

    # 完成輸入
    break

  # 放置棋子
  board[row][col] = turn

  # 檢查是否有人贏了
  winner = check_win()

  if winner == 1:
    print("O 贏了")
    break

  elif winner == 2:
    print("X 贏了")
    break

  elif winner == 3:
    print("平手")
    break

  # 換人
  if turn == 1:
    turn = 2

  else:
    turn = 1

  # 印出分隔線
  print("------------\n\n\n")

