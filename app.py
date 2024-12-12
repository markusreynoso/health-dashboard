"""Imports"""

import pandas as pd
from dash import Dash, html, dcc, Input, Output 
import plotly.express as px
import plotly.graph_objects as go

""" Variables"""

df = pd.read_csv("https://raw.githubusercontent.com/markusreynoso/dashboard-datasets/refs/heads/main/Life%20Expectancy/Life%20Expectancy%20Data.csv")