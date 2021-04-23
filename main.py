#!/usr/bin/env python

import pandas as pd
import os
from sodapy import Socrata
import numpy as np
import matplotlib
import cufflinks as cf
import plotly
import plotly.offline as py
import plotly.graph_objs as go
cf.go_offline()
py.init_notebook_mode()

# Unauthenticated client only works with public data sets. Note 'None'
# in place of application token, and no username or password:
# client = Socrata("data.cdc.gov", None)

# Example authenticated client (needed for non-public datasets):
client = Socrata("data.cdc.gov", os.environ["SOCRATA_APP_TOKEN"])

# First 2000 results, returned as JSON from API / converted to Python list of
# dictionaries by sodapy.
results = client.get("n8mc-b4w4", case_month="2020-02")

# Convert to pandas DataFrame
results_df = pd.DataFrame.from_records(results)

results_df.value_counts(subset=["res_state"]).plot(kind='bar')


results_df = pd.DataFrame.from_records(results)
case_by_county_df=pd.concat([results_df.res_county])

case_by_county_df

case_by_county_df.value_counts()

case_by_county_df.value_counts().iplot(kind="bar")

temp = pd.DataFrame({'case_by_county':case_by_county_df.value_counts()})

df = temp[temp.index != 'NA']

df = df.sort_values(by='case_by_county', ascending=True)
case_by_county = df
case_by_county

data  = go.Data([
            go.Bar(
              y = df.index,
              x = df.case_by_county,
              orientation='h'
        )])
layout = go.Layout(
        height = 1000,
        margin=go.Margin(l=300),
        title = "Cases by County"
)
fig  = go.Figure(data=data, layout=layout)
py.iplot(fig)

results_df.case_month = results_df.case_month

results_df.case_month.sort_values().index

df_by_date = results_df.iloc[results_df.case_month.sort_values().index]

df_by_date

case_by_date = df_by_date.groupby('case_month').case_month.count()
case_by_date.iplot(kind='scatter', title='Cases Per Month')


case_by_date