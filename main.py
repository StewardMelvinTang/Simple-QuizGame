import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from quizchild import QuizStruct
import json

TITLE_FONT_STYLE = ("Arial", 15, "bold")
BUTTON_FONT_STYLE = ("Arial", 25)
def menu_about_click():
    messagebox.showinfo("About", "Created by Steward Melvin Tang with love <3")
def setScreensize(window, res):
    window.geometry(res)
    window.resizable(False,False)
    #split the resolution string from "500x500" to ["500", "500"]
    split_res = res.split("x")
    #set to center of screen
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x_pos = int(screen_width / 2 - int(split_res[0]) / 2)
    y_pos = int(screen_height / 2 - int(split_res[1]) / 2)
    window.geometry("+{}+{}".format(x_pos, y_pos))
def createQuiz(frame, index):
    global button_frame, label_quiz_name
    if index < quiz_length:
        quiz_data_byindex = quiz_data[index]
        label_quiz_name = tk.Label(frame, text=quiz_data_byindex["quiz_name"], font=TITLE_FONT_STYLE, fg="black", bg="#e8e8e8", wraplength=500)
        label_quiz_name.pack(fill="x", expand=False)
        correctanswer = quiz_data_byindex["correct_answer"]
        answers = quiz_data_byindex["quiz_answers"]
        
        button_frame = tk.Frame(frame, bg="#e8e8e8")
        
        for answer in answers:
            btn_answer = ttk.Button(button_frame, text=answer, command=lambda a = answer, b = correctanswer: onAnswerChoosed(a, b))
            btn_answer.pack(side=tk.LEFT, padx=5)
            
        button_frame.pack(pady=(25 , 0))
    else:
        gameFinished()
def onAnswerChoosed(answer, correctanswer):
    global current_quiz_index, correct_answer, wrong_answer, frame, button_frame, label_quiz_name
    if (answer == correctanswer):
        print ("Correct Answer")
        correct_answer += 1
    else:
        print("Wrong Answer")
        wrong_answer += 1
    button_frame.destroy()
    label_quiz_name.destroy()
    current_quiz_index += 1
    label_answerpoint.config(text=f"{current_quiz_index + 1}/{quiz_length}")
    createQuiz(frame, current_quiz_index)
    
def updateCounter():
    if current_quiz_index+1 >= quiz_length:
        gameFinished()
    else:
        label_answerpoint.config(text=f"{current_quiz_index + 1}/{quiz_length}")
    
def gameFinished():
    if current_quiz_index+1 > len(quiz_data):
        label_answerpoint.config(text="You Finished the game!")
        label_correct = tk.Label(frame, text=f"Correct Answers: {correct_answer}", font=TITLE_FONT_STYLE).pack(pady=10)
        label_wrong = tk.Label(frame, text=f"Wrong Answers: {wrong_answer}", font=TITLE_FONT_STYLE).pack(pady=10)
        
def restartGame():
    current_quiz_index = 0
    wrong_answer = 0
    correct_answer = 0
    button_frame.destroy()
    label_quiz_name.destroy()
    label_answerpoint.config(text=f"1/{quiz_length}")
    createQuiz(frame, current_quiz_index)

window = tk.Tk()
setScreensize(window, "500x500")
window.title("Quiz Game")

with open('quiz_data.json', 'r') as f:
    quiz_data = json.load(f)
    quiz_length = len(quiz_data)
    current_quiz_index = 0
    wrong_answer = 0
    correct_answer = 0
    
menu_bar = tk.Menu(window)
window.config(menu=menu_bar)
menu_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Menu", menu=menu_menu)

menu_menu.add_command(label="Tips")
menu_menu.add_command(label="Restart", command=restartGame)
menu_menu.add_separator()
menu_menu.add_command(label="About", command=menu_about_click)
menu_menu.add_command(label="Exit", command=window.quit)

frame = tk.Frame(window, background="#e8e8e8", pady=5)
frame.pack(fill="both", expand=False)


label_answerpoint = tk.Label(frame,text=f"{current_quiz_index + 1}/{quiz_length}", font=TITLE_FONT_STYLE, bg="#e8e8e8")
label_answerpoint.pack(pady=(0, 15))

createQuiz(frame=frame, index=0)


window.mainloop()