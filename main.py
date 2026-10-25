# Main script that runs the whole simulation
# Handles parameter initialization, time-stepping loop, and execution flow

import numpy as np

from src.config import PARAMS
from src.solver import initialize_grid, fdm_solver
from src.visualisation import plot_concentration, animate_concentration


def calculate_dt_max(vx, vy, D, dx, dy):
    """Stability limit for explicit upwind advection
    and central-difference diffusion.
    """
    rate = (
        abs(vx) / dx
        + abs(vy) / dy
        + 2 * D / dx**2
        + 2 * D / dy**2
    )

    if rate == 0:
        return np.inf

    return 1.0 / rate


def run_simulation(params):
    nx, ny = params["nx"], params["ny"]
    vx, vy, D = params["vx"], params["vy"], params["D"]
    dt = params["dt"]
    total_steps = params["total_steps"]

    X, Y, C, dx, dy = initialize_grid(
        nx, ny,
        params["x_range"],
        params["y_range"],
        params["sigma"],
        params["A"],
    )

    dt_max = calculate_dt_max(vx, vy, D, dx, dy)

    print(f"dx = {dx:.5f}, dy = {dy:.5f}")
    print(f"Chosen dt = {dt:.6f}")
    print(f"Stability limit dt_max = {dt_max:.6f}")

    if dt > dt_max:
        raise ValueError(
            f"Unstable time step: dt={dt:.6g}, "
            f"but dt_max={dt_max:.6g}"
        )

    # Save initial condition and selected time steps.
    save_every = max(1, total_steps // 10)
    history = [C.copy()]
    times = [0.0]

    for step in range(1, total_steps + 1):
        C = fdm_solver(C, dx, dy, dt, vx, vy, D)

        if step % save_every == 0 or step == total_steps:
            history.append(C.copy())
            times.append(step * dt)

    return X, Y, history, times


if __name__ == "__main__":
    X, Y, history, times = run_simulation(PARAMS)

    plot_concentration(X, Y, history[0], times[0])
    plot_concentration(X, Y, history[-1], times[-1])

    animate_concentration(X, Y, history, times)
