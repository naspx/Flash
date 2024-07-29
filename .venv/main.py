import tkinter as tk
import random


class NumberGuessingGame:
    def __init__(self, master):
        self.master = master
        self.master.title("Infrastruktur TIU by Bjorka")

        # Set the fixed size of the application window
        self.master.geometry("400x550")
        self.master.resizable(False, False)

        # Initialize the game
        self.generate_question()

        # Label to display the question
        self.question_label = tk.Label(master, text=self.question, font=('Arial', 24))
        self.question_label.pack(pady=10)

        # Frame for the buttons
        self.buttons_frame = tk.Frame(master)
        self.buttons_frame.pack()

        # Generate and place buttons with random numbers
        self.buttons = []
        self.generate_buttons()

        # Variable to store the player's input
        self.player_input = ""

        # Label to display the player's input
        self.input_label = tk.Label(master, text=self.player_input, font=('Arial', 18))
        self.input_label.pack(pady=10)

        # Button to restart the game
        self.restart_button = tk.Button(master, text=" Coba Ulang ", command=self.restart_game, font=('Arial', 14))
        self.restart_button.pack(pady=10)


    def generate_question(self):
        while True:
            self.num1 = random.randint(0, 99)
            self.num2 = random.randint(0, 99)
            self.operation = random.choice(['+', '-', '*' ]) #, '/'])

            if self.operation == '+':
                self.answer = self.num1 + self.num2
            elif self.operation == '-':
                self.answer = self.num1 - self.num2
            elif self.operation == '*':
                self.answer = self.num1 * self.num2
            elif self.operation == '/':
                self.num2 = random.randint(1, 9)  # Ensure single-digit denominator
                self.answer = round(self.num1 / self.num2, 2)  # Use float division and round to 2 decimal places

            # Ensure the answer is within the range 0-99
            if 0 <= self.answer <= 99:
                break

        self.question = f"{self.num1} {self.operation} {self.num2} = ... ?"

    def generate_buttons(self):
        # Clear existing buttons
        for button in self.buttons:
            button.destroy()

        # Generate random positions for buttons
        numbers = list(range(10)) + [' '] + [' ']
        random.shuffle(numbers)

        for i, num in enumerate(numbers):
            button = tk.Button(self.buttons_frame, text=str(num), command=lambda n=num: self.update_input(n),
                               font=('Arial', 18), width=5, height=2)
            button.grid(row=i // 3, column=i % 3, padx=5, pady=5)
            self.buttons.append(button)

    def update_input(self, num):
        if num == '.' and '.' in self.player_input:
            return
        self.player_input += str(num)
        self.input_label.config(text=self.player_input)

        # Check if the player input is a valid multi-digit number or decimal
        if len(self.player_input) >= len(str(self.answer)) or '.' in self.player_input:
            self.check_answer()

    def check_answer(self):
        try:
            if float(self.player_input) == self.answer:
                self.question_label.config(text="Betul! Coba lagi.")
                self.master.after(2000, self.next_question)
            else:
                self.question_label.config(text="Salah! Coba ulang.")
                self.player_input = ""
                self.input_label.config(text=self.player_input)

        except ValueError:
            self.question_label.config(text="Invalid input! Coba ulang.")
            self.player_input = ""
            self.input_label.config(text=self.player_input)

    def next_question(self):
        self.generate_question()
        self.question_label.config(text=self.question)
        self.generate_buttons()
        self.player_input = ""
        self.input_label.config(text=self.player_input)

    def restart_game(self):
        self.next_question()


if __name__ == "__main__":
    root = tk.Tk()
    game = NumberGuessingGame(root)
    root.mainloop()
