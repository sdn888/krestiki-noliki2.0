import tkinter as tk
from tkinter import messagebox, simpledialog

# Основные переменные
window = tk.Tk()
window.title("Крестики-нолики: серия до 3-х побед")
window.geometry("400x450")
window.configure(bg="#f0f0f0")

current_player = "X"
player_choice = "X"
opponent_choice = "0"
buttons = []
player_score = {"X": 0, "0": 0}

# Функции
def on_click(row, col):
    global current_player
    if buttons[row][col]['text'] == "" and winner_label['text'].startswith("Ход"):
        buttons[row][col]['text'] = current_player
        if check_winner():
            player_score[current_player] += 1
            update_score()
            if player_score[current_player] == 3:
                messagebox.showinfo("Игра окончена", f"Игрок {current_player} победил в серии до 3 побед!")
                reset_all()
            else:
                messagebox.showinfo("Игра окончена", f"Игрок {current_player} победил!")
                reset_board()
            return
        elif check_draw():
            messagebox.showinfo("Игра окончена", "Ничья!")
            reset_board()
            return
        current_player = "0" if current_player == "X" else "X"
        update_turn_label()

def check_winner():
    # Проверка строк и столбцов
    for i in range(3):
        if buttons[i][0]["text"] == buttons[i][1]["text"] == buttons[i][2]["text"] != "":
            return True
        if buttons[0][i]["text"] == buttons[1][i]["text"] == buttons[2][i]["text"] != "":
            return True
    # Проверка диагоналей (вне цикла!)
    if buttons[0][0]["text"] == buttons[1][1]["text"] == buttons[2][2]["text"] != "":
        return True
    if buttons[0][2]["text"] == buttons[1][1]["text"] == buttons[2][0]["text"] != "":
        return True
    return False

def check_draw():
    for row in buttons:
        for btn in row:
            if btn['text'] == "":
                return False
    return True

def reset_board():
    for row in buttons:
        for btn in row:
            btn['text'] = ""
    update_turn_label()

def reset_all():
    global player_score, current_player
    player_score = {"X": 0, "0": 0}
    current_player = player_choice
    update_score()
    reset_board()

def update_score():
    score_label.config(text=f"Счёт: X - {player_score['X']} | 0 - {player_score['0']}")

def update_turn_label():
    winner_label.config(text=f"Ход игрока: {current_player}")

def choose_player():
    global player_choice, opponent_choice, current_player
    choice = simpledialog.askstring("Выбор игрока", "Выберите X или 0").upper()
    if choice not in ["X", "0"]:
        messagebox.showerror("Ошибка", "Выберите только X или 0!")
        choose_player()
    else:
        player_choice = choice
        opponent_choice = "0" if choice == "X" else "X"
        current_player = player_choice
        update_turn_label()

# Интерфейс
winner_label = tk.Label(window, text=f"Ход игрока: {current_player}", font=("Arial", 16), bg="#f0f0f0")
winner_label.pack(pady=10)

frame = tk.Frame(window, bg="#f0f0f0")
frame.pack()

for i in range(3):
    row = []
    for j in range(3):
        btn = tk.Button(frame, text="", font=("Arial", 24, "bold"), width=5, height=2,
                        bg="#ffffff", fg="#333333",
                        command=lambda r=i, c=j: on_click(r, c))
        btn.grid(row=i, column=j, padx=5, pady=5)
        row.append(btn)
    buttons.append(row)

score_label = tk.Label(window, text=f"Счёт: X - 0 | 0 - 0", font=("Arial", 14), bg="#f0f0f0")
score_label.pack(pady=10)

reset_button = tk.Button(window, text="Сбросить игру", font=("Arial", 14), bg="#4CAF50", fg="white", command=reset_all)
reset_button.pack(pady=10)

# Инициализация выбора
choose_player()

window.mainloop()
