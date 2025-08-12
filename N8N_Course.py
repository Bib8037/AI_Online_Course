import streamlit as st

# Set page config
st.set_page_config(
    page_title="AI Training : N8N Automation Workflow",
    page_icon="📚"
)

# Sidebar for page selection
st.sidebar.title("Navigation")
page = st.sidebar.radio(
    "Choose a page:",
    ["Home", "What is N8N?", "About us"]
)

# Main content based on page selection
if page == "Home":
    # Main title
    st.title("📚 Welcome to AI Learning Hub")
    st.divider()
    # Add poster image
    st.image("/Users/patsanansuksiri/Personal_Business/Poster - Master AI Today.png", use_container_width=True)


elif page == "What is N8N?":
    st.title("📖 What is N8N?")
    st.write("N8N is an open-source workflow automation tool that allows you to connect various apps and services.")
     # YouTube video URL
    youtube_url = "https://youtu.be/AEgtDv6jlTg?si=I6ao3E31hA2bB5NF"
    # Embed the video
    st.video(youtube_url)


elif page == "About us":
    st.title("ℹ️ About us")
    st.write("Information about the instructors (Kru Yim and Kru Bib).")
    
    # Display CV images
    st.image("/Users/patsanansuksiri/Personal_Business/CV_Bib_1.jpg", use_container_width=True)
    st.image("/Users/patsanansuksiri/Personal_Business/CV_Bib_2.jpg", use_container_width=True)

