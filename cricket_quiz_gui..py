import tkinter as tk
from tkinter import messagebox

quiz_questions = [
    {
        "question": "Which Indian player won the Player of the Tournament in T20 World Cup 2024?",
        "options": ["A. Jasprit Bumrah", "B. Virat Kohli", "C. Suryakumar Yadav", "D. Arshdeep Singh"],
        "ans": "A"
    },
    {
        "question": "Who was the top run-scorer for India in IPL 2024?",
        "options": ["A. Shubman Gill", "B. Virat Kohli", "C. Ruturaj Gaikwad", "D. Sanju Samson"],
        "ans": "B"
    },
    {
        "question": "Which team won IPL 2024?",
        "options": ["A. Mumbai Indians", "B. Chennai Super Kings", "C. Kolkata Knight Riders", "D. Gujarat Titans"],
        "ans": "C"
    },
    {
        "question": "Who took a hat-trick for India against Australia in the ODIs series?",
        "options": ["A. Bumrah", "B. Axar Patel", "C. Arshdeep Singh", "D. Kuldeep Yadav"],
        "ans": "D"
    },
    {
        "question": "Who is currently India's head coach (2025)?",
        "options": ["A. Rahul Dravid", "B. VVS Laxman", "C. Anil Kumble", "D. Gautam Gambhir"],
        "ans": "D"
    },
    {
        "question": "Which stadium hosted the T20 World Cup 2024 final?",
        "options": ["A. Eden Gardens", "B. Narendra Modi Stadium", "C. MCG", "D. Kensington Oval"],
        "ans": "D"
    },
    {
        "question": "Which Indian bowler reached 100 T20I wickets in 2024?",
        "options": ["A. Bhuvneshwar Kumar", "B. Ravindra Jadeja", "C. Yuzvendra Chahal", "D. Jasprit Bumrah"],
        "ans": "D"
    },
    {
        "question": "Which team won IPL 2022?",
        "options": ["A. Mumbai Indians", "B. Chennai Super Kings", "C. Kolkata Knight Riders", "D. Gujarat Titans"],
        "ans": "D"
    },
    {
        "question": "Who was the top run-scorer for India in 2023?",
        "options": ["A. Shubman Gill", "B. Virat Kohli", "C. Ruturaj Gaikwad", "D. Sanju Samson"],
        "ans": "A"
    },
    {
        "question": "Which young Indian player made his debut in 2024 and impressed in T20s?",
        "options": ["A. Riyan Parag", "B. Tilak Varma", "C. Yashasvi Jaiswal", "D. Abhishek Sharma"],
        "ans": "D"
    }
]

class QuizApp:
    def __init__(self, root, questions):
        self.root = root
        self.root.title("Quiz Game ")
        self.questions = questions
        self.q_index = 0
        self.score = 0
        self.time_left = 10
        self.timer_id = None
        self.answered = False

        self.timer_label = tk.Label(root, text="Time left: 10s", font=("Arial", 14), fg="blue")
        self.timer_label.pack(pady=5)

        self.question_label = tk.Label(root, text="", font=("Arial", 16), wraplength=500, justify="center")
        self.question_label.pack(pady=20)

        self.buttons = []
        for i in range(4):
            btn = tk.Button(root, text="", width=30, font=("Arial", 12), command=lambda i=i: self.check_answer(i))
            btn.pack(pady=5)
            self.buttons.append(btn)

        self.feedback_label = tk.Label(root, text="", font=("Arial", 12))
        self.feedback_label.pack(pady=10)

        self.load_question()

    def load_question(self):
        self.answered = False
        self.time_left = 10
        self.update_timer()

        q = self.questions[self.q_index]
        self.question_label.config(text=f"Q{self.q_index + 1}. {q['question']}")
        self.feedback_label.config(text="")
        for btn in self.buttons:
            btn.config(state="normal")

        for i, option in enumerate(q["options"]):
            self.buttons[i].config(text=option)

    def update_timer(self):
        self.timer_label.config(text=f"Time left: {self.time_left}s")
        if self.time_left > 0:
            self.time_left -= 1
            self.timer_id = self.root.after(1000, self.update_timer)
        else:
            self.check_answer(-1) 

    def check_answer(self, index):
        if self.answered:
            return
        self.answered = True
        self.root.after_cancel(self.timer_id)

        correct_answer = self.questions[self.q_index]['ans']

        if index == -1:
            self.feedback_label.config(text=f" Time's up! Correct answer: {correct_answer}", fg="orange")
        else:
            selected_option = self.buttons[index].cget("text")[0]
            if selected_option == correct_answer:
                self.score += 1
                self.feedback_label.config(text=" Correct!", fg="green")
            else:
                self.feedback_label.config(text=f" Wrong! Correct answer: {correct_answer}", fg="red")

        for btn in self.buttons:
            btn.config(state="disabled")

        self.root.after(1000, self.next_question)  

    def next_question(self):
        self.q_index += 1
        if self.q_index < len(self.questions):
            self.load_question()
        else:
            self.show_score()

    def show_score(self):
        result = f"🏁 You scored {self.score} out of {len(self.questions)}!"
        if self.score == len(self.questions):
            result += "\n Perfect Score!"
        elif self.score >= len(self.questions) * 0.7:
            result += "\n Great job!"
        else:
            result += "\n Keep practicing!"
        messagebox.showinfo("Quiz Finished", result)
        self.root.destroy()

root = tk.Tk()
app = QuizApp(root, quiz_questions)
root.mainloop()
