import streamlit as st

highlights = [
    {"premier league": "https://www.youtube.com/results?search_query=highlights"},
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

