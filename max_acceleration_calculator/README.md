# Max Acceleration Calculator

This folder contains the advanced performance calculator for the UCD Formula Student EV.

## Description

This calculator determines realistic vehicle acceleration by considering both motor power and tire grip limitations. It provides a comprehensive analysis of vehicle performance by calculating the limiting factors that affect maximum acceleration.

## Features

- **Power-Limited vs Traction-Limited Analysis**: Determines whether the vehicle is limited by motor power or tire grip
- **Realistic Performance Metrics**: Calculates effective tractive force and maximum acceleration
- **Flexible Input Methods**: Choose between CSV file input or manual parameter entry
- **CSV File Support**: Load parameters from CSV files, save manually entered parameters to CSV, and create default CSV files
- **User-Friendly Interface**: Interactive prompts with clear parameter descriptions
- **Comprehensive Results**: Provides detailed analysis including time-to-speed calculations

## Files

- `max_acceleration_calculator.py` - Complete calculator implementation with interactive interface

## Usage

Run the calculator from the command line:

```bash
python max_acceleration_calculator.py
```

The program will first ask you to choose an input method:

### Input Method Options

1. **CSV File Input**: Load parameters from a CSV file
   - Enter an existing CSV filename
   - If the file doesn't exist, you can create one with default values
   - The CSV format uses descriptive English headers for easy manual editing

2. **Manual Input**: Enter parameters interactively through prompts
   - After calculations, you can save the entered parameters to a CSV file for future use

### CSV File Format

The CSV file uses the following format with descriptive headers:

```csv
Peak Torque (Nm),Final Drive Ratio,Drivetrain Efficiency (0-1),Loaded Tyre Radius (m),Total Mass (kg),Weight Percentage on Driven Axle (%),Tire Coefficient of Static Friction,Target Speed (km/h)
250,5.25,0.92,0.25,280,55,1.4,100
```

This allows for easy manual editing between runs for quick development and testing.

### Parameters

Whether entered manually or loaded from CSV, the following parameters are required:

#### Powertrain Parameters
- Peak Torque (Nm)
- Final Drive Ratio
- Drivetrain Efficiency (decimal, e.g., 0.92 for 92%)
- Loaded Tyre Radius (m)

#### Vehicle and Tire Parameters
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