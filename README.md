Projectile Motion Calculator

This repository contains a Python script that calculates various parameters for a projectile's motion, including the optimal launch angle, required initial velocity, time to collision, and maximum height. It utilizes the `scipy.optimize` library to find the optimal launch angle to achieve a desired target velocity.

How It Works

The script uses a simplified model of projectile motion with the following inputs:
- Geographical coordinates (latitude and longitude) of the launch and landing locations.
- Altitude at launch and landing locations.
- Temperature at launch and landing locations.
- A target velocity to reach the destination.

The code consists of three main functions:
1. `calculate_initial_velocity`: Calculates the initial velocity required to reach the target velocity.
2. `calculate_time_to_collision`: Computes the time to collision based on the optimal launch angle and other parameters.
3. `calculate_max_height`: Determines the maximum height achieved during the projectile's motion.

The `scipy.optimize.minimize` function is used to find the optimal launch angle that minimizes the difference between the calculated initial velocity and the target velocity.

## Usage

To use this script, provide the necessary input parameters and run it. The optimal launch angle, required initial velocity, time to collision, and maximum height will be displayed as output.

## Dependencies
Python 3.x
scipy
Install the required packages using:

```python3
pip install scipy
pip install math
```
## Example

```python
python3 projectile_motion.py
```
![image](https://github.com/soltanali0/Univercity/assets/87374678/88c63767-7820-49cd-a3da-5269a0fd3112)

```text
latitude0 Geographical latitude of launch location
longitude0 Geographical longitude of launch location
altitude0 Altitude relative to sea level at launch location
temperatures Temperature at launch location (K) 
latitude1 Geographical latitude of landing location
longitude1 Geographical longitude of landing location
altitude1 Altitude relative to sea level at landing location
temperature1 Temperature at landing location (K)
target_velocity The desired velocity to reach the destination (m/s)
initial_guess [math.radians(45)]
```



