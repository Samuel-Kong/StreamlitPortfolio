import streamlit as st


st.set_page_config(page_title="My Portfolio", page_icon="💻", layout="wide")


if "page" not in st.session_state:
    st.session_state.page = "Home"


st.sidebar.title("Portfolio Navigation")


home_button = st.sidebar.button("Home")
projects_button = st.sidebar.button("Projects")


if home_button:
    st.session_state.page = "Home"
elif projects_button:
    st.session_state.page = "Projects"


st.title("Welcome to My Portfolio!")


if st.session_state.page == "Home":
    st.header("About Me")
    st.write("""
    Hello! I'm Kong Le Xin Samuel, a passionate developer with expertise in Python, cybersecurity, data manipulation, and machine learning. I take photographs, read manga, watch anime, and play games like Minecraft and CoDM in my free time.
    \n
    Connect with me on Discord! Username: `entity8o8`\n
    Send me an email at konglexinsamuel@gmail.com
    """)

    st.image("images/306_SamuelKong.png", caption="That's me!", width=200)


elif st.session_state.page == "Projects":
    st.header("My Projects")
    st.write("""
    Here are some of the exciting projects I've worked on. Click on a project to learn more!
    """)


    project1_button = st.button("Project 1: Soul Knight Prequel Discord Bot")
    project2_button = st.button("Project 2: Portfolio Website")


    if project1_button:
        st.session_state.page = "Project 1: Soul Knight Prequel Discord Bot"
    if project2_button:
        st.session_state.page = "Project 2: Portfolio Website"

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
elif st.session_state.page == "Project 2: Portfolio Website":
    st.header("Project 1: Development of a Portfolio Website using Streamlit")
    st.write("""
    Objective: To make a website that allows people to view my projects\n
    Duration: Around 10 minutes\n
    Tools Used:
    - Python
    - Streamlit
    - Streamlit Cloud (For hosting)
    - Github (To store code)
    Features:
    - Images display
    - Projects display

    I started by outlining the structure of my portfolio. I wanted it to be simple yet informative, with sections dedicated to who I am, my skills, and my projects. The projects section was a critical part of the design, as I wanted it to showcase my work clearly and concisely. I included buttons that would take users to different pages for each project to keep everything clean and prevent information overload.\n
    I chose **Streamlit** for this project because it's an easy and fast way to create interactive web applications, particularly useful for data science and personal projects. While not traditionally used for building complex websites, Streamlit is great for a personal portfolio site when you want to showcase specific projects or technical skills. It allowed me to quickly create the necessary functionality for navigation and content display with minimal effort.\n
    One of the challenges I faced was handling page navigation. I initially had issues with buttons redirecting to the wrong pages, often returning me to the home page instead of the project pages. This was because Streamlit's built-in widgets like `st.button()` don’t naturally retain state across interactions. To fix this, I utilized `st.session_state`, which allowed me to preserve the current page and improve navigation.\n
    The process of debugging and implementing state management was a valuable learning experience. I was forced to think about how to handle different states across multiple pages, something that is crucial in building any dynamic website.\n
    I focused on creating a clean and minimalistic design. Streamlit offers flexibility in layout, but I wanted to avoid making the site overly complex. I added a sidebar to make the site easier to navigate, as it allowed me to keep the main content area focused on the current project or information. This layout also makes the website feel organized and user-friendly.
    \n
    For the actual content, I included descriptions, images, and code snippets that could convey the essence of each project. This balance between technical details and visual appeal was key to creating a portfolio that was both informative and visually appealing.
    \n
    Building this portfolio website was a fulfilling project that allowed me to showcase my skills and reflect on the technical journey I’ve been on. It reinforced my understanding of web development while also serving as a personal project I can continue to improve over time. This portfolio will serve as both a tool for future job applications and a reminder of the progress I’ve made as a developer.\n
    You can see the code here: https://github.com/Samuel-Kong/StreamlitPortfolio
    """)
    
    

