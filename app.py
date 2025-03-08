
import streamlit as st

# Set page config
st.set_page_config(page_title="My Portfolio", page_icon=":guardsman:", layout="wide")

# Header
st.title("Welcome to My Portfolio!")

# Navigation for Projects
page = st.selectbox(
    "Select a Project",
    ["Home", "Project 1: Data Analysis", "Project 2: Web App with Flask", "Project 3: Machine Learning"]
)

# Home Page Content
if page == "Home":
    st.header("About Me")
    st.write("""
    Hello! I'm a passionate developer with expertise in Python, Data Science, Web Development, and Machine Learning. Below are some of the projects I've worked on:
    """)

    st.image("images/profile_picture.png", caption="That's me!", width=200)

# Project 1: Data Analysis Page
elif page == "Project 1: Data Analysis":
    st.header("Project 1: Data Analysis with Python")
    st.write("""
    In this project, I used Python and libraries like Pandas and Matplotlib to analyze and visualize a dataset.
    The goal was to extract meaningful insights and create visual representations of the data.
    """)

    # Sample Code for Project 1
    code = '''import pandas as pd
import matplotlib.pyplot as plt

# Load Data
data = pd.read_csv('dataset.csv')

# Simple analysis
summary = data.describe()
print(summary)

# Visualize data
data.plot(kind='line', x='Date', y='Value')
plt.show()
'''
    st.subheader("Sample Code for Data Analysis")
    st.code(code, language='python')

    # Display project image (you can add an image of your analysis here)
    st.image("images/project1_analysis.png", caption="Data Analysis Visualization", width=600)

# Project 2: Web App with Flask Page
elif page == "Project 2: Web App with Flask":
    st.header("Project 2: Full-Stack Web App with Flask")
    st.write("""
    This is a full-stack web application built using Flask, HTML, CSS, and JavaScript. The app is designed to manage user data and display dynamic content.
    I implemented routing, templates, and a simple backend with Flask.
    """)

    # Sample Code for Project 2
    code = '''from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
'''
    st.subheader("Sample Code for Flask Web App")
    st.code(code, language='python')

    # Display project image (show a screenshot of your app here)
    st.image("images/project2_flask.png", caption="Flask Web App Screenshot", width=600)

# Project 3: Machine Learning Page
elif page == "Project 3: Machine Learning":
    st.header("Project 3: Machine Learning Model")
    st.write("""
    In this project, I built a machine learning model to predict housing prices. I used scikit-learn and trained the model using a dataset of historical housing prices.
    The model was then evaluated on various metrics to ensure its accuracy.
    """)

    # Sample Code for Project 3
    code = '''from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# Load dataset
data = pd.read_csv('housing.csv')

# Features and target
X = data[['Size', 'Rooms', 'Location']]
y = data['Price']

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Model training
model = LinearRegression()
model.fit(X_train, y_train)

# Model evaluation
print(f'Accuracy: {model.score(X_test, y_test)}')
'''
    st.subheader("Sample Code for Machine Learning Model")
    st.code(code, language='python')

    # Display project image (show a model evaluation graph or dataset)
    st.image("images/project3_ml.png", caption="Model Accuracy Graph", width=600)
