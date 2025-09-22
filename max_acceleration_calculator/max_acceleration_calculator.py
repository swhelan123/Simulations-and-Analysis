import math
import csv
import os

def get_float_input(prompt, min_val=0):
    """Continuously asks for a valid float input until one is given."""
    while True:
        try:
            value = float(input(prompt))
            if value > min_val:
                return value
            else:
                print(f"Please enter a number greater than {min_val}.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def create_default_csv(filename):
    """Creates a default CSV file with example values and descriptive headers."""
    headers = [
        "Peak Torque (Nm)",
        "Final Drive Ratio",
        "Drivetrain Efficiency (0-1)",
        "Loaded Tyre Radius (m)",
        "Total Mass (kg)",
        "Weight Percentage on Driven Axle (%)",
        "Tire Coefficient of Static Friction",
        "Target Speed (km/h)"
    ]
    default_values = [250, 5.25, 0.92, 0.25, 280, 55, 1.4, 100]
    
    with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(headers)
        writer.writerow(default_values)
    print(f"Created default CSV file: {filename}")

def load_parameters_from_csv(filename):
    """Loads vehicle parameters from a CSV file."""
    try:
        with open(filename, 'r', encoding='utf-8') as csvfile:
            reader = csv.reader(csvfile)
            headers = next(reader)  # Skip headers
            values = next(reader)
            
            # Convert string values to float
            params = {
                'peak_torque': float(values[0]),
                'final_drive_ratio': float(values[1]),
                'drivetrain_efficiency': float(values[2]),
                'tyre_radius': float(values[3]),
                'total_mass': float(values[4]),
                'weight_on_driven_axle': float(values[5]) / 100,  # Convert percentage
                'coeff_friction': float(values[6]),
                'target_speed_kmh': float(values[7])
            }
            return params
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        return None
    except (ValueError, IndexError) as e:
        print(f"Error reading CSV file: {e}")
        print("Please check that the CSV file has the correct format.")
        return None

def save_parameters_to_csv(filename, params):
    """Saves vehicle parameters to a CSV file."""
    headers = [
        "Peak Torque (Nm)",
        "Final Drive Ratio", 
        "Drivetrain Efficiency (0-1)",
        "Loaded Tyre Radius (m)",
        "Total Mass (kg)",
        "Weight Percentage on Driven Axle (%)",
        "Tire Coefficient of Static Friction",
        "Target Speed (km/h)"
    ]
    values = [
        params['peak_torque'],
        params['final_drive_ratio'],
        params['drivetrain_efficiency'],
        params['tyre_radius'],
        params['total_mass'],
        params['weight_on_driven_axle'] * 100,  # Convert back to percentage
        params['coeff_friction'],
        params['target_speed_kmh']
    ]
    
    with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(headers)
        writer.writerow(values)
    print(f"Parameters saved to: {filename}")

def get_input_method():
    """Asks user to choose input method: CSV file or manual entry."""
    while True:
        print("\n--- Input Method Selection ---")
        print("1. Load parameters from CSV file")
        print("2. Enter parameters manually")
        choice = input("Choose input method (1 or 2): ").strip()
        
        if choice == "1":
            return "csv"
        elif choice == "2":
            return "manual"
        else:
            print("Invalid choice. Please enter 1 or 2.")

def get_csv_filename():
    """Gets CSV filename from user, with option to create default file."""
    while True:
        filename = input("Enter CSV filename (e.g., 'parameters.csv'): ").strip()
        if not filename.endswith('.csv'):
            filename += '.csv'
            
        if os.path.exists(filename):
            return filename
        else:
            create_choice = input(f"File '{filename}' doesn't exist. Create it with default values? (y/n): ").strip().lower()
            if create_choice in ['y', 'yes']:
                create_default_csv(filename)
                return filename
            else:
                print("Please enter an existing filename or choose to create a new one.")

def gather_parameters_manually():
    """Gathers all parameters through manual input."""
    print("\n--- Powertrain Parameters ---")
    peak_torque = get_float_input("Enter Peak Torque (Nm): ")
    final_drive_ratio = get_float_input("Enter Final Drive Ratio (e.g., 5.25): ")
    drivetrain_efficiency = get_float_input("Enter Drivetrain Efficiency (e.g., 0.92 for 92%): ")
    tyre_radius = get_float_input("Enter Loaded Tyre Radius (m): ")

    print("\n--- Vehicle and Tire Parameters ---")
    total_mass = get_float_input("Enter Total Mass (car + driver) (kg): ")
    weight_on_driven_axle = get_float_input("Enter Weight Percentage on Driven Axle (e.g., 55 for 55%): ") / 100
    coeff_friction = get_float_input("Enter Tire Coefficient of Static Friction (e.g., 1.4): ")
    target_speed_kmh = get_float_input("Enter Target Speed for 0-to-X calculation (km/h): ")
    
    return {
        'peak_torque': peak_torque,
        'final_drive_ratio': final_drive_ratio,
        'drivetrain_efficiency': drivetrain_efficiency,
        'tyre_radius': tyre_radius,
        'total_mass': total_mass,
        'weight_on_driven_axle': weight_on_driven_axle,
        'coeff_friction': coeff_friction,
        'target_speed_kmh': target_speed_kmh
    }

def calculate_advanced_performance():
    """
    Calculates a vehicle's performance, considering both power and traction limits.
    """
    print("--- Advanced Vehicle Performance Calculator ---")
    print("This tool calculates realistic acceleration based on motor and tire limits.")

    # Choose input method
    input_method = get_input_method()
    
    if input_method == "csv":
        filename = get_csv_filename()
        params = load_parameters_from_csv(filename)
        if params is None:
            print("Falling back to manual input...")
            params = gather_parameters_manually()
        else:
            print(f"Parameters loaded from {filename}")
            # Display loaded parameters
            print(f"Peak Torque: {params['peak_torque']} Nm")
            print(f"Final Drive Ratio: {params['final_drive_ratio']}")
            print(f"Drivetrain Efficiency: {params['drivetrain_efficiency']}")
            print(f"Tyre Radius: {params['tyre_radius']} m")
            print(f"Total Mass: {params['total_mass']} kg")
            print(f"Weight on Driven Axle: {params['weight_on_driven_axle']*100}%")
            print(f"Coefficient of Friction: {params['coeff_friction']}")
            print(f"Target Speed: {params['target_speed_kmh']} km/h")
    else:
        params = gather_parameters_manually()

    # Extract parameters for calculations
    peak_torque = params['peak_torque']
    final_drive_ratio = params['final_drive_ratio']
    drivetrain_efficiency = params['drivetrain_efficiency']
    tyre_radius = params['tyre_radius']
    total_mass = params['total_mass']
    weight_on_driven_axle = params['weight_on_driven_axle']
    coeff_friction = params['coeff_friction']
    target_speed_kmh = params['target_speed_kmh']

    # --- Calculations ---
    G_ACCEL = 9.81  # Gravitational acceleration in m/s^2

    # 1. Calculate the maximum force the MOTOR can produce at the wheels.
    motor_tractive_force = (peak_torque * final_drive_ratio * drivetrain_efficiency) / tyre_radius

    # 2. Calculate the maximum force the TIRES can transmit to the road.
    total_weight_force = total_mass * G_ACCEL
    normal_force_on_driven_axle = total_weight_force * weight_on_driven_axle
    tire_grip_limit_force = normal_force_on_driven_axle * coeff_friction

    # 3. Determine the limiting factor: motor power or tire grip.
    # The actual force is the MINIMUM of what the motor can supply and what the tires can handle.
    effective_tractive_force = min(motor_tractive_force, tire_grip_limit_force)

    # 4. Calculate the REALISTIC maximum acceleration using the effective force.
    max_acceleration = effective_tractive_force / total_mass

    # 5. Calculate time to reach target speed.
    target_speed_ms = target_speed_kmh * (1000 / 3600)
    time_to_target = target_speed_ms / max_acceleration
    
    # --- Display Results ---
    print("\n" + "="*35)
    print("---      PERFORMANCE ANALYSIS     ---")
    print("="*35)
    
    print(f"\nForce from Motor (Powertrain Limit): {motor_tractive_force:.2f} N")
    print(f"Force from Tires (Grip Limit):      {tire_grip_limit_force:.2f} N")
    
    if motor_tractive_force > tire_grip_limit_force:
        print("\nResult: The car is TRACTION-LIMITED.")
        print("The tires will slip before full motor power is delivered at launch.")
    else:
        print("\nResult: The car is POWER-LIMITED.")
        print("The tires can handle more force than the motor can produce.")
        
    print("\n--- Final Performance Metrics ---")
    print(f"Effective Tractive Force: {effective_tractive_force:.2f} N")
    print(f"Realistic Max Acceleration: {max_acceleration:.2f} m/s^2")
    print(f"Estimated time to reach {target_speed_kmh} km/h: {time_to_target:.2f} seconds")
    print("-" * 35)

    # Option to save parameters
    if input_method == "manual":
        save_choice = input("\nSave these parameters to CSV file? (y/n): ").strip().lower()
        if save_choice in ['y', 'yes']:
            save_filename = input("Enter filename to save (e.g., 'my_car.csv'): ").strip()
            if not save_filename.endswith('.csv'):
                save_filename += '.csv'
            save_parameters_to_csv(save_filename, params)


if __name__ == "__main__":
    calculate_advanced_performance()
