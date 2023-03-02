#Importing required libraries
import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image
import plotly.express as px
import os
import seaborn as sns


#absolute path to this file
FILE_DIR = os.path.dirname(os.path.abspath(__file__))

#absolute path to this file's root directory
PARENT_DIR = os.path.join(FILE_DIR, os.pardir)

#absolute path of directory_of_interest
dir_of_interest = os.path.join(PARENT_DIR, 'resources')

#Loading Dataset
df = sns.load_dataset("tips")

#Display title
st.title(":red[Dashboard] - EDA On Tips Dataset")

#Display DataFrame
st.markdown("**:blue[Dataset:]** ")
st.dataframe(df)

#Basic info about the dataset
st.write(":blue[**Basic statistics about the data**]")
st.write(df.describe().T)

#Correlation
st.write(":blue[**Correlation of the dataset**]")
corr_matrix = df.corr()

# Add color scale and axis labels
fig = px.imshow(corr_matrix, text_auto=True, width=800, height=600)

fig.update_layout(
    title="Correlation Matrix",
    xaxis_title="Features",
    yaxis_title="Features",
    coloraxis=dict(colorscale="Bluered_r"))

#Show plot in streamlit
st.plotly_chart(fig)

#Line plot for Total bill and Tip
tip_plot = px.scatter(data_frame=df, x='total_bill', y='tip', title="Line plot for total bill Vs tip")

#Tips for A Vs Dinner
fig = px.scatter(df , x='time', y='total_bill',color='sex',
                                    title = "Scatter plot on time Vs total bill for male and female")

#Display figure
st.plotly_chart(fig)

#Barplot for total bill Vs Meal time
time = st.selectbox("Select the time:", df['time'].unique())
col1, col2 = st.columns(2)

fig_1 = px.histogram(df[df['time'] == time], x="total_bill")
col1.plotly_chart(fig_1, use_container_width=True)

fig_2 = px.box(df[df['time']==time], x="total_bill")
col2.plotly_chart(fig_2, use_container_width=True)

#Higher tip paid by person is he/she smoker or not
fig = px.scatter(
    data_frame=df, 
    x='total_bill', 
    y='tip',
    color=df['smoker'] ,color_discrete_sequence=px.colors.qualitative.Set2,
    title = "Higest tip paid customer is smoker or not")

#Display figure
st.plotly_chart(fig)

#Scatter plot for Crowded Days with respect to time
fig = px.scatter(
    data_frame=df,
    x='day', y='tip',
    color=df['time'], color_discrete_sequence=px.colors.qualitative.Set2,
    title="Crowded Days with respect to time")

#Display figure
st.plotly_chart(fig)

#Pie chart for tips paid by male and female
fig = px.pie(data_frame=df, names='sex', values='tip',
                                     title="Camparision between tips given by Male Vs Female")

#Display figure
st.plotly_chart(fig)

#---------------------------------------------------Done--------------------------------------------------




