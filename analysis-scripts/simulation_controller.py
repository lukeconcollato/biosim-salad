
import time
import requests
import json
import os
import subprocess

## -1. Run Docker
#os.system('docker compose up')

# Run Docker in the background
subprocess.Popen(['docker', 'compose', 'up', '-d'])
time.sleep(20)

## 0. Create a simulation
BASE_URL = "http://localhost:8009/api"
requests.get(f"{BASE_URL}/simulation")

##0.5 running the post command
with open('your_file.xml', 'r') as file:
    xml_data = file.read()
pc0 = requests.post(f"{BASE_URL}/simulation/start", data=xml_data)
pc1 = requests.post(f"{BASE_URL}/simulation/start", data=xml_data)
pc2 = requests.post(f"{BASE_URL}/simulation/start", data=xml_data)

# 1. Get all existing simulation IDs
response = requests.get(f"{BASE_URL}/simulation")
sim_ids = response.json().get("simulations", [])
print(f"📋 Found {len(sim_ids)} simulations: {sim_ids}")

# 2. Loop through each and extract data
for sim_id in sim_ids:
    print(f"📦 Extracting data for simId {sim_id}...")
    r = requests.get(f"{BASE_URL}/simulation/{sim_id}")
    if r.status_code == 200:
        sim_data = r.json()
        with open(f"simulation_{sim_id}.json", "w") as f:
            json.dump(sim_data, f, indent=2)
        print(f"✅ Saved simulation_{sim_id}.json")
    else:
        print(f"❌ Failed to fetch data for simId {sim_id} — HTTP {r.status_code}")

## 3. Close Docker
os.system('docker compose down')

## old version that needs to be updated!