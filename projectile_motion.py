import math
from scipy.optimize import minimize
def calculate_initial_velocity(launch_angle, latitude0, longitude0, altitude0, temperature0, latitude1, longitude1, altitude1, temperature1):
    g = 9.81  # Gravitational acceleration (m/s^2)
    R = 287.05  # Gas constant for air (J/(kg*K))
    
    # Convert geographical coordinates to Cartesian coordinates
    x0 = (R + altitude0) * math.cos(math.radians(latitude0)) * math.cos(math.radians(longitude0))
    y0 = (R + altitude0) * math.cos(math.radians(latitude0)) * math.sin(math.radians(longitude0))
    x1 = (R + altitude1) * math.cos(math.radians(latitude1)) * math.cos(math.radians(longitude1))
    y1 = (R + altitude1) * math.cos(math.radians(latitude1)) * math.sin(math.radians(longitude1))

    # Calculate initial velocity
    delta_temperature = temperature1 - temperature0
    v0 = math.sqrt((x1 - x0)**2 + (y1 - y0)**2) / (math.sin(2 * launch_angle)) * math.sqrt(temperature0 / temperature1)
    return v0
def calculate_time_to_collision(launch_angle, latitude0, longitude0, altitude0, temperature0, latitude1, longitude1, altitude1, temperature1):
    v0 = calculate_initial_velocity(launch_angle, latitude0, longitude0, altitude0, temperature0, latitude1, longitude1, altitude1, temperature1)
    g = 9.81  # Gravitational acceleration (m/s^2)
    t = (2 * v0 * math.sin(launch_angle)) / g
    return t
def calculate_max_height(launch_angle, latitude0, longitude0, altitude0, temperature0, latitude1, longitude1, altitude1, temperature1):
    v0 = calculate_initial_velocity(launch_angle, latitude0, longitude0, altitude0, temperature0, latitude1, longitude1, altitude1, temperature1)
    g = 9.81  # Gravitational acceleration (m/s^2)
    h_max = (v0**2 * (math.sin(launch_angle))**2) / (2 * g)
    return h_max

latitude0 = 35.6895  # Geographical latitude of launch location
longitude0 = 51.3890  # Geographical longitude of launch location
altitude0 = 0  # Altitude relative to sea level at launch location
temperature0 = 288.15  # Temperature at launch location (K) 
latitude1 = 40.7128  # Geographical latitude of landing location
longitude1 = -74.0060  # Geographical longitude of landing location
altitude1 = 0  # Altitude relative to sea level at landing location
temperature1 = 288.15  # Temperature at landing location (K)
target_velocity = 100  # The desired velocity to reach the destination (m/s)
initial_guess = [math.radians(45)]
# Optimize the launch angle
result = minimize(lambda launch_angle: abs(calculate_initial_velocity(launch_angle, latitude0, longitude0, altitude0, temperature0, latitude1, longitude1, altitude1, temperature1) - target_velocity), initial_guess, method='SLSQP')
optimal_launch_angle = result.x[0]
optimal_velocity = result.fun
time_to_collision = calculate_time_to_collision(optimal_launch_angle, latitude0, longitude0, altitude0, temperature0, latitude1, longitude1, altitude1, temperature1)
max_height = calculate_max_height(optimal_launch_angle, latitude0, longitude0, altitude0, temperature0, latitude1, longitude1, altitude1, temperature1)
print("--------------------------------------------------------------------------")
print(f"Optimal launch angle 🏹 : {math.degrees(optimal_launch_angle)} degrees")
print(f"Required initial velocity 🚀 : {optimal_velocity} meters per second")
print(f"Time to collision ⏰ : {time_to_collision} seconds")
print(f"Maximum height ✈️ : {max_height} meters")
print("--------------------------------------------------------------------------")
