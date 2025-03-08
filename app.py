import streamlit as st

# Set page config
st.set_page_config(page_title="My Portfolio", page_icon=":guardsman:", layout="wide")

# Sidebar Navigation with Buttons
st.sidebar.title("Portfolio Navigation")

# Create buttons for navigation
home_button = st.sidebar.button("Home")
projects_button = st.sidebar.button("Projects")

# Default page is "Home"
page = "Home"

# Check which button was clicked
if home_button:
    page = "Home"
elif projects_button:
    page = "Projects"

# Header for Portfolio
st.title("Welcome to My Portfolio!")

# Home Page Content
if page == "Home":
    st.header("About Me")
    st.write("""
    Hello! I'm a passionate developer with expertise in Python, cybersecurity, data manipulation, and machine learning.
    Below are some of the projects I've worked on:
    """)

    st.image("images/306_SamuelKong.png", caption="That's me!", width=200)

# Projects Page: List all projects with brief summaries and buttons to each project
elif page == "Projects":
    st.header("My Projects")
    st.write("""
    Here are some of the exciting projects I've worked on. Click on a project to learn more!
    """)

    # Buttons for individual projects
    project1_button = st.button("Project 1: Data Analysis")
    project2_button = st.button("Project 2: Web App with Flask")
    project3_button = st.button("Project 3: Machine Learning")

    # Project 1: Data Analysis Brief Summary
    if project1_button:
        st.write("""
        **Project 1: Data Analysis with Python**
        - This project involves using Python, Pandas, and Matplotlib to analyze and visualize data.
        - Extracting meaningful insights and creating visual representations of the data.
        (Click below for more details on the Data Analysis project.)
        """)
        st.button("Go to Data Analysis Project")

    # Project 2: Web App with Flask Brief Summary
    if project2_button:
        st.write("""
        **Project 2: Full-Stack Web App with Flask**
        - A web app built with Flask, HTML, CSS, and JavaScript to manage user data.
        - The app interacts with a backend to display dynamic content.
        (Click below for more details on the Flask Web App project.)
        """)
        st.button("Go to Web App with Flask Project")

    # Project 3: Machine Learning Brief Summary
    if project3_button:
        st.write("""
        **Project 3: Machine Learning Model**
        - Built a machine learning model to predict housing prices using scikit-learn.
        - Evaluating the model with accuracy metrics and predicting housing prices based on input features.
        (Click below for more details on the Machine Learning project.)
        """)
        st.button("Go to Machine Learning Project")

# Project 1: Data Analysis Page (Detailed Information)
elif page == "Project 1: Data Analysis":
    st.header("Project 1: Data Analysis with Python")
    st.write("""
    This project involves using Python and libraries like Pandas and Matplotlib to analyze and visualize a dataset.
    The goal was to extract meaningful insights from the dataset and create visual representations of the data.

    Tools used:
    - Pandas for data manipulation.
    - Matplotlib for data visualization.
    """)

    # Sample code for Project 1
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

    # Add an image or plot related to the project
    st.image("images/project1_analysis.png", caption="Data Analysis Visualization", width=600)

# Project 2: Web App with Flask Page (Detailed Information)
elif page == "Project 2: Web App with Flask":
    st.header("Project 2: Full-Stack Web App with Flask")
    st.write("""
    This full-stack web application was built using Flask, HTML, CSS, and JavaScript.
    It showcases dynamic content management and backend integration for user data.

    Tools used:
    - Flask for backend routing.
    - HTML, CSS, JavaScript for frontend.
    """)

    # Sample code for Project 2
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

    # Add a screenshot of the app
    st.image("images/project2_flask.png", caption="Flask Web App Screenshot", width=600)

# Project 3: Machine Learning Page (Detailed Information)
elif page == "Project 3: Machine Learning":
    st.header("Project 3: Machine Learning Model")
    st.write("""
    In this project, I created a machine learning model to predict housing prices using scikit-learn.
    I evaluated the model based on various metrics like R-squared and Mean Absolute Error.

    Tools used:
    - scikit-learn for machine learning algorithms.
    - Pandas for data manipulation.
    """)

    # Sample code for Project 3
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

    # Add an image or plot related to the project
    st.image("images/project3_ml.png", caption="Model Accuracy Graph", width=600)
