import streamlit as st
from datetime import datetime as dt
import datetime


st.title("Hello! It's my webpage")

button=st.button("press the button")
if button:
    st.write(':blue[success] :sparkles: ')

agree=st.checkbox("do you know what is your mbti type?")
if agree:
    st.write("you are smart!:sparkles:")

mbti=st.selectbox(
    'what is your mbti ?',
    ('isfp','estp','cute')
)
if mbti=='isfp':
    st.write('오 :blue[저랑] 똑같으십니다 ㅎ ㅇ')
elif mbti=='estp':
    st.write('you have the same mbti as Trumph')
elif mbti=='cute':
    st.write('^_&')




st.header("Let's have a meeting")

start_time=st.slider(
    'when do you have a time?',
    min_value=dt(2024,2,1,0,0),
    max_value=dt(2024,2,7,12,0),
    value=dt(2024,2,6,5,1),
    step=datetime.timedelta(hours=1),
    format='MM/DD/YY - HH:mm')
st.write("is it correct?: ",start_time)




