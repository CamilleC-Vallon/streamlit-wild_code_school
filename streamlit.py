# -*- coding: utf-8 -*-

import pandas as pd 
import matplotlib.pyplot as plt 
import numpy as np

df = pd.read_csv('https://raw.githubusercontent.com/murpi/wilddata/master/quests/cars.csv', sep=',')

import streamlit as st

st.title('Hello Wilders, welcome to my application!')

st.write("I enjoy to discover stremalit possibilities")

st.line_chart(df['YEAR'])

import seaborn as sns
viz_correlation = sns.heatmap(df.corr(), 
								center=0,
								cmap = sns.color_palette("vlag", as_cmap=True)
								)

st.pyplot(viz_correlation.figure)

name = st.text_input("Please give me your name :")
name_length = len(name)
st.write("Your name has ",name_length,"characters")

