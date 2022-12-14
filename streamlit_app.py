
import streamlit

import pandas

import requests

import snowflake.connector

from urllib.error import URLError


streamlit.title('My Parents New Healthy Diner')
streamlit.header('Breakfast Menu')
streamlit.text('π₯£ Omega 3 & Blueberry Meal')
streamlit.text('π₯ Kale, Spinach, Rocket Smoothie')
streamlit.text('πHalf-Boiled Free-Range Egg')
streamlit.text('π₯π Avacado Toast')


streamlit.header('ππ₯­ Build Your Own Fruit Smoothie π₯π')

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')

fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado', 'Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]
streamlit.dataframe(my_fruit_list)
streamlit.header("Fruityvice Fruit Advice!")
try:
fruit_choice = streamlit.text_input('What fruit would you like information about?','Kiwi')
if not fruit_choice:
  streamlit.error("Please selet a fruit to get information")
 else:
#streamlit.write('The user entered ', fruit_choice)
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" +fruit_choice)
#upload the json file to normalize dataset using Python Pandas library function as below 
fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
#display the normalized output as table
streamlit.dataframe(fruityvice_normalized)


except URLError as e:
  streamlit.error()


