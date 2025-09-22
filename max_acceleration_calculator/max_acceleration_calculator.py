import math

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

def calculate_advanced_performance():
    """
    Calculates a vehicle's performance, considering both power and traction limits.
    """
    print("--- Advanced Vehicle Performance Calculator ---")
    print("This tool calculates realistic acceleration based on motor and tire limits.")

    # --- Gather Powertrain Inputs ---
    print("\n--- Powertrain Parameters ---")
    peak_torque = get_float_input("Enter Peak Torque (Nm): ")
    final_drive_ratio = get_float_input("Enter Final Drive Ratio (e.g., 5.25): ")
    drivetrain_efficiency = get_float_input("Enter Drivetrain Efficiency (e.g., 0.92 for 92%): ")
    tyre_radius = get_float_input("Enter Loaded Tyre Radius (m): ")

    # --- Gather Vehicle and Tire Inputs ---
    print("\n--- Vehicle and Tire Parameters ---")
    total_mass = get_float_input("Enter Total Mass (car + driver) (kg): ")
    weight_on_driven_axle = get_float_input("Enter Weight Percentage on Driven Axle (e.g., 55 for 55%): ") / 100
    coeff_friction = get_float_input("Enter Tire Coefficient of Static Friction (e.g., 1.4): ")
    target_speed_kmh = get_float_input("Enter Target Speed for 0-to-X calculation (km/h): ")

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


if __name__ == "__main__":
    calculate_advanced_performance()
