import tkinter as tk
from functions import on_click, win_lines, reset
import logging

logger = logging.getLogger(__name__)
file_handler = logging.FileHandler("gui2.log")
logger.addHandler(file_handler)
logger.setLevel(logging.INFO)
formatter = logging.Formatter("%(asctime)s:%(levelname)s:%(funcName)s:%(message)s")
file_handler.setFormatter(formatter)

window = tk.Tk()
window.title("Tic-Tac-Toe (by AV)")


def create_buttons():
    game_mode_var = tk.StringVar()
    game_mode_var.set("Player X vs Player O")

    game_modes = tk.Menu(window)
    window.config(menu=game_modes)
    sub_game_modes = tk.Menu(game_modes, tearoff=0)

    def set_game_mode(mode):
        game_mode_var.set(mode)
        reset(buttons_list, top_info)
        logger.info(f"Game mode: {mode}. Completed.")

    game_modes.add_cascade(label="GameMode", menu=sub_game_modes)
    sub_game_modes.add_command(label="Player X vs Player O", command=lambda: set_game_mode("Player X vs Player O"))
    sub_game_modes.add_command(label='Player vs AI "Normal Mode"', command=lambda: set_game_mode('Player vs AI "Normal Mode"'))
    sub_game_modes.add_command(label='Player vs AI "Hard Mode"', command=lambda: set_game_mode('Player vs AI "Hard Mode"'))

    status_bar = tk.Label(window, textvariable=game_mode_var, relief=tk.SUNKEN, anchor=tk.W)
    status_bar.grid(row=6, columnspan=5, sticky="we")

    top_info = tk.Label(window, text="Player X move", font="Arial")
    top_info.grid(row=0, columnspan=5)

    empty_space = tk.Label(window, width=7, height=3)
    empty_space.grid(row=0, column=0)

    button1 = tk.Button(window, text="", width=7, height=3, command=lambda: (on_click(button1, top_info, buttons_list, count_win, game_mode_var), win_lines(buttons_list, top_info, count_win)))
    button1.grid(row=1, column=1)
    button2 = tk.Button(window, text="", width=7, height=3, command=lambda: (on_click(button2, top_info, buttons_list, count_win, game_mode_var), win_lines(buttons_list, top_info, count_win)))
    button2.grid(row=1, column=2)
    button3 = tk.Button(window, text="", width=7, height=3, command=lambda: (on_click(button3, top_info, buttons_list, count_win, game_mode_var), win_lines(buttons_list, top_info, count_win)))
    button3.grid(row=1, column=3)
    button4 = tk.Button(window, text="", width=7, height=3, command=lambda: (on_click(button4, top_info, buttons_list, count_win, game_mode_var), win_lines(buttons_list, top_info, count_win)))
    button4.grid(row=2, column=1)
    button5 = tk.Button(window, text="", width=7, height=3, command=lambda: (on_click(button5, top_info, buttons_list, count_win, game_mode_var), win_lines(buttons_list, top_info, count_win)))
    button5.grid(row=2, column=2)
    button6 = tk.Button(window, text="", width=7, height=3, command=lambda: (on_click(button6, top_info, buttons_list, count_win, game_mode_var), win_lines(buttons_list, top_info, count_win)))
    button6.grid(row=2, column=3)
    button7 = tk.Button(window, text="", width=7, height=3, command=lambda: (on_click(button7, top_info, buttons_list, count_win, game_mode_var), win_lines(buttons_list, top_info, count_win)))
    button7.grid(row=3, column=1)
    button8 = tk.Button(window, text="", width=7, height=3, command=lambda: (on_click(button8, top_info, buttons_list, count_win, game_mode_var), win_lines(buttons_list, top_info, count_win)))
    button8.grid(row=3, column=2)
    button9 = tk.Button(window, text="", width=7, height=3, command=lambda: (on_click(button9, top_info, buttons_list, count_win, game_mode_var), win_lines(buttons_list, top_info, count_win)))
    button9.grid(row=3, column=3)

    empty_space2 = tk.Label(window, width=7, height=3)
    empty_space2.grid(row=4, column=4)

    count_win = tk.Label(window, text="", font="Impact")
    count_win.grid(row=4, columnspan=5)

    buttons_list = [button1, button2, button3, button4, button5, button6, button7, button8, button9]
    win_lines(buttons_list, top_info, count_win)

    def reset_click():
        reset(buttons_list, top_info)
        logger.info("completed.")

    button_reset = tk.Button(window, text="Reset", width=10, height=2, command=reset_click)
    button_reset.grid(row=5, columnspan=2)

    def exit_game():
        window.quit()
        logger.info("completed.")

    button_exit = tk.Button(window, text="Exit", width=10, height=2, command=exit_game)
    button_exit.grid(row=5, column=3, columnspan=2)

    logger.info("completed.")


def main():
    create_buttons()
    window.mainloop()
    logger.info("complited.")


if __name__ == "__main__":
    main()
