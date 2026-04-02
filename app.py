from flask import Flask, render_template, request
from model import predict
import matplotlib.pyplot as plt
import os

app = Flask(__name__)

# Ensure static folder exists
if not os.path.exists('static'):
    os.makedirs('static')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def get_prediction():
    # Get inputs
    attendance = float(request.form['attendance'])
    study_hours = float(request.form['study_hours'])
    marks = float(request.form['marks'])
    assignments = float(request.form['assignments'])

    # Prediction
    result = predict(attendance, study_hours, marks, assignments)

    # Status
    if result >= 75:
        status = "Good Performance"
    else:
        status = "Needs Improvement"

    # Suggestions
    suggestions = []

    if attendance < 75:
        suggestions.append("Improve attendance")

    if study_hours < 2:
        suggestions.append("Increase study hours")

    if marks < 60:
        suggestions.append("Focus on weak subjects")

    if assignments < 70:
        suggestions.append("Complete more assignments")

    if not suggestions:
        suggestions.append("Keep up the good work!")

    # Create graph
    labels = ['Attendance', 'Study Hours', 'Marks', 'Assignments']
    values = [attendance, study_hours, marks, assignments]

    plt.figure()
    plt.bar(labels, values)
    plt.title("Student Performance Factors")
    plt.savefig('static/graph.png')
    plt.close()

    return render_template('index.html',
                           prediction=round(result, 2),
                           status=status,
                           tips=suggestions)

if __name__ == "__main__":
    app.run(debug=True)