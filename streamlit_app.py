import streamlit
streamlit.title('My MOms  healthy diner')
streamlit.header('Breakfast menu')
streamlit.text('🥣 Omega 3  & blueberry oatmeal')
streamlit.text('🥗 kale,spinach & rocket smoothe')
streamlit.text('🐔 hard-boiled free-range egg') 
streamlit.text (' 🥑🍞 Avacado toast')  
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')
import pandas
my_fruit_list= pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)
# Let's put a pick list here so they can pick the fruit they want to include 
streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index))
