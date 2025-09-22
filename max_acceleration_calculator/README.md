# Max Acceleration Calculator

This folder contains the advanced performance calculator for the UCD Formula Student EV.

## Description

This calculator determines realistic vehicle acceleration by considering both motor power and tire grip limitations. It provides a comprehensive analysis of vehicle performance by calculating the limiting factors that affect maximum acceleration.

## Features

- **Power-Limited vs Traction-Limited Analysis**: Determines whether the vehicle is limited by motor power or tire grip
- **Realistic Performance Metrics**: Calculates effective tractive force and maximum acceleration
- **Interactive Input**: User-friendly prompts for all vehicle parameters
- **Comprehensive Results**: Provides detailed analysis including time-to-speed calculations

## Files

- `max_acceleration_calculator.py` - Complete calculator implementation with interactive interface

## Usage

Run the calculator from the command line:

```bash
python max_acceleration_calculator.py
```

The program will prompt you to enter the following parameters:

### Powertrain Parameters
- Peak Torque (Nm)
- Final Drive Ratio
- Drivetrain Efficiency (decimal, e.g., 0.92 for 92%)
- Loaded Tyre Radius (m)

### Vehicle and Tire Parameters
- Total Mass including driver (kg)
- Weight Percentage on Driven Axle (%)
- Tire Coefficient of Static Friction
- Target Speed for 0-to-X calculation (km/h)

## Output

The calculator provides:
- Force from motor (powertrain limit)
- Force from tires (grip limit)
- Limiting factor analysis (power-limited vs traction-limited)
- Effective tractive force
- Realistic maximum acceleration (m/s²)
- Estimated time to reach target speed

## Dependencies

- Python 3.x (standard library only - no external dependencies required)