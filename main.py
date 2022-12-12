# 38. Напишите программу, удаляющую из текста все слова, содержащие "абв".

# def del_some_words(my_text):
#     my_text = list(filter(lambda x: 'абв' not in x, my_text.split()))
#     return " ".join(my_text)
# my_text = 'ghj про грам неабв абв стило абваш громав'
# my_text = del_some_words(my_text)
# print(my_text)

#___________________________________________________________________________________________
# 39. Создайте программу для игры с конфетами человек против человека.
#   Условие задачи: На столе лежит 2021 конфета. Играют два игрока, делая ход друг после друга.
#   Первый ход определяется жеребьевкой. За один ход можно забрать не более чем 28 конфет.
#   Все конфеты оппонента достаются сделавшему последний ход. Сколько конфет нужно взять первому игроку,
#   чтобы забрать все конфеты у своего конкурента?
#       а) добавьте игру против бота
#       б) подумайте как наделить бота "интеллектом"
#
#_______________________________________________________________________________________________
# 40. Создайте программу для игры в "Крестики-нолики".

# board = [7, 8, 9,
#          4, 5, 6,
#          1, 2, 3]
# vins = [[0, 1, 2],
#         [3, 4, 5],
#         [6, 7, 8],
#         [0, 3, 6],
#         [1, 4, 7],
#         [2, 5, 8],
#         [0, 4, 8],
#         [2, 4, 6]]
#
# def print_board():
#     print(board[0], board[1], board[2])
#     print(board[3], board[4], board[5])
#     print(board[6], board[7], board[8])
#
# def step_next(step, symbol):
#     if step in board:
#         i = board.index(step)
#         board[i] = symbol
#     else:
#         print('This cell is busy or not exist, you lose your move!')
#
# def get_result():
#     win = ''
#     for i in vins:
#         if board[i[0]] == 'X' and board[i[1]] == 'X' and board[i[2]] == 'X':
#             win = 'Player 1'
#         if board[i[0]] == 'O' and board[i[1]] == 'O' and board[i[2]] == 'O':
#             win = 'Player 2'
#     return win
#
# game_over = False
# player1 = True
# count = 0
#
# while game_over == False:
#     print_board()
#     if player1 == True:
#         symbol = 'X'
#         step = int(input('Player 1, Make your move! Print cell number: '))
#     else:
#         symbol = 'O'
#         step = int(input('Player 2, Make your move! Print cell number: '))
#
#     step_next(step, symbol)
#     win = get_result()
#     if win != '' or count == 8:
#         game_over = True
#     else:
#         game_over = False
#
#     player1 = not (player1)
#     count += 1
#
# print_board()
# if win != '':
#     print(win, 'wins!')
# else:
#     print('Nobody wins -:-')
#
#_____________________________________________________________________________________
# 42. Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.

# def rle_crypt(in_str):
#     crypt = ''
#     i = 0
#     while i < len(in_str):
#         count = 1
#         while i + 1 < len(in_str) and in_str[i] == in_str[i + 1]:
#             count += 1
#             i += 1
#         crypt += str(count) + in_str[i]
#         i += 1
#     return crypt
#
#
# def rle_decrypt(in_str):
#     decrypt = ''
#     for i in range(0, len(in_str), 2):
#         decrypt += in_str[i + 1] * int(in_str[i])
#     return decrypt
#
#
# with open('code.txt', 'w', encoding='utf-8') as data:
#     data.write('qaaaqqaaqqqa')
#
# with open('code.txt', 'r', encoding='utf-8') as data:
#     code = data.read()
#
# crypt_code = rle_crypt(code)
# print(crypt_code)
#
# with open('crypt_code.txt', 'w', encoding='utf-8') as data:
#     data.write(crypt_code)
# with open('crypt_code.txt', 'r', encoding='utf-8') as data:
#     code1 = data.read()
#
# print(rle_decrypt(code1))

