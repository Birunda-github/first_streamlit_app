
import streamlit as st
import pandas as p
import requests
import snowflake.connector
from urllib.error import URLError

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
fruit_selected=st.multiselect('pick some fruits',list(my_fruit_list.index),
               ['Avocado','Strawberries'])
fruits_to_show=my_fruit_list.loc[fruit_selected]

#st.dataframe(my_fruit_list)
st.dataframe(fruits_to_show)

#new section to display api response

# create a function for fruit_choice
def get_fruityvice_data(this_fruity_choice):
  fruityvice_response=requests.get('https://fruityvice.com/api/fruit/'+fruit_choice)
  fruityvice_normalize=p.json_normalize(fruityvice_response.json())
  return fruityvice_normalize

st.header('Fruityvice fruit advice!')
try:
  fruit_choice=st.text_input('What fruit would you like information about?')
  if not fruit_choice:
    st.error('please select a fruit to get information')
  else:
    back_from_function=get_fruityvice_data(fruit_choice)
    st.dataframe(back_from_function)
except URLError as e:
  st.error()

#don't run anything past when we troubleshoot
st.stop()

#conecting to snowflake

#returns only one value
#my_data_row = my_cur.fetchone()

st.header("The Fruit List contains:")
#snowflake function

def get_fruit_load_list():
  with my_cnx.cursor() as my_cur:
    my_cur.execute("select * from fruit_load_list")
    return my_cur.fetchall()
#add a button to load fruit
if st.button('Get Fruit Load list'):
  my_cnx=snowflake.connector.connect(**st.secrets["snowflake"])
  my_data_rows=get_fruit_load_list()
  st.dataframe(my_data_rows)

# add_my_fruit=st.text_input('What would you like to choose?','Mango')
# st.write('Thanks for adding ',add_my_fruit)


#my_cur.execute("insert into pc_rivery_db.public.fruit_load_list values('from streamlit')")

