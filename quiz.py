import tkinter as tk
from tkinter import messagebox

# Questions and answers
questions = [
    {"question": "What is the capital of Uganda?", "options": ["Mitooma", "Kampala", "Mbarara", "Gulu"], "answer": "Kampala"},
    {"question": "Which programming language is known as the language of the web?", "options": ["C++", "Python", "JavaScript", "Java"], "answer": "JavaScript"},
    {"question": "What is the largest planet in our solar system?", "options": ["Earth", "Jupiter", "Mars", "Saturn"], "answer": "Jupiter"},
    {"question": "Who wrote 'Romeo and Juliet'?", "options": ["Charles Dickens", "William Shakespeare", "Mark Twain", "Jane Austen"], "answer": "William Shakespeare"},
    {"question": "What is the boiling point of water?", "options": ["90°C", "100°C", "110°C", "120°C"], "answer": "100°C"},
]

# Quiz application class
class QuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title(" VU Quiz Application")
        self.root.geometry("500x400")
        self.root.configure(bg="#2c3e50")

        self.score = 0
        self.current_question = 0
        self.correct_answers = []

        self.title_label = tk.Label(
            root, text="Welcome to the Quiz", font=("Arial", 18, "bold"), bg="#34495e", fg="white", padx=10, pady=10
        )
        self.title_label.pack(fill="x")

        self.question_label = tk.Label(
            root, text="", font=("Arial", 16), wraplength=450, bg="#2c3e50", fg="white", pady=20
        )
        self.question_label.pack()

        self.options_frame = tk.Frame(root, bg="#2c3e50")
        self.options_frame.pack(pady=10)

        self.selected_option = tk.StringVar(value="")
        self.radio_buttons = []
        for _ in range(4):
            button = tk.Radiobutton(
                self.options_frame,
                text="",
                variable=self.selected_option,
                value="",
                font=("Arial", 14),
                bg="#34495e",
                fg="white",
                selectcolor="#1abc9c",
                anchor="w",
                wraplength=400
            )
            button.pack(anchor="w", pady=5, padx=10)
            self.radio_buttons.append(button)

        self.submit_button = tk.Button(
            root,
            text="Submit",
            font=("Arial", 14),
            bg="#1abc9c",
            fg="white",
            activebackground="#16a085",
            activeforeground="white",
            command=self.submit_answer
        )
        self.submit_button.pack(pady=20)

        self.footer_label = tk.Label(
            root, text="Good Luck!", font=("Arial", 12, "italic"), bg="#2c3e50", fg="#bdc3c7"
        )
        self.footer_label.pack(side="bottom", pady=10)

        self.display_question()

    def display_question(self):
        if self.current_question < len(questions):
            question = questions[self.current_question]
            self.question_label.config(text=question["question"])

            for i, option in enumerate(question["options"]):
                self.radio_buttons[i].config(text=option, value=option)
            self.selected_option.set("")
        else:
            self.show_score()

    def submit_answer(self):
        selected_option = self.selected_option.get()

        if selected_option:
            correct_answer = questions[self.current_question]["answer"]
            if selected_option == correct_answer:
                self.score += 1
            else:
                self.correct_answers.append(
                    f"Q: {questions[self.current_question]['question']}\nYour Answer: {selected_option}\nCorrect Answer: {correct_answer}"
                )

            self.current_question += 1
            self.display_question()
        else:
            messagebox.showwarning("Warning", "Please select an answer before submitting.")

    def show_score(self):
        result_message = f"Your score: {self.score}/{len(questions)}\n\n"
        if self.correct_answers:
            result_message += "Questions you got wrong:\n\n" + "\n\n".join(self.correct_answers)

        messagebox.showinfo(
            "Quiz Completed", result_message
        )
        self.root.quit()

# Main application
if __name__ == "__main__":
    root = tk.Tk()
    app = QuizApp(root)
    root.mainloop()
