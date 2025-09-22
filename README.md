# Simulations-and-Analysis
A collection of various custom calculators used to find values such as max acceleration of the UCD Formula Student EV

## Available Calculators

### Max Acceleration Calculator
Located in `max_acceleration_calculator/`

This advanced performance calculator determines realistic vehicle acceleration by considering both motor power and tire grip limitations. It helps optimize the design of the UCD Formula Student Electric Vehicle by:

- Calculating maximum tractive force from the powertrain
- Determining tire grip limits based on vehicle weight distribution
- Identifying whether the vehicle is power-limited or traction-limited
- Providing realistic acceleration estimates and 0-to-speed times
- Supporting both CSV file input and manual parameter entry for flexible usage

**Usage:** Run `python max_acceleration_calculator/max_acceleration_calculator.py` and choose between loading parameters from a CSV file or entering them manually. CSV files use descriptive English headers for easy manual editing between runs.
