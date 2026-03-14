from flask import Flask, render_template, request
 
app = Flask(__name__)
 
def generate_plan(bmi, age, gender):
 
    if bmi < 20:

        category = "Underweight"
 
        diet = [

            "Increase calorie intake",

            "Eat protein rich foods (eggs, chicken, beans)",

            "Add nuts and dairy products",

            "5–6 small meals per day"

        ]
 
        exercise = [

            "Light strength training 3 times/week",

            "Yoga or stretching",

            "Short walks"

        ]
 
    elif 20 <= bmi < 25:

        category = "Normal"
 
        diet = [

            "Balanced diet with fruits and vegetables",

            "Maintain regular meals",

            "Drink plenty of water"

        ]
 
        exercise = [

            "30 minutes cardio 4 times/week",

            "Strength training twice a week"

        ]
 
    else:

        category = "Overweight"
 
        diet = [

            "Reduce sugar and processed food",

            "Increase vegetables and fiber",

            "Eat lean proteins"

        ]
 
        exercise = [

            "45 minutes brisk walking",

            "Cycling or jogging",

            "Strength training 3 times/week"

        ]
 
    return category, diet, exercise
 
 
@app.route("/", methods=["GET", "POST"])

def index():
 
    bmi = None

    category = None

    diet = None

    exercise = None
 
    if request.method == "POST":
 
        weight = float(request.form["weight"])

        height_cm = float(request.form["height"])

        age = int(request.form["age"])

        gender = request.form["gender"]
 
        height = height_cm / 100

        bmi = round(weight / (height ** 2), 2)
 
        category, diet, exercise = generate_plan(bmi, age, gender)
 
    return render_template(

        "index.html",

        bmi=bmi,

        category=category,

        diet=diet,

        exercise=exercise

    )
 
 
if __name__ == "__main__":

    app.run(debug=True)

 