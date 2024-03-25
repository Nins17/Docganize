import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from tkinter import *

# inpt = int(input("Enter age: "))
# inptt = int(input("Enter 1 for female or 0 for male: "))


# print("most wanted genre: "+ prediction[0])

winblit = Tk()
winblit.geometry(('800x600'))

landing_scrn = Frame(winblit, width=800, height=900, bg="#282828")
landing_scrn.pack(expand=True)
canvas = Canvas(landing_scrn, width=750, height=550, bg="#8B8378")
canvas.place(x=25, y=25)
canvas.create_text(375, 100, text="Genre Predictor", font=("times new roman", 30), fill="white")
canvas.place()
canvas.create_text(100, 180, text="Enter Age:", font=("times new roman", 13, "bold"), fill="white")
canvas.place()
inpt_age = Entry(landing_scrn, font=("arial", 13), borderwidth=5, relief="sunken")
inpt_age.place(width=270, height=30, x=195, y=190)
canvas.create_text(115, 280, text="Enter Gender:", font=("times new roman", 13, "bold"), fill="white")
canvas.place()
inpt_gender = Entry(landing_scrn, font=("arial", 13), borderwidth=5, relief="sunken")
inpt_gender.place(width=270, height=30, x=195, y=290)


# machine learning process
def generatepred():
    data = pd.read_csv("Book1.csv")

    X = data.drop(columns=['genre'])
    Y = data['genre']

    ren = DecisionTreeClassifier()
    ren.fit(X.values, Y)  # train the machine learning
    prediction = ren.predict([[inpt_age, inpt_gender]])
    canvas.create_text(115, 350, text=prediction[0], font=("times new roman", 13, "bold"), fill="white")
    canvas.place()


button = Button(canvas, text="start", command=generatepred)
button.place(width=170, height=40, x=260, y=320)

winblit.mainloop()