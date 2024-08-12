import streamlit as st
import wikipediaapi

# Initialize the Wikipedia API with a proper user agent
wiki_wiki = wikipediaapi.Wikipedia(
    language='en',
    user_agent='streamlit_wikisearch/1.0 (https://yourwebsite.com; your.email@example.com)'
)

# Streamlit app title
st.title("Wikipedia Search App")

# Input box for the user to enter the topic they want to search for
search_term = st.text_input("Enter a Wikipedia topic to search for:")

# When the user inputs a topic, search for it on Wikipedia
if search_term:
    # Get the Wikipedia page for the search term
    page = wiki_wiki.page(search_term)

    # Check if the page exists
    if page.exists():
        # Display the title and summary of the page
        st.header(page.title)
        st.write(page.summary)

        # Optionally, display the entire content of the page
        if st.checkbox("Show full content"):
            st.write(page.text)
    else:
        st.warning(f"No Wikipedia page found for '{search_term}'")

# Provide a brief about the app functionality
st.sidebar.header("About this App")
st.sidebar.info("This app allows you to search for information available on Wikipedia and display the summary or full content of the page.")
