# Numerical solver module for the 2D Advection-Diffusion equation.
# Implement here Finite Difference Method (FDM) with Upwind scheme and central differences.
import numpy as np

def initialize_grid(nx, ny, x_range, y_range, sigma, A=1):
    """Initialize rectangular grid"""
    x = np.linspace(x_range[0], x_range[1], nx)
    y = np.linspace(y_range[0], y_range[1], ny)

    dx = (x_range[1]-x_range[0])/(nx-1)
    dy = (y_range[1]-y_range[0])/(ny-1)

    X, Y = np.meshgrid(x,y)

    # Gauss: C(x,y,0) = exp(((X-x0)^2+(Y-y0)^2)/2sigma^2)
    xs, ys = (x_range[1]+x_range[0])/2, (y_range[1]+y_range[0])/2
    C = A * np.exp(-((X-xs)**2 + (Y-ys)**2)/(2*sigma**2))
    return X, Y, C, dx, dy

def fdm_solver(C, dx, dy, dt, vx, vy, D):
    """One time step using FDM"""
    C_new = C.copy()
    Ny, Nx = C.shape
    
    for i in range(1, Ny - 1):
        for j in range(1, Nx - 1):
            # Upwind Scheme (advection)
            if vx > 0:
                dc_dx = (C[i, j] - C[i, j-1]) / dx
            else:
                dc_dx = (C[i, j+1] - C[i, j]) / dx
                
            if vy > 0:
                dc_dy = (C[i, j] - C[i-1, j]) / dy
            else:
                dc_dy = (C[i+1, j] - C[i, j]) / dy
                
            # Central Difference (diffusion)
            d2c_dx2 = (C[i, j+1] - 2 * C[i, j] + C[i, j-1]) / (dx**2)
            d2c_dy2 = (C[i+1, j] - 2 * C[i, j] + C[i-1, j]) / (dy**2)
            
            # Update Scheme
            advection = vx * dc_dx + vy * dc_dy
            diffusion = D * (d2c_dx2 + d2c_dy2)
            
            C_new[i, j] = C[i, j] - dt * advection + dt * diffusion
            
    # Dirichlet boundary conditions
    C_new[0, :] = 0.0
    C_new[-1, :] = 0.0
    C_new[:, 0] = 0.0
    C_new[:, -1] = 0.0
    
    return C_new