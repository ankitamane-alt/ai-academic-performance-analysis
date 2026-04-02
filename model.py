from sklearn.linear_model import LinearRegression
import numpy as np

# Sample dataset (attendance, study_hours, marks, assignments)
X = np.array([
    [75, 2, 65, 60],
    [85, 3, 80, 75],
    [60, 1, 50, 40],
    [90, 4, 90, 85],
    [70, 2, 60, 65],
    [95, 5, 95, 90]
])

y = np.array([70, 85, 55, 95, 65, 98])

model = LinearRegression()
model.fit(X, y)

def predict(attendance, study_hours, marks, assignments):
    return model.predict([[attendance, study_hours, marks, assignments]])[0]