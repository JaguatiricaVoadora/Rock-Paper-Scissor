import tkinter as tk
from tkinter import font
import random
import sys
import os

# Importa as listas do arquivo principal
from RockPaperScissor import Plays, Counters

# Cores retrô
BG_COLOR = '#22223b'
BTN_COLOR = '#9a8c98'
BTN_ACTIVE = '#f2e9e4'
LBL_COLOR = '#4a4e69'
TXT_COLOR = '#f2e9e4'

class RetroRPS:
    def __init__(self, root):
        self.root = root
        self.root.title('Rock Paper Scissor - Retro Edition')
        self.root.geometry('400x500')
        self.root.configure(bg=BG_COLOR)

        self.custom_font = font.Font(family='Courier', size=16, weight='bold')
        self.title_font = font.Font(family='Courier', size=22, weight='bold')

        self.user_score = 0
        self.cpu_score = 0

        self.create_widgets()

    def create_widgets(self):
        tk.Label(self.root, text='ROCK PAPER SCISSOR', font=self.title_font, fg=TXT_COLOR, bg=BG_COLOR).pack(pady=20)
        
        self.result_lbl = tk.Label(self.root, text='', font=self.custom_font, fg=TXT_COLOR, bg=LBL_COLOR, width=22, height=2)
        self.result_lbl.pack(pady=10)

        btn_frame = tk.Frame(self.root, bg=BG_COLOR)
        btn_frame.pack(pady=20)

        for play in Plays:
            btn = tk.Button(
                btn_frame,
                text=play,
                font=self.custom_font,
                bg=BTN_COLOR,
                fg=BG_COLOR,
                width=8,
                height=2,
                activebackground=BTN_ACTIVE,
                command=lambda p=play: self.play_round(p)
            )
            btn.pack(side='left', padx=10)

        self.user_lbl = tk.Label(self.root, text='Sua escolha: ', font=self.custom_font, fg=TXT_COLOR, bg=BG_COLOR)
        self.user_lbl.pack(pady=5)
        self.cpu_lbl = tk.Label(self.root, text='Computador: ', font=self.custom_font, fg=TXT_COLOR, bg=BG_COLOR)
        self.cpu_lbl.pack(pady=5)

        self.score_lbl = tk.Label(self.root, text='Placar - Você: 0  CPU: 0', font=self.custom_font, fg=TXT_COLOR, bg=BG_COLOR)
        self.score_lbl.pack(pady=20)

        tk.Button(self.root, text='Resetar', font=self.custom_font, bg=LBL_COLOR, fg=TXT_COLOR, command=self.reset_game).pack(pady=10)

    def play_round(self, user_choice):
        cpu_choice = random.choice(Plays)
        self.user_lbl.config(text=f'Sua escolha: {user_choice}')
        self.cpu_lbl.config(text=f'Computador: {cpu_choice}')

        if user_choice == cpu_choice:
            result = 'Empate!'
        elif Counters[cpu_choice] == user_choice:
            result = 'Você Ganhou!'
            self.user_score += 1
        else:
            result = 'Você Perdeu!'
            self.cpu_score += 1

        self.result_lbl.config(text=result)
        self.score_lbl.config(text=f'Placar - Você: {self.user_score}  CPU: {self.cpu_score}')

    def reset_game(self):
        self.user_score = 0
        self.cpu_score = 0
        self.result_lbl.config(text='')
        self.user_lbl.config(text='Sua escolha: ')
        self.cpu_lbl.config(text='Computador: ')
        self.score_lbl.config(text='Placar - Você: 0  CPU: 0')

def run_gui():
    root = tk.Tk()
    app = RetroRPS(root)
    root.mainloop()

if __name__ == '__main__':
    run_gui()
