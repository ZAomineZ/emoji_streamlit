# Streamlit Emoji Shortcode Explorer

![Streamlit Emoji Shortcode Explorer](https://img.shields.io/badge/Streamlit-Emoji%20Explorer-brightgreen)

## Overview

The **Streamlit Emoji Shortcode Explorer** is a fun and interactive web app built using [Streamlit](https://streamlit.io/). It allows users to:

- Browse and search emojis by their ASCII shortcodes.
- Explore special emojis like Streamlit's own `:streamlit:` emoji.
- Download the emoji data as a JSON file for offline use.

This app is perfect for developers, designers, and emoji enthusiasts looking to integrate emojis into their projects effortlessly.

---

## Features

- **Dynamic Emoji Search**: Search emojis by shortcode or symbol.
- **Pagination**: Adjust the number of rows displayed per page for easier navigation.
- **Emoji Export**: Download all emoji data as a JSON file.
- **Real-Time Updates**: Dynamic interaction powered by Streamlit.



## Usage

1. **Search Emojis**:
   - Use the search bar to filter emojis by their shortcodes (e.g., `:smile:`) or symbols (e.g., 😊).

2. **Adjust Rows Per Page**:
   - Use the input box to specify how many rows of emojis to display per page.

3. **Export Emoji Data**:
   - Click the **Download emojis as JSON** button to export all emoji data for offline use.

---

## Project Structure

```
.
├── app.py               # Main application file
├── requirements.txt     # Dependencies
└── README.md            # Project documentation
```

## License

This project is licensed under the [MIT License](LICENSE).

---

## Acknowledgments

- Emoji data sourced from the [omnidan/node-emoji](https://github.com/omnidan/node-emoji) repository.
- Built with ❤️ using [Streamlit](https://streamlit.io/).