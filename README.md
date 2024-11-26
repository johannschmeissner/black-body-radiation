# black-body-radiation
Python-code visualisation of the Black-body radiation formulas

According to the classical thermodynamics there are two famous approximation laws for the black-body radiation problem:

The Rayleigh-Jeans approximation for the spectral radiance which is valid for lower frequencies or higher temperatures. It is expressed as:

  f(𝜈,T) = (2*𝜈^2*k*T)/c^2

​Wien's approximation is valid for higher frequencies (𝜈) or lower temperatures (T). It is expressed as:

  f(𝜈,T) = (2*h*𝜈^3/c^2)*exp(-h*𝜈/k*T)
 
The Planck's formula using solution for the quantum harmonic oscillator describes the Black-body radiation in a most accurate way. It is expressed as:

  f(𝜈,T) = (2*h*𝜈^3/c^2)*(1/(exp(h*𝜈/k*T)-1))

where 

      c - speed of light, 3*10^8 m/s

      h - planck constant, 6.626*10^-34 J*s

      k - Boltzmann constant, 1.28*10^-23 J/K

The Stefan-Boltzmanns law describes the intensity of the thermal radiation emitted by matter in terms of that matter's temperature.

The radiant emittance R is directly proportional to the fourth power of the black body's temperature T as:

R = σ*T^4

where

      σ = 5.670*10^-8 W*m^-2*K^-4

Python program visualizes the Planck, Rayleigh-Jeans, and Wien formulas as functions of frequency and animates their behavior with a temperature slider

It uses the following steps:

1. Implements the formulas:

     Planck's formula.

     Rayleigh-Jeans formula.

     Wien's formula.

2. Plots all three formulas on a graph using Matplotlib.

3. Includes a slider widget for adjusting the temperature.

4. Calculates and displays the Stefan-Boltzmann luminosity value.
