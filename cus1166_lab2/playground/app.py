from flask import Flask, render_template

app = Flask(__name__)
class_roster = [
    ("Jonella Wong", "B", "Senior"),
    ("Dan Guerrero", "A", "Sophmore"),
    ("George Clinton", "C", "Senior"),
]

def index():
    return render_template("index.html")

def welcome(student_name):
    return render_template("welcome.html", student_name=student_name)

def roster(grade_view):
    print(grade_view)
    return render_template("roster.html", class_roster=class_roster, grade_view=grade_view)

if __name__ == "__main__":
    app.run()
