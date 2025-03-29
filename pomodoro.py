import tkinter as tk
import math
from constants import PINK, RED, GREEN, YELLOW, FONT_NAME, WORK_MIN, SHORT_BREAK_MIN, LONG_BREAK_MIN

class PomodoroTimer:
    def __init__(self):
        self.reps = 0
        self.timer = None
        
        # Configuração da Janela
        self.window = tk.Tk()
        self.window.title("Pomodoro")
        self.window.config(padx=100, pady=50, bg=YELLOW)
        
        # Título
        self.title_label = tk.Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 50, "bold"))
        self.title_label.grid(row=0, column=1)
        
        # Canvas e Imagem
        self.canvas = tk.Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
        self.tomato_img = tk.PhotoImage(file="tomato.png")
        self.canvas.create_image(100, 112, image=self.tomato_img)
        self.timer_text = self.canvas.create_text(100, 138, text="00:00", fill="white", font=(FONT_NAME, 28, "bold"))
        self.canvas.grid(row=1, column=1)
        
        # Botões
        self.start_button = tk.Button(text="Start", highlightthickness=0, command=self.start_timer)
        self.start_button.grid(row=2, column=0)
        
        self.reset_button = tk.Button(text="Reset", highlightthickness=0, command=self.reset_timer)
        self.reset_button.grid(row=2, column=2)
        
        # Check Marks
        self.check_marks = tk.Label(fg=GREEN, bg=YELLOW)
        self.check_marks.grid(row=3, column=1)

    def reset_timer(self):
        """Reseta o temporizador e as variáveis."""
        if self.timer:
            self.window.after_cancel(self.timer)
        self.canvas.itemconfig(self.timer_text, text="00:00")
        self.title_label.config(text="Timer")
        self.check_marks.config(text="")
        self.reps = 0

    def start_timer(self):
        """Inicia o temporizador de acordo com o ciclo Pomodoro."""
        if self.timer:
            self.window.after_cancel(self.timer)
        
        self.reps += 1
        work_sec = WORK_MIN * 60
        short_break_sec = SHORT_BREAK_MIN * 60
        long_break_sec = LONG_BREAK_MIN * 60

        if self.reps % 8 == 0:
            self.count_down(long_break_sec)
            self.title_label.config(text="Break", fg=RED)
        elif self.reps % 2 == 0:
            self.count_down(short_break_sec)
            self.title_label.config(text="Break", fg=PINK)
        else:
            self.count_down(work_sec)
            self.title_label.config(text="Work", fg=GREEN)

    def count_down(self, count):
        """Executa a contagem regressiva do timer."""
        count_min = math.floor(count / 60)
        count_sec = count % 60
        count_sec = f"0{count_sec}" if count_sec < 10 else count_sec

        self.canvas.itemconfig(self.timer_text, text=f"{count_min}:{count_sec}")
        
        if count > 0:
            self.timer = self.window.after(1000, self.count_down, count - 1)
        else:
            self.start_timer()
            self.update_check_marks()

    def update_check_marks(self):
        """Atualiza os check marks conforme os ciclos de trabalho forem concluídos."""
        marks = "✔" * (self.reps // 2)
        self.check_marks.config(text=marks)

    def run(self):
        """Inicia o loop da interface gráfica."""
        self.window.mainloop()
