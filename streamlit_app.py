
import streamlit as st
import numpy as np
from PIL import Image

st.write('MA 346 Final Project App - Carly Drischler')
st.title( 'Titanic Survival Probability' )
st.write()


st.sidebar.header('Select the inputs you wish to analyze:')

ticket_class = st.sidebar.selectbox('Choose: First, Second, or Third Class', ('First', 'Second', 'Third'))
st.sidebar.write('You selected:', ticket_class, ' class.')

if ticket_class == 'First':
    class_num = 1
if ticket_class == 'Second':
    class_num = 2
if ticket_class == 'Third':
    class_num = 3

gender = st.sidebar.selectbox('Choose: Male or Female', ('Male', 'Female'))
st.sidebar.write('You selected:', gender)

if gender == 'Female':
    is_fem = 1
if gender == 'Male':
    is_fem = 0

age = st.sidebar.slider('Select an age from 1 to 80:', min_value=1, max_value=80, value=21)
st.sidebar.write('You selected:', age, ' years old.')

survival_prob = (1 / (1 + np.exp(-(2.848 +  (-1.3842 * class_num) + (-0.0405 * age) + (2.4938 * is_fem))))) * 100
survival_prob = survival_prob.round(2)

st.write('According to my logistic regression model, a(n) ', age, 'year old ', gender, ' in ', ticket_class, ' Class had approximately a(n) ', survival_prob, '% chance of surviving the wreck of the Titanic.')

image = Image.open('Titanic.jpg')
st.image(image)