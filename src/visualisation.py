# Visualisation module for the 2D Advection-Diffusion equation.
# Implement here plotting functions for visualising the simulation results.

from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation, PillowWriter


FIGURES_DIR = Path(__file__).resolve().parent.parent / "figures"


def plot_concentration(X, Y, C, time):
    """Plot pollutant concentration as a 2D heatmap."""

    fig, ax = plt.subplots(figsize=(9, 5))

    mesh = ax.pcolormesh(
        X, Y, C,
        shading="auto",
        cmap="viridis",
        vmin=0
    )

    fig.colorbar(mesh, ax=ax, label="Concentration C")
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.set_title(f"Pollutant concentration at t = {time:.3f}")
    ax.set_aspect("equal", adjustable="box")

    fig.tight_layout()
    plt.show()


def animate_concentration(X, Y, history, times):
    """Animate and save pollutant concentration over time."""

    FIGURES_DIR.mkdir(parents=True, exist_ok=True)
    output_path = FIGURES_DIR / "pollutant_transport.gif"

    fig, ax = plt.subplots(figsize=(9, 5))

    vmax = max(float(C.max()) for C in history)
    if vmax <= 0:
        vmax = 1.0

    mesh = ax.pcolormesh(
        X, Y, history[0],
        shading="auto",
        cmap="viridis",
        vmin=0,
        vmax=vmax
    )

    colorbar = fig.colorbar(mesh, ax=ax)
    colorbar.set_label("Concentration C")

    title = ax.set_title(
        f"Pollutant concentration at t = {times[0]:.3f}"
    )
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.set_aspect("equal", adjustable="box")

    def update(frame):
        mesh.set_array(history[frame].ravel())
        title.set_text(
            f"Pollutant concentration at t = {times[frame]:.3f}"
        )
        return mesh, title

    animation = FuncAnimation(
        fig,
        update,
        frames=len(history),
        interval=200,
        blit=False,
        repeat=True
    )

    # Save animation as a GIF.
    animation.save(
        output_path,
        writer=PillowWriter(fps=5)
    )

    print(f"Animation saved to: {output_path}")

    plt.show()

    return animation
