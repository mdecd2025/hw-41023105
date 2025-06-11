from controller import Robot

def run_robot():
    # Create the Robot instance
    robot = Robot()

    # Get simulation time step
    timestep = int(robot.getBasicTimeStep())

    # Get motor and keyboard devices
    motor = robot.getDevice('motor')
    keyboard = robot.getKeyboard()
    keyboard.enable(timestep)

    # Set initial motor position
    initial_position = 0.0  # Assuming initial position is 0

    # Main control loop
    while robot.step(timestep) != -1:
        motor.setPosition(38 * 3.14159 / 180)

if __name__ == "__main__":
    run_robot()