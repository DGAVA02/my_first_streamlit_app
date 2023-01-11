import streamlit
import pandas
import requests

fruityvice_response = requests.get("https://fruityvice.com/api/fruit/watermelon")

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")

streamlit.title('My Parents new healthy Diner')

streamlit.header('Breakfast Menu')
streamlit.text('🥣    Omega3 and Blue Berry Oatmeal')
streamlit.text('🥗    Kale, spinach and Rocket smoothie')
streamlit.text('🐔    Hard Boiled Free-Range Egg')
streamlit.text('🥑🍞 Avacado Toast')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

# This Allows us to use names instead of numbers
my_fruit_list = my_fruit_list.set_index('Fruit')

# Let's put a pick list here so they can pick the fruit they want to include 
fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),(['Apple', 'Kiwifruit']))

fruits_to_show = my_fruit_list.loc[fruits_selected]

# Display the table on the page.

streamlit.dataframe(fruits_to_show)

streamlit.header("Fruityvice Fruit Advice!")
streamlit.text(fruityvice_response.json())





