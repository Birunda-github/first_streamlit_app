
import streamlit as st
import pandas as p

my_fruit_list=p.read_csv('https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt')
#setting fruit_name as index for widget
my_fruit_list=my_fruit_list.set_index('Fruit')

st.title('My Mom\'s New Healthy Diner')

st.header('Breakfast Favorites')
st.text('🥣 Omega 3 & Blueberry Oatmeal')
st.text('🥗 Kale, Spinach & Rocket Smoothie')
st.text('🐔 Hard-Boiled Free-Range Egg')
st.text('🥑🍞 Avocado Toast')

st.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

#let's put a pick list here so that the user can pick fruit they want for smoothie
st.multiselect('pick some fruits',list(my_fruit_list.index),['Avocada','Strawberries'])

st.dataframe(my_fruit_list)



