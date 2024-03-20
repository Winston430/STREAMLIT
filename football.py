import streamlit as st

# Define highlight data (replace with your actual data)
highlights = [
    {"league": "Premier League", "video_url": "https://www.youtube.com/results?search_query=premier+league+highlights"},
    {"league": "La Liga", "video_url": "https://www.youtube.com/results?search_query=laliga+highlights"},
    {"league": "Serie A", "video_url": "https://www.youtube.com/results?search_query=serie+A+highlights"},
]

# Create the menu using st.radio
selected_league = st.radio("Select League", ["Premier League", "La Liga", "Serie A"])

# Filter highlights based on selection
filtered_highlights = [h for h in highlights if h["league"] == selected_league]

# Display Highlights based on selection
if filtered_highlights:
    st.header(f"Highlights from {selected_league}")
    for highlight in filtered_highlights:
        st.header(f"{highlight['date']} - {highlight['teams']}")
        st.subheader(highlight["title"])
        st.video(highlight["video_url"])
else:
    st.write(f"No highlights available for {selected_league}.")

