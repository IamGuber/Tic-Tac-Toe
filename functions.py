import tkinter
import random
import logging

logger = logging.getLogger(__name__)
file_handler = logging.FileHandler("functions2.log")
logger.addHandler(file_handler)
logger.setLevel(logging.INFO)
formatter = logging.Formatter("%(asctime)s:%(levelname)s:%(funcName)s:%(message)s")
file_handler.setFormatter(formatter)

game_over = False
player = "X"
x_winner = 0
o_winner = 0


def normal_mode(buttons, top_info, count_win, game_mode_var):
    logger.info("started.")

    if game_mode_var.get() == 'Player vs AI "Normal Mode"':
        empty_buttons = [button for button in buttons if button["text"] == ""]
        logger.info("AI moved.")

        if empty_buttons:
            selected_button = random.choice(empty_buttons)
            selected_button["text"] = "O"
            change_player()
            top_info["text"] = "Player X move"
            win_lines(buttons, top_info, count_win)
            logger.info("AI random move.")

    logger.info("completed.")


def hard_mode(buttons, top_info, count_win, game_mode_var):
    logger.info("started.")

    if game_mode_var.get() == 'Player vs AI "Hard Mode"':
        empty_buttons = [button for button in buttons if button["text"] == ""]
        logger.info("AI moved.")

        for button in empty_buttons:
            button["text"] = "O"
            if check_winner(buttons, "O"):
                button["text"] = "O"
                change_player()
                top_info["text"] = "Player X move"
                win_lines(buttons, top_info, count_win)
                logger.info("AI tried to win.")
                return

            button["text"] = ""

        for button in empty_buttons:
            button["text"] = "X"
            if check_winner(buttons, "X"):
                button["text"] = "O"
                change_player()
                top_info["text"] = "Player X move"
                win_lines(buttons, top_info, count_win)
                logger.info("AI tried to block win.")
                return

            button["text"] = ""

        if empty_buttons:
            selected_button = random.choice(empty_buttons)
            selected_button["text"] = "O"
            change_player()
            top_info["text"] = "Player X move"
            win_lines(buttons, top_info, count_win)
            logger.info("AI random move.")

    logger.info("completed.")


def check_winner(buttons, play):
    combinations_for_win = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
    for x in combinations_for_win:
        if all(buttons[y]["text"] == play for y in x):
            logger.info(f"matched win line: {x}.")
            return True
        logger.info(f"checking win line: {x}.")
    return False


def reset(buttons, info):
    global game_over, player
    for button in buttons:
        button["text"] = ""
    info["text"] = "Player X move"
    game_over = False
    player = "X"
    enable_buttons(buttons)
    logger.info("completed.")


def change_player():
    global player
    if player == "X":
        player = "O"
        logger.info('player changed to "O". ')
    else:
        player = "X"
        logger.info('player changed to "X".')
    logging.info("completed.")


def on_click(button, top_info, buttons, count_win, game_mode):
    global player, game_over

    if not game_over and button["text"] == "":
        button["text"] = player
        change_player()
        if player == "X":
            top_info["text"] = "Player X move"
        else:
            top_info["text"] = "Player O move"

        win_lines(buttons, top_info, count_win)

        if not game_over and game_mode.get() == 'Player vs AI "Normal Mode"' and player == "O":
            normal_mode(buttons, top_info, count_win, game_mode)

        if not game_over and game_mode.get() == 'Player vs AI "Hard Mode"' and player == "O":
            hard_mode(buttons, top_info, count_win, game_mode)


def win_lines(buttons, info, count_win):
    global game_over, x_winner, o_winner

    board = []

    for i in range(3):
        row = [buttons[i * 3]["text"], buttons[i * 3 + 1]["text"], buttons[i * 3 + 2]["text"]]
        board.append(row)
        column = [buttons[i]["text"], buttons[i + 3]["text"], buttons[i + 6]["text"]]
        board.append(column)
    diagram1 = [buttons[0]["text"], buttons[4]["text"], buttons[8]["text"]]
    board.append(diagram1)
    diagram2 = [buttons[2]["text"], buttons[4]["text"], buttons[6]["text"]]
    board.append(diagram2)

    for line in board:
        if all(cell == "X" for cell in line):
            info["text"] = "Player X winner!"
            x_winner += 0.5
            game_over = True
        elif all(cell == "O" for cell in line):
            info["text"] = "Player O winner!"
            o_winner += 0.5
            game_over = True

    if x_winner == 0 and o_winner == 0:
        count_win["text"] = f'Result: "X"-{int(x_winner)} : {int(o_winner)}-"O" '
    else:
        count_win["text"] = f'Result: "X"-{int(x_winner)} : {int(o_winner)}-"O" '

    if not game_over and all(button["text"] != "" for button in buttons):
        info["text"] = "Draw!"
        game_over = True

    if game_over:
        disable_buttons(buttons)


def disable_buttons(buttons):
    for button in buttons:
        button.config(state=tkinter.DISABLED)
    logger.info("buttons was disabled.")


def enable_buttons(buttons):
    for button in buttons:
        button.config(state=tkinter.ACTIVE)
    logger.info("buttons was enabled.")
