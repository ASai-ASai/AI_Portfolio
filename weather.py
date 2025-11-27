import requests
import pandas as pd               # 1. Import Pandas (The "Excel" tool)
import matplotlib.pyplot as plt   # 2. Import Matplotlib (The "Graph" tool)

print("1. Connecting to Weather Satellite...")

# --- STEP 1: GET THE DATA ---
url = "https://api.open-meteo.com/v1/forecast?latitude=41.89&longitude=12.49&past_days=10&hourly=temperature_2m"
response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    
    # --- STEP 2: ORGANIZE DATA (The part that was missing) ---
    hourly_data = data['hourly']
    df = pd.DataFrame(hourly_data)
    
    # Rename columns to be easier to read
    df = df.rename(columns={"time": "Date_Time", "temperature_2m": "Temp_C"})
    
    # --- STEP 3: DRAW THE GRAPH ---
    print("2. Data downloaded. Generating Graph...")
    
    # Fix the dates so Python understands them
    df['Date_Time'] = pd.to_datetime(df['Date_Time'])
    
    # Create the picture
    plt.figure(figsize=(10, 5))
    plt.plot(df['Date_Time'], df['Temp_C'], color='orange', label='Rome Temperature')
    
    plt.title("Rome Weather (Last 10 Days)")
    plt.xlabel("Date")
    plt.ylabel("Temperature (°C)")
    plt.grid(True)
    plt.legend()
    
    # Save it
    plt.savefig("rome_weather.png")
    print("3. SUCCESS! Graph saved as 'rome_weather.png'. Check your folder!")

else:
    print("Error: Could not connect to server.")