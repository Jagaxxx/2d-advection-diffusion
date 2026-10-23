# == Simulation parameters for 2D Advection-Diffusion equation ==
PARAMS = {
    # Grid parameters
    "nx": 100,
    "ny": 100,
    "x_range": (0.0, 15.0),
    "y_range": (0.0, 10.0),
    
    # Physical parameters
    "vx": 1,      # Velocity (along x-axis)
    "vy": 0.5,      # Velocity (along y-axis)
    "D": 0.05,      # Isotropic diffusion coefficient
    
    # Initial condition parameters (Gaussian plume)
    "sigma": 0.6,   # Spread
    "A": 1,       # Amplitude
    
    # Time integration parameters
    "dt": 0.002,    # Time step (but keep the CFL stability condition in mind!!!)
    "total_steps": 300
}