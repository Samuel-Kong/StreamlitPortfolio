import streamlit as st

# Set page config
st.set_page_config(page_title="My Portfolio", page_icon=":guardsman:", layout="wide")

# Check if session state already has a page set
if "page" not in st.session_state:
    st.session_state.page = "Home"

# Sidebar Navigation with Buttons
st.sidebar.title("Portfolio Navigation")

# Create buttons for navigation
home_button = st.sidebar.button("Home")
projects_button = st.sidebar.button("Projects")

# Update page state based on button clicks
if home_button:
    st.session_state.page = "Home"
elif projects_button:
    st.session_state.page = "Projects"

# Header for Portfolio
st.title("Welcome to My Portfolio!")

# Home Page Content
if st.session_state.page == "Home":
    st.header("About Me")
    st.write("""
    Hello! I'm a passionate developer with expertise in Python, cybersecurity, data manipulation, and machine learning. I do phtography, read manga, watch anime and play games like Minecraft and CoDM in my free time.
    """)

    st.image("images/306_SamuelKong.png", caption="That's me!", width=200)

# Projects Page: List all projects with brief summaries and buttons to each project
elif st.session_state.page == "Projects":
    st.header("My Projects")
    st.write("""
    Here are some of the exciting projects I've worked on. Click on a project to learn more!
    """)

    # Buttons for individual projects
    project1_button = st.button("Project 1: Soul Knight Prequel Discord Bot")
    project2_button = st.button("Project 2: Web App with Flask")
    project3_button = st.button("Project 3: Machine Learning")

    # Navigate to Project 1 Page
    if project1_button:
        st.session_state.page = "Project 1: Soul Knight Prequel Discord Bot"

    # Navigate to Project 2 Page
    if project2_button:
        st.session_state.page = "Project 2: Web App with Flask"

    # Navigate to Project 3 Page
    if project3_button:
        st.session_state.page = "Project 3: Machine Learning"

# Project 1: Data Analysis Page (Detailed Information)
elif st.session_state.page == "Project 1: Soul Knight Prequel Discord Bot":
    st.header("Project 1: Development of a Disnake Discord Bot for a 60,000+ Member Soul Knight Prequel Community")
    st.write("""
    Objective: Designed to provide readily accessible game information, link game achievements to Discord profiles, facilitate moderation, and serve as an AI chatbot to enhance user engagement within the Soul Knight Prequel Discord community.
    Duration: A comprehensive project spanning approximately 2-3 years, with continuous updates and improvements post-deployment.
    Tools used:
    - Python: Utilized for backend development, leveraging the Disnake library for seamless Discord integration.
    - Disnake Library: Provided an async-ready API wrapper for Discord, facilitating efficient bot operations. 
    - DOCS.DISNAKE.DEV
    - Pillow: Employed for image processing tasks, enhancing visual content delivery.
    - Google Gemini API: Integrated to enrich bot functionalities with advanced AI capabilities.
    - JSON: Used for data storage and configuration, ensuring structured data management.
    - Sparked Hosting Service: Chosen for reliable hosting, supporting the bot's operational demands.
    - OCR Space: Incorporated for optical character recognition tasks, expanding the bot's utility.

    Features (including but not limited to):
    - Game Information Access: Provided users with up-to-date game details, guides, and news within the Discord server.
    - Achievement Linking: Enabled synchronization of in-game achievements with Discord profiles, fostering community recognition.
    - Moderation Tools: Developed features to assist moderators in maintaining community standards and managing user interactions.
    - AI Chatbot: Integrated an AI-driven chatbot to engage users in dynamic conversations and provide assistance.
    
    Challenges and Solutions:
    - Limited Server Access: Lacked administrative privileges on the hosting server, necessitating reliance on external APIs and modules to perform tasks requiring root access.
    - Scalability Concerns: Ensured the bot could handle the growing user base, implementing optimizations to maintain performance.
    - User Engagement: Continuously updated the bot's features based on user feedback to enhance engagement and satisfaction.



    From this project, I gained insights into project management, user-centred design, and the importance of community feedback in iterative development. I plan to introduce new features such as real-time game analytics, multilingual support, and deeper AI integrations to further enrich user experience.
    """)

# Project 2: Web App with Flask Page (Detailed Information)
elif st.session_state.page == "Project 2: Web App with Flask":
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
elif st.session_state.page == "Project 3: Machine Learning":
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
