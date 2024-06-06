# Smart Energy Management System Simulation

This Python program simulates a basic Smart Energy Management System (SEMS), particularly focusing on how it might intelligently manage energy resources to charge Electric Vehicles (EVs).

## Overview

The system simulates a scenario where you have:

- **Electric Vehicles (EVs):**  Each with a specific name and battery capacity.
- **Energy Sources:**
    - **PV (Photovoltaic/Solar):**  Simulates solar energy availability.
    - **ESU (Energy Storage Unit):** Simulates a battery storage system.
    - **Grid:** Represents the conventional power grid.
- **Time Zones:**  The simulation considers different time zones and their potential impact on energy availability (e.g., solar energy being more readily available during the day).

## How it Works

1. **Data Input:** The system reads data from a JSON file (`formated_data.json`), which contains information about:
   - Available cars (name, capacity).
   - Time zones and their corresponding PV, ESU, and Grid energy availability.

2. **User Interaction:**
   - The program presents the user with a list of available cars and time zones.
   - You can select one or more cars to charge and specify the time zone for the simulation.

3. **Energy Management Logic:**
   - The program calculates the total energy demand based on the selected cars.
   - It prioritizes energy sources in the following order:
      - **PV (Solar):** If enough solar energy is available, it's used first.
      - **ESU (Battery):** If solar energy is insufficient or unavailable, the battery storage is utilized.
      - **Grid:**  The power grid is used as a last resort if PV and ESU can't meet the demand.
   - The system determines the most efficient charging mode (e.g., `PV2EV`, `ESU2EV`, `GRID2EV`).

4. **Output:**
   - The program displays:
      - A summary of available cars, their capacities, and time zones.
      - The calculated energy demand, energy source usage, and the charging mode for each selected car. 
   - The results can also be optionally written to a text file.

## Running the Simulation

1. **Prerequisites:** Make sure you have Python 3 installed on your system. You'll also need to install the required libraries:
   ```bash
   pip install colorama prettytable requests