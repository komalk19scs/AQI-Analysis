import pandas as pd
from io import StringIO
from contextlib import redirect_stdout

# Load data
df = pd.read_csv('data.csv', encoding='latin1', error_bad_lines=False)
df['date'] = pd.to_datetime(df['date'])

# Task 1: Year-wise list of Top 10 Cities of India with the most Air Pollution
df['year'] = df['date'].dt.year
grouped_data = df.groupby(['year', 'location']).mean(numeric_only=True)
top_10_cities = grouped_data.groupby('year').apply(lambda x: x['rspm'].nlargest(10).dropna())

# Display Task 1 result
print("Task 1 - Top 10 Cities with Most Air Pollution Each Year:")
print(top_10_cities)


# Task 2: Year-wise list of Top 10 States of India which has the most Air Pollution
def calculate_si(so2):
    if so2 <= 40:
        return so2 * (50 / 40)
    elif 40 < so2 <= 80:
        return 50 + (so2 - 40) * (50 / 40)
    elif 80 < so2 <= 380:
        return 100 + (so2 - 80) * (100 / 300)
    elif 380 < so2 <= 800:
        return 200 + (so2 - 380) * (100 / 800)
    elif 800 < so2 <= 1600:
        return 300 + (so2 - 800) * (100 / 800)
    else:
        return 400 + (so2 - 1600) * (100 / 800)

def calculate_ni(no2):
    if no2 <= 40:
        return no2 * 50 / 40
    elif 40 < no2 <= 80:
        return 50 + (no2 - 40) * (50 / 40)
    elif 80 < no2 <= 180:
        return 100 + (no2 - 80) * (100 / 100)
    elif 180 < no2 <= 280:
        return 200 + (no2 - 180) * (100 / 100)
    elif 280 < no2 <= 400:
        return 300 + (no2 - 280) * (100 / 120)
    else:
        return 400 + (no2 - 400) * (100 / 120)

def calculate_rpi(rspm):
    if rspm <= 30:
        return rspm * 50 / 30
    elif 30 < rspm <= 60:
        return 50 + (rspm - 30) * 50 / 30
    elif 60 < rspm <= 90:
        return 100 + (rspm - 60) * 100 / 30
    elif 90 < rspm <= 120:
        return 200 + (rspm - 90) * 100 / 30
    elif 120 < rspm <= 250:
        return 300 + (rspm - 120) * (100 / 130)
    else:
        return 400 + (rspm - 250) * (100 / 130)

def calculate_spi(spm):
    if spm <= 50:
        return spm
    elif 50 < spm <= 100:
        return spm
    elif 100 < spm <= 250:
        return 100 + (spm - 100) * (100 / 150)
    elif 250 < spm <= 350:
        return 200 + (spm - 250)
    elif 350 < spm <= 450:
        return 300 + (spm - 350) * (100 / 80)
    else:
        return 400 + (spm - 430) * (100 / 80)

df['si'] = df['so2'].apply(calculate_si)
df['ni'] = df['no2'].apply(calculate_ni)
df['rpi'] = df['rspm'].apply(calculate_rpi)
df['spi'] = df['spm'].apply(calculate_spi)

def calculate_aqi(row):
    si, ni, rpi, spi = row['si'], row['ni'], row['rpi'], row['spi']
    return max(si, ni, rpi, spi)

df['AQI'] = df.apply(calculate_aqi, axis=1)

# Extract year from the 'date' column
df['year'] = df['date'].dt.year

# Group by year and state, calculate the mean AQI for each group
grouped_data = df.groupby(['year', 'state'])['AQI'].mean().reset_index()

# Get the top 10 states with the highest mean AQI for each year
top_10_states_per_year = grouped_data.groupby('year').apply(lambda x: x.nlargest(10, 'AQI')).reset_index(drop=True)

# Display the result for Task 2
print("\nTask 2 - Year-wise list of Top 10 States with the most Air Pollution:")
print(top_10_states_per_year[['year', 'state', 'AQI']])


# Task 3: Month-wise Air Quality of Delhi for the Year 2021
delhi_2021_data = df[(df['date'].dt.year == 2021) & (df['location'] == 'Delhi')]
delhi_2021_data['month'] = delhi_2021_data['date'].dt.month_name()
delhi_monthly_air_quality = delhi_2021_data.groupby('month')['AQI'].mean().reset_index()

# Display Task 3 result
print("\nTask 3 - Monthly Air Quality of Delhi in 2021:")
print(delhi_monthly_air_quality[['month', 'AQI']])
