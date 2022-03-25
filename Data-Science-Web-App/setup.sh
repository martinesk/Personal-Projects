#!/bin/bash
wget 'https://data.cityofnewyork.us/api/views/h9gi-nx95/rows.csv?accessType=DOWNLOAD' -o 'Dataset/Motor_Vehicle_Collisions_-_Crashes.csv'

streamlit run ./TrafficDashboard