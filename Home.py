import streamlit as st
# import pandas as pd
# import numpy as np
from PIL import Image

st.set_page_config(
    page_title="Hello",
    page_icon="👋",
    # layout="wide"
)

st.write("Create Knowledge Base")
uploaded_files = st.file_uploader("Upload Document", accept_multiple_files=True, type=("pdf", "txt", "csv", 'json', 'docx', 'xlsx'))
# uploaded_files = st.file_uploader("Choose a CSV file", accept_multiple_files=True)
for uploaded_file in uploaded_files:
    bytes_data = uploaded_file.read()
    st.write("filename:", uploaded_file.name)
    st.write(bytes_data)

st.markdown("---")
web_url_name = ['Web URL', 'Webhook', 'Google Sheets', 'Google Slides', 'Google Docs', 'ElasticSearch']
web_url_image = ['web_url.png', 'webhook.png', 'google_sheets.png', 'google_Slides.png', 'google_docs.png', 'elasticsearch.png']

row1 = st.columns(3)
row2 = st.columns(3)

for i, col in enumerate(row1 + row2):
    tile = col.container(height=120)
    text = 'Web URL'
    link = 'Web URL Link'
    # tile.markdown("Web URL")
    # tile.markdown(f"<div style='text-align:center'><a href='{link}'>{text}</a></div>", unsafe_allow_html=True)
    tile.markdown(web_url_name[i])
    # img = Image.open("web_url.png")
    img = Image.open(web_url_image[i])
    img_resized = img.resize((40, 40))
    tile.image(img_resized)
    # tile.image("web_url.png", use_column_width=True)
    # tile.title(":balloon:")





# def main():
#     # st.title("this is title")
#     # st.header("this is header")
    
#     # Navbar
#     # nav_option = st.sidebar.radio("Navigation", ["Home", "About", "Contact"])

#     # with st.sidebar:
#     #     selected = option_menu("Main Menu", ["Home", 'Settings'], 
#     #         icons=['house', 'gear'], menu_icon="cast", default_index=0)
#     #     nav_option = selected
    
#     # if nav_option == "Home":
#     #     show_home_page()
#     # elif nav_option == "About":
#     #     show_about_page()
#     # elif nav_option == "Contact":
#     #     show_contact_page()
        
#     # Footer
#     st.markdown("---")
#     # st.markdown("this is markdown")

# def show_home_page():
#     st.write("Create Knowledge Base")
#     uploaded_file = st.file_uploader("Upload Document", type=("txt", "md"))

# def show_about_page():
#     st.write("This is the About Page. Learn more about us here.")

# def show_contact_page():
#     st.write("This is the Contact Page. Contact us at contact@example.com.")

# if __name__ == "__main__":
#     main()













# DATE_COLUMN = 'date/time'
# DATA_URL = ('https://s3-us-west-2.amazonaws.com/'
#          'streamlit-demo-data/uber-raw-data-sep14.csv.gz')

# st.sidebar.success("Select a demo above.")

# def load_data(nrows):
#     data = pd.read_csv(DATA_URL, nrows=nrows)
#     lowercase = lambda x: str(x).lower()
#     data.rename(lowercase, axis='columns', inplace=True)
#     data[DATE_COLUMN] = pd.to_datetime(data[DATE_COLUMN])
#     return data

# # Create a text element and let the reader know the data is loading.
# data_load_state = st.text('Loading data...')
# # Load 10,000 rows of data into the dataframe.
# data = load_data(10000)
# # Notify the reader that the data was successfully loaded.
# data_load_state.text('Loading data...done!')
