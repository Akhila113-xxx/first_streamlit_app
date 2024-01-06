import streamlit
import pandas
import requests
import snowflake.connector

streamlit.title('My MOms  healthy diner')
streamlit.header('Breakfast menu')
streamlit.text('🥣 Omega 3  & blueberry oatmeal')
streamlit.text('🥗 kale,spinach & rocket smoothe')
streamlit.text('🐔 hard-boiled free-range egg') 
streamlit.text (' 🥑🍞 Avacado toast')  
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

my_fruit_list= pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list=my_fruit_list.set_index('Fruit')
# Let's put a pick list here so they can pick the fruit they want to include 
# let's put a pick list so they can pick the fruit they want to include
fruits_selected=streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','Strawberries'])
fruits_to_show=my_fruit_list.loc[fruits_selected]

# Display the table on the page.
streamlit.dataframe(fruits_to_show)



# New section to display fruity vice api responce
streamlit.header('Fruityvice Fruit Advice!')
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/watermelon")
fruityvice_normalized= pandas.json_normalize(fruityvice_response.json())
#output it as a table
streamlit.dataframe(fruityvice_normalized)
















