import requests
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Constants
API_KEY = '9ab49733d3e7210f71b4ca076807bb1d'
CITY = 'Chennai'
URL = f"https://api.openweathermap.org/data/2.5/forecast?q={CITY}&appid={API_KEY}&units=metric"

# Fetching data
response = requests.get(URL)
data = response.json()

# Extract relevant data
weather_list = data['list']

# Convert to DataFrame
weather_data = {
    "DateTime": [],
    "Temperature (°C)": [],
    "Humidity (%)": [],
    "Wind Speed (m/s)": []
}

for entry in weather_list:
    weather_data["DateTime"].append(entry["dt_txt"])
    weather_data["Temperature (°C)"].append(entry["main"]["temp"])
    weather_data["Humidity (%)"].append(entry["main"]["humidity"])
    weather_data["Wind Speed (m/s)"].append(entry["wind"]["speed"])

df = pd.DataFrame(weather_data)
df['DateTime'] = pd.to_datetime(df['DateTime'])

# Show first few rows
print(df.head())
plt.figure(figsize=(14, 6))
sns.lineplot(x="DateTime", y="Temperature (°C)", data=df, marker="o", label='Temperature')
sns.lineplot(x="DateTime", y="Humidity (%)", data=df, marker="s", label='Humidity')
plt.xticks(rotation=45)
plt.title(f"Weather Forecast for {CITY}")
plt.xlabel("Date & Time")
plt.ylabel("Value")
plt.legend()
plt.tight_layout()
plt.grid(True)
plt.show()
# Plotting multiple variables in subplots
fig, axs = plt.subplots(3, 1, figsize=(12, 10), sharex=True)

sns.lineplot(ax=axs[0], x="DateTime", y="Temperature (°C)", data=df, color="r")
axs[0].set_title("Temperature Over Time")

sns.lineplot(ax=axs[1], x="DateTime", y="Humidity (%)", data=df, color="b")
axs[1].set_title("Humidity Over Time")

sns.lineplot(ax=axs[2], x="DateTime", y="Wind Speed (m/s)", data=df, color="g")
axs[2].set_title("Wind Speed Over Time")

plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

