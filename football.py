import streamlit as st

# Replace with your data source (list or dictionary)
highlights = [
    {"date": "2023-10-26", "teams": "Man United vs Liverpool", "title": "Salah's Wonder Strike", "video_url": "https://example.com/video1.mp4"},
    {"date": "2023-11-12", "teams": "Barcelona vs Real Madrid", "title": "Messi Magic", "video_url": "https://example.com/video2.mp4"},
]

# Title and Introduction
st.title("Football Highlights")
st.write("Catch up on all the latest action from the world of football!")

# Sidebar for filtering (optional)
selected_date = st.sidebar.selectbox("Filter by Date", [h["date"] for h in highlights])
filtered_highlights = [h for h in highlights if h["date"] == selected_date]

# Display Highlights
for highlight in filtered_highlights:
    st.header(f"{highlight['date']} - {highlight['teams']}")
    st.subheader(highlight["title"])
    st.video(highlight["video_url"])

