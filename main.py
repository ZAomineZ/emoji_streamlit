import streamlit as st
import requests
import pandas as pd

# API URL
API_URL = 'https://raw.githubusercontent.com/omnidan/node-emoji/master/lib/emoji.json'

@st.cache_data(ttl=60 * 60 * 12)
def fetch_emojis():
    """
    Fetch emojis from the API or fallback to local JSON in case of an error.
    """
    try:
        resp = requests.get(API_URL, timeout=10)
        resp.raise_for_status()  # Check for HTTP errors
        json_data = resp.json()
    except requests.exceptions.RequestException as e:
        st.error(f"Error fetching emoji data: {e}. Using fallback data.")
        with open("emoji_fallback.json", "r") as file:
            json_data = pd.read_json(file).to_dict()

    codes, emojis = zip(*json_data.items())
    return pd.DataFrame({
        'Emojis': emojis,
        'Shortcodes': [f':{code}:' for code in codes],
    })

# Load emojis
emojis = fetch_emojis()

# Title and introduction
st.title("Explore Emoji Shortcodes with Streamlit")
st.markdown("""
    🎉 **Welcome to the Emoji Shortcode Explorer!** 🎉

    This app allows you to browse and use emojis effortlessly by typing their ASCII shortcodes, such as `:smile:` for 😊.
    It’s a fun and efficient way to incorporate emojis into your projects or messages!

    **Features:**
    - Browse a searchable table of supported emoji shortcodes.
    - Use Unicode emojis directly in your Python strings if you prefer.
    - Discover special emojis, like Streamlit's very own `:streamlit:`!

    🚀 Start exploring and adding a touch of personality to your work with emojis!
""")

st.info("💡 **Tip**: For Streamlit 1.40.0 and later, try the exclusive Streamlit emoji: `:streamlit:` -> :streamlit:")

# Dynamic search
search_query = st.text_input("Search emojis by shortcode or symbol:", placeholder="E.g., smile, 😊")
if search_query:
    filtered_emojis = emojis[
        emojis['Shortcodes'].str.contains(search_query, case=False) |
        emojis['Emojis'].str.contains(search_query)
    ]
else:
    filtered_emojis = emojis

# Layout for rows per page and pagination
col1, col2 = st.columns([1, 3])
with col1:
    rows_per_page = st.number_input("Rows per page", min_value=1, max_value=100, value=20, step=1)

with col2:
    total_rows = len(filtered_emojis)
    page_number = st.number_input("Page number", min_value=1, max_value=(total_rows // rows_per_page) + 1, step=1)

# Pagination logic
start_idx = (page_number - 1) * rows_per_page
end_idx = start_idx + rows_per_page

# Display the table
st.table(filtered_emojis.iloc[start_idx:end_idx])

# Convert the DataFrame to JSON
emoji_json = emojis.to_json(orient="records", indent=4)
st.download_button(
    label="Download emojis as JSON",
    data=emoji_json,
    file_name="emoji_data.json",
    mime="application/json"
)
