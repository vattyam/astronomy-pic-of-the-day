import requests
import streamlit as st

url = ("https://api.nasa.gov/planetary/apod?api_key=mqbQmvoOBmJdX4X7JuSBSjjGNMQIxuRNiXuIi1mw")

request = requests.get(url)
content = request.json()
print(content)

title = content['title']
image_url = content['url']
description = content['explanation']

image_response = requests.get(image_url)
with open("astronomy-image.png", "wb") as file:
    file.write(image_response.content)

st.set_page_config(layout='wide')
st.title(title)
st.image("astronomy-image.png")
st.write(description)

