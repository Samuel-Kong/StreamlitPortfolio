import streamlit as st

# Set page config
st.set_page_config(page_title="My Portfolio", page_icon=":guardsman:", layout="wide")

# Sidebar Navigation with Buttons
st.sidebar.title("Portfolio Navigation")

# Create buttons for navigation
home_button = st.sidebar.button("Home")
project1_button = st.sidebar.button("Project 1: Data Analysis")
project2_button = st.sidebar.button("Project 2: Web App with Flask")
project3_button = st.sidebar.button("Project 3: Machine Learning")

# Default page is "Home"
page = "Home"

# Check which button was clicked
if home_button:
    page = "Home"
elif project1_button:
    page = "Project 1: Data Analysis"
elif project2_button:
    page = "Project 2: Web App with Flask"
elif project3_button:
    page = "Project 3: Machine Learning"

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

# Project 1: Data Analysis Page (Blank for now)
elif page == "Project 1: Data Analysis":
    st.header("Project 1: Data Analysis with Python")
    st.write("""
    This section will be dedicated to a project involving data analysis using Python, Pandas, and Matplotlib.
    (Content for this project will be added later.)
    """)

# Project 2: Web App with Flask Page (Blank for now)
elif page == "Project 2: Web App with Flask":
    st.header("Project 2: Full-Stack Web App with Flask")
    st.write("""
    This section will showcase a full-stack web application built using Flask, HTML, CSS, and JavaScript.
    (Content for this project will be added later.)
    """)

# Project 3: Machine Learning Page (Blank for now)
elif page == "Project 3: Machine Learning":
    st.header("Project 3: Machine Learning Model")
    st.write("""
    This section will cover a machine learning model built to predict housing prices using scikit-learn.
    (Content for this project will be added later.)
    """)
