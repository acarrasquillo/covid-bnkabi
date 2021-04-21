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