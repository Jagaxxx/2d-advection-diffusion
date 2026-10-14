# Numerical Simulation of the 2D Advection-Diffusion Equation

A Python-based numerical simulation of pollutant transport and dispersion in a two-dimensional fluid domain.

---

## Overview

How does a pollutant spread through a moving fluid?

This project investigates the transport and dispersion of a pollutant by numerically solving the **two-dimensional advection-diffusion equation**. It demonstrates how fluid flow carries a pollutant downstream while diffusion causes it to spread across the domain over time.

The project focuses on numerical discretization methods and the visualisation of simulation results.

## Mathematical Model

The simulation is based on the two-dimensional advection-diffusion equation:

$$
\frac{\partial C}{\partial t}
+ v_x \frac{\partial C}{\partial x}
+ v_y \frac{\partial C}{\partial y}
= D \left(
\frac{\partial^2 C}{\partial x^2}
+ \frac{\partial^2 C}{\partial y^2}
\right)
$$

where:

- $C(x,y,t)$ - pollutant concentration at position $(x,y)$ and time $t$,
- $v_x, v_y$ - velocity components of the fluid,
- $D$ - isotropic diffusion coefficient.

The equation describes two main physical processes:

- **Advection:** transport of the pollutant by the fluid flow.
- **Diffusion:** spreading of the pollutant due to concentration gradients.

Together, these processes determine how the pollutant concentration evolves over time.


## Repository Structure

```text
2d-advection-diffusion/
├── figures/                 # Generated plots, heatmaps, and animations
├── src/
│   ├── solver.py            # Numerical solver
│   └── visualisation.py     # Plotting and animation functions
├── .gitignore            
├── main.py                  # Main simulation script
├── README.md                # Project documentation
└── requirements.txt         
```


## Project Goals

The main objectives of this project are to:

- Apply numerical methods to a partial differential equation.
- Investigate the effects of advection and diffusion on pollutant transport.
- Visualise the evolution of pollutant concentration in two dimensions.
- Explore how numerical discretization affects simulation results.

## Authors

This project was developed as part of the *Numerical Methods in Differential Equations* course.

- [Jagoda](https://github.com/Jagaxxx)
- [Magda](https://github.com/MagdalenaSudol)
- [Paweł](https://github.com/Pawel-Stepien1)

