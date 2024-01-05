# -*- coding: utf-8 -*-

import tkinter as tk
from tkinter import messagebox
import random

class TaiXiuGame:
    def __init__(self, master):
        self.master = master
        self.master.title("Game Đánh Tài Xỉu")
        self.master.geometry("400x200")

        self.dice_faces = ['\u2681', '\u2682', '\u2683', '\u2684', '\u2685']

        self.dice_label = tk.Label(self.master, font=("Helvetica", 100))
        self.result_label = tk.Label(self.master, font=("Helvetica", 20))

        self.bet_button = tk.Button(self.master, text="Đặt cược", command=self.roll_dice)
        self.bet_button.pack(pady=10)

        self.dice_label.pack()
        self.result_label.pack()

    def roll_dice(self):
        first_dice = random.randint(1, 6)
        second_dice = random.randint(1, 6)
        third_dice = random.randint(1, 6)

        dice_result = '{} {} {}'.format(self.dice_faces[first_dice - 1], self.dice_faces[second_dice - 1], self.dice_faces[third_dice - 1])
        self.dice_label.config(text=dice_result)

        total_sum = first_dice + second_dice + third_dice
        result_text = 'Tài' if total_sum > 10 else 'Xỉu'
        color = 'red' if total_sum > 10 else 'green'

        self.result_label.config(text=result_text, foreground=color)

        messagebox.showinfo("Kết quả", "Kết quả: {}".format(result_text))

if __name__ == "__main__":
    root = tk.Tk()
    game = TaiXiuGame(root)
    root.mainloop()
