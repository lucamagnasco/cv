import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
from streamlit_timeline import timeline
import plotly.express as px
import plotly.figure_factory as ff
import requests
import re
import io
import matplotlib.pyplot as plt
import streamlit.components.v1 as components


# To add any element (be it a button or some text) on the left pane, this can very easily be embedded using streamlit.sidebar.feature_name
st.sidebar.caption('Wish to connect?')
st.sidebar.write('📧: luca.magnasco@gmail.com')
pdfFileObj = open('abc.pdf', 'rb')
st.sidebar.download_button('text_to_display',pdfFileObj,file_name='abc.pdf',mime='pdf')


#The download resume button is a special type of button

#todo: https://medium.com/data-science-in-your-pocket/building-portfolio-using-streamlit-ac215b8e74da
# completar