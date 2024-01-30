import streamlit
streamlit.title('My parents new Healthy Dinner')

streamlit.header('Breakfast Favorites')
streamlit.text('🥣 Omega 3 eggs and Blueberry Oatmeal')
streamlit.text('🥗 Kale, Spinach, and Rocket Smoothie')
streamlit.text('🐔 Hard-Boiled Free Range egg')
streamlit.text('🥑🍞 Avocado Toast')
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")

my_fruit_list = my_fruit_list.set_index('Fruit')

fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','Strawberries'])

fruits_to_show = my_fruit_list.loc[fruits_selected]

# Display the table on the page.
streamlit.dataframe(fruits_to_show)

#New section for FruityVice
streamlit.header("Fruityvice Fruit Advice!")

import requests

fruityvice_response = requests.get("https://fruityvice.com/api/fruit/watermelon")

#streamlit.text(fruityvice_response.json())

# normalize json output
fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())

# write to the screen
streamlit.dataframe(fruityvice_normalized)

