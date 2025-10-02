

def water_column_height(tower_height, tank_height):
    height = tower_height + 3 * tank_height / 4
    return height

def pressure_gain_from_water_height(height):
    pressure = 998.2 * 9.80665 * height / 1000
    return pressure

def pressure_loss_from_pipe(pipe_diameter,
        pipe_length, friction_factor, fluid_velocity):
    pressure = (-friction_factor * pipe_length * 998.2 * fluid_velocity ** 2) / (2000 * pipe_diameter)
    return pressure

def main():
    print(pressure_loss_from_pipe(0.048692, 0, 0.018, 1.75))
    print(pressure_loss_from_pipe(0.048692, 200, 0, 1.75))
    print(pressure_loss_from_pipe(0.048692, 200, 0.018, 0))   
    print(pressure_loss_from_pipe(0.048692, 200, 0.018, 1.75))
    print(pressure_loss_from_pipe(0.048692, 200, 0.018, 1.65))
    print(pressure_loss_from_pipe(0.28687, 1000, 0.013, 1.65))
    print(pressure_loss_from_pipe(0.28687, 1800.75, 0.013, 1.65))


if __name__ == "__main__":
    main()