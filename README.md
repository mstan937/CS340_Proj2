# CS340_Proj2
Project 2_READ ME
Grazioso Salvare Dashboard
Project Overview
Grazioso Salvare is a company dedicated to identifying and training dogs for search-and-rescue operations. This project involves developing a full-stack application to help Grazioso Salvare categorize and identify suitable dogs using data from a nonprofit agency operating five animal shelters in the Austin, Texas, area.
The core functionality of this application is a client-facing dashboard that connects to a MongoDB database. This dashboard allows Grazioso Salvare to interact with and visualize the data. It is designed to be user-friendly and intuitive, reducing user errors and training time.
Dashboard Features
Branding Elements
•	Grazioso Salvare Logo: The dashboard includes the Grazioso Salvare logo, linked to the company’s home page: www.snhu.edu.
•	Creator Identifier: The dashboard features a unique identifier with the creator's name, Marcus Stanley, to credit the dashboard's development.
Required Widgets
The dashboard includes the following interactive widgets:
•	Interactive Filter Options: Users can filter the data by rescue type using buttons or drop-downs:
o	Water Rescue
o	Mountain or Wilderness Rescue
o	Disaster Rescue or Individual Tracking
o	Reset: Resets all widgets to their original, unfiltered state.
•	Dynamic Data Table: The data table updates dynamically in response to the filtering options.
•	Geolocation Chart: A map that visualizes the shelters' locations, dynamically updated based on the selected filter.
•	Secondary Chart: An additional chart (e.g., pie chart) that responds dynamically to the filtering options.
Functionality
Filtering Mechanism
The dashboard's filtering options allow users to query the database for dogs suited to specific types of rescue training. Based on the selected filter, the data table, geolocation chart, and secondary chart will be updated to display the relevant data.
Rescue Types and Preferred Dog Breeds
Grazioso Salvare uses the following guidelines for selecting dogs:
•	Water Rescue: Preferred breeds include Labrador Retriever Mix, Chesapeake Bay Retriever, and Newfoundland. The preferred sex is intact female, with an age range of 26 to 156 weeks.
•	Mountain or Wilderness Rescue: Preferred breeds include the German Shepherd, Alaskan Malamute, Old English Sheepdog, Siberian Husky, and Rottweiler. The preferred sex is an intact male.
•	Disaster or Individual Tracking: Preferred breeds include Doberman Pinscher, German Shepherd, Golden Retriever, Bloodhound, and Rottweiler. The preferred sex is intact male, with an age range of 20 to 300 weeks.
Technical Specifications
•	Backend: MongoDB for database management.
•	Frontend: The dashboard is built with user-friendly UI components that allow intuitive interaction with the data.
Installation and Setup
To set up the application locally, follow these steps:
1.	Clone the Repository:
bash
Copy code
git clone  https://github.com/mstan937/CS340_Proj2
2.	Install Dependencies: Navigate to the project directory and install the necessary packages:
Copy code
npm install
3.	Set Up MongoDB: Ensure MongoDB is installed and running. Import the provided dataset into your MongoDB instance.
4.	Run the Application: Start the development server:
MongoDB
Copy code
npm start
5.	Access the Dashboard: Open your browser and navigate to http://localhost:3000 to interact with the dashboard.
Jupyter IPYNB Code:
app.run_server(debug=True, port=8051)If os errors came up I switched back
and forth between port=2223 and port=8051

from jupyter_dash import JupyterDash
import dash_leaflet as dl
from dash import dcc, html, dash_table
from dash.dependencies import Input, Output, State
import plotly.express as px
import base64
import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from Project2_crud import CRUD

# MongoDB connection parameters
USER = 'aacuser'
PASS = 'SNHU1234'
HOST = 'nv-desktop-services.apporto.com'
PORT = 32478
DB = 'AAC'
COL = 'animals'

# Connect to the database via CRUD Module
db = CRUD(USER, PASS, HOST, PORT, DB, COL)

# Get data from MongoDB
df = pd.DataFrame.from_records(db.read({}))
df.drop(columns=['_id'], inplace=True)

# Initialize the JupyterDash app
app = JupyterDash('Grazioso_Salvare_Dashboard')

# App layout
app.layout = html.Div([
    html.Center([
        html.A(href='https://learn.snhu.edu/content/enforced/1644157-CS-340-11210.202456-1/course_documents/Grazioso%20Salvare%20Logo.png?_&d2lSessionVal=ScQoRYLN9OTGv4T9RbCyYwie6&ou=1332057&ou=1644157', 
               children=[html.Img(src= "assets/Grazioso Salvare Logo.png")]),
        html.B(html.H1('Marcus Stanley - SNHU CS-340 Dashboard'))
    ]),
    html.Hr(),

    # Radio buttons for filtering options
    dcc.RadioItems(
        id='rescue-type-radio',
        options=[
            {'label': 'Water Rescue', 'value': 'Water Rescue'},
            {'label': 'Mountain or Wilderness Rescue', 'value': 'Mountain or Wilderness Rescue'},
            {'label': 'Disaster or Individual Tracking', 'value': 'Disaster or Individual Tracking'},
            {'label': 'Reset', 'value': 'Reset'}
        ],
        value='Reset',
        labelStyle={'display': 'inline-block'}
    ),
    html.Br(),
    html.Hr(),

    # Data table
    dash_table.DataTable(
        id='datatable-id',
        columns=[{"name": i, "id": i, "deletable": False, "selectable": True} for i in df.columns],
        data=df.to_dict('records'),
        page_size=10,
        row_selectable='single',
        selected_rows=[0],
        style_table={'height': '300px', 'overflowY': 'auto'},
        style_header={'backgroundColor': 'rgb(30, 30, 30)'},
        style_cell={'backgroundColor': 'rgb(50, 50, 50)', 'color': 'white'}
    ),
    html.Br(),
    html.Hr(),

    # Geolocation chart
    html.Div(id='map-id', className='col s12 m6'),
    
    # Second chart (Pie chart)
    dcc.Graph(id='pie-chart')
])

#############################################
# Interaction Between Components / Controller
#############################################

# Callback to update the data table, pie chart, and map based on filtering options and selected row
@app.callback(
    [Output('datatable-id', 'data'),
     Output('pie-chart', "figure"),
     Output('map-id', "children")],
    [Input('rescue-type-radio', 'value'),
     Input('datatable-id', 'selected_rows')],
    [State('datatable-id', 'data')]
)
def update_dashboard(rescue_type, selected_rows, current_data):
    # Filtering the data based on rescue type
    if rescue_type == 'Reset':
        data = db.read({})
    else:
        if rescue_type == 'Water Rescue':
            query = {"animal_type": "Dog", "breed": {"$in": ["Labrador Retriever Mix", "Chesapeake Bay Retriever", "Newfoundland"]}}
        elif rescue_type == 'Mountain or Wilderness Rescue':
            query = {"animal_type": "Dog", "breed": {"$in": ["German Shepherd", "Alaskan Malamute", "Rough Collie", "Bloodhound", "Rottweiler"]}}
        elif rescue_type == 'Disaster or Individual Tracking':
            query = {"animal_type": "Dog", "breed": {"$in": ["Beagle", "Bloodhound", "Bluetick Coonhound", "Plott Hound", "Treeing Walker Coonhound"]}}
        else:
            query = {}

        data = db.read(query)
    
    df = pd.DataFrame.from_records(data)
    if '_id' in df.columns:
        df.drop(columns=['_id'], inplace=True)
    data_table = df.to_dict('records')

    # Generate the Pie Chart
    if not df.empty:
        pie_chart = px.pie(df, names='breed', title='Breed Distribution')
    else:
        pie_chart = {}

    # Generate the Geo-Location Map
    if selected_rows is None or len(selected_rows) == 0 or df.empty:
        map_component = []
    else:
        row = selected_rows[0]
        #print (df.iloc[row]) 
        map_component = [
            dl.Map(style={'width': '1000px', 'height': '500px'}, center=[df.iloc[row]['location_lat'], df.iloc[row]['location_long']], zoom=10, children=[
                dl.TileLayer(id="base-layer-id"),
                dl.Marker(position=[df.iloc[row]['location_lat'], df.iloc[row]['location_long']], children=[
                    dl.Tooltip(df.iloc[row]['breed']),
                    dl.Popup([
                        html.H1("Animal Name"),
                        html.P(df.iloc[row]['name'])
                    ])
                ])
            ])
        ]

    return data_table, pie_chart, map_component

# Running the server
app.run_server(debug=True, port=8051)
