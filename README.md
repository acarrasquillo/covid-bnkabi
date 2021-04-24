# covid-bnkabi
Visualize COVID-19 data for California data using CDC API 

'''
This iPython Notebook Visualized COVID-19 data from the data.cdc.gov APIs
Dataset Name: COVID-19 Case Surveillance Public Use Data with Geography
Dataset URL: https://data.cdc.gov/Case-Surveillance/COVID-19-Case-Surveillance-Public-Use-Data-with-Ge/n8mc-b4w4
'''

# See the iPython Notebook outputs in html on the link below
https://acarrasquillo.github.io/covid-bnkabi/
You can also download the repo and open the index.html file on the root directory.


# DOCs utilized

DATA
- https://data.cdc.gov/Case-Surveillance/COVID-19-Case-Surveillance-Public-Use-Data-with-Ge/n8mc-b4w4
- https://dev.socrata.com/foundry/data.cdc.gov/n8mc-b4w4

Plotpy and Panda doc
https://dev.socrata.com/blog/2016/02/02/plotly-pandas.html

- Data elements can be found on the COVID-19 case report form located at www.cdc.gov/coronavirus/2019-ncov/downloads/pui-form.pdf


# Requirements

- Download the repo
- On the root directory of the repo run the below commands

```
pip install -r requirements.txt
brew install npm
npm install
pip install jupyterlab "ipywidgets>=7.5"
jupyter labextension install jupyterlab-plotly@4.14.3
jupyter lab
```