import numpy as np
import pandas as pd
import streamlit as st
import numpy as np
import pydeck as pdk
import plotly.express as px

st.title('NYC Vehicle Collision Visualization')
st.set_page_config(layout="wide")
data_path = 'Data-Science-Web-App/Motor_Vehicle_Collisions_-_Crashes-1.csv'
colunm_name = ['CRASH_DATE', 'CRASH_TIME', 'BOROUGH', 'ZIP_CODE', 'LATITUDE',
       'LONGITUDE', 'LOCATION', 'ON_STREET_NAME', 'CROSS_STREET_NAME',
       'OFF_STREET_NAME', 'INJURED_PERSONS', 'KILLED_PERSONS',
       'INJURED_PEDESTRIANS', 'KILLED_PEDESTRIANS', 'INJURED_CYCLISTS',
       'KILLED_CYCLISTS', 'INJURED_MOTORISTS', 'KILLED_MOTORISTS',
       'CONTRIBUTING_FACTOR_VEHICLE_1', 'CONTRIBUTING_FACTOR_VEHICLE_2',
       'CONTRIBUTING_FACTOR_VEHICLE_3', 'CONTRIBUTING_FACTOR_VEHICLE_4',
       'CONTRIBUTING_FACTOR_VEHICLE_5', 'COLLISION_ID', 'VEHICLE_TYPE_1',
       'VEHICLE_TYPE_2', 'VEHICLE_TYPE_3', 'VEHICLE_TYPE_4', 'VEHICLE_TYPE_5']


@st.cache(persist=True)
def load_data(nrows):
    data = pd.read_csv(data_path, nrows=nrows, parse_dates=[['CRASH_DATE','CRASH_TIME']])
    data.dropna(subset=['LATITUDE','LONGITUDE'], inplace=True)
    lowercase = lambda x: str(x).lower()
    data.rename(lowercase, axis='columns', inplace=True)
    data.rename(columns={'crash_date_crash_time': 'date/time'}, inplace=True)
    for i in ['zip_code','killed_persons','killed_motorists']:
        data[i] = pd.to_numeric(data[i], errors='coerce').convert_dtypes()
    data = data.drop(data.index[0])
    return data

data = load_data(100000)
print(data.info())
original_data = data


st.header('Where are the most people injured in NYC')
injured_people = st.slider('Number of persons injured in vehicle ', 0, 19)
st.map(data.query('injured_persons >= @injured_people')[['latitude', 'longitude']].dropna(how='any'))


st.header('How many collision occur during a given time of day?')
hour = st.slider('Hour to look at', 0, 23)
data = data[data['date/time'].dt.hour == hour]


st.markdown('Vehicle collisions between %i:00 and %i:00' % (hour, (hour+1)%24 ) )
mid_point = (np.average(data['latitude']), np.average(data['longitude']))
st.write(pdk.Deck(
    map_style='mapbox://styles/mapbox/light-v9',
    initial_view_state={
        'latitude' : mid_point[0],
        'longitude' : mid_point[1],

        'zoom' : 11,
        'pitch' : 50,
    },
    layers=[
        pdk.Layer(
            'HexagonLayer',
            data=data[['date/time','latitude','longitude']],
            get_position=['longitude','latitude'],
            radius = 100,
            extruded = True,
            pickable = True,
            elevation_range = [0,1000],
        ),
    ],
))

st.subheader('Breakdown by minute between %i:00 and %i:00' % (hour,(hour+1)%24))
filtered = data[(data['date/time'].dt.hour >= hour) & (data['date/time'].dt.hour < (hour+1))]
hist = np.histogram(filtered['date/time'].dt.minute, bins=60, range=(0,60))[0]
chart_data = pd.DataFrame({'minute':range(60), 'crashes':hist})
fig = px.bar(chart_data, x='minute', y='crashes', hover_data=['minute','crashes'], height=400)
st.write(fig)


st.header('Top 5 dangerous streets by affected type')
select = st.selectbox('Affected type of people', ['Pedestrains','Cyclists','Motorists'])
if select == 'Pedestrians':
    st.write(original_data.query('injured_pedestrians >= 1')[['on_street_name','injured_pedestrians']].sort_values(by=['injured_pedestrians'], ascending=False).dropna(how='any')[:5])
elif select == 'Cyclists':
    st.write(original_data.query('injured_cyclists >= 1')[['on_street_name','injured_cyclists']].sort_values(by=['injured_cyclists'], ascending=False).dropna(how='any')[:5])
else:
    st.write(original_data.query('injured_motorists >= 1')[['on_street_name','injured_motorists']].sort_values(by=['injured_motorists'], ascending=False).dropna(how='any')[:5])


if st.checkbox('Raw Data', False):
    st.subheader('Raw Data')
    st.write(data)

