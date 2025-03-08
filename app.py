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
    Objective: Designed to provide readily accessible game information, link game achievements to Discord profiles, facilitate moderation, and serve as an AI chatbot to enhance user engagement within the Soul Knight Prequel Discord community.\n
    Duration: A comprehensive project spanning approximately 2-3 years, with continuous updates and improvements post-deployment.\n
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
    - Limited Server Access: The hosting server lacked administrative privileges, necessitating reliance on external APIs and modules to perform tasks requiring root access.
    - Scalability Concerns: Ensured the bot could handle the growing user base, implementing optimizations to maintain performance.
    - User Engagement: Continuously updated the bot's features based on user feedback to enhance engagement and satisfaction.

    You can join the Discord server using this link: https://discord.gg/soulknightprequel \n

    Since the bot was deployed on one server, I could closely monitor user interactions and gather feedback more easily. This allowed me to tailor features to the specific needs of the community. As the user base grew, the focus shifted toward optimizing performance, ensuring the bot was responsive even with an increasing number of commands and interactions. Continuous testing and improvements were crucial to maintaining smooth operations.\n\n
    Having the bot in a single server meant I could engage with the community more directly. Feedback and suggestions from users could be integrated more quickly, helping refine the bot's features. The close-knit nature of the community allowed for faster iteration and adjustments, whether it was for new game information, achievements, or chatbot interactions. The challenge was ensuring that changes made to accommodate a growing user base didn't disrupt the established experience for long-time members.\n\n
    Despite not having administrative access to the server, I had to be resourceful with the tools available. Using external APIs and modules for certain tasks required creative problem-solving, especially since I couldn’t implement more advanced solutions that needed server-level permissions. This pushed me to think outside the box and find workarounds that would allow the bot to function optimally without compromising its capabilities.\n\n
    With only one server to focus on, I could more easily monitor performance and reliability. However, as the user base grew, I needed to ensure that the bot continued to run smoothly without overwhelming the server resources. This highlighted the importance of load balancing, efficient coding practices, and proactive error handling.\n\n
    The project allowed me to build meaningful relationships with the community, offering valuable learning experiences about user expectations and how to foster engagement over time. Interacting with a dedicated group of users helped me improve the bot's functionality while also contributing to a stronger sense of community within the server. This experience taught me the importance of maintaining open communication channels and transparency with users.\n\n
    By working within one server, I delivered a highly personalized and optimized experience, which was a key takeaway from this project.\n\n
    I would upload the code here but there are too many files due to it being built modularly
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
