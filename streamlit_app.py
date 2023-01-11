import snowflake.connector
import streamlit
import pandas
import requests
from urllib.error import URLError


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
# streamlit.text(fruityvice_response.json())

def get_fruityvice_data(this_fruit_choice):
  fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice)
  #take the json version of data and normalize it
  fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
  return fruityvice_normalized

  

try:
  fruit_choice = streamlit.text_input('What fruit would you like information about?')
  if not fruit_choice:
    streamlit.error("Please select a fruit to get information.")
  else:
    back_from_function = get_fruityvice_data(fruit_choice)
    # Display the table on the page.
    streamlit.dataframe(back_from_function)
    
    
except URLError as e:
  streamlit.error();
    

   



# add_my_fruit = streamlit.text_input('What fruit would you like to add ?')
# streamlit.write('Thanks for adding', add_my_fruit)

# my_cur.execute("insert into fruit_load_list values()")

streamlit.header ("The fruit load list contains:")
 #Snowflake-related functions
 def get_fruit_load_list():
     with my_cnx.cursor () as my_cur:
          my_cur.execute("select * from fruit_load_list")
          return my_cur.fetchall()
 # Add a button to load the fruit
 if streamlit.button('Get Fruit Load List'):
     my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
     my_data_rows = get_fruit_load_list()
     streamlit.dataframe(my_data_rows)



