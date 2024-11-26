# black-body-radiation
Python-code visualisation of the Black-body radiation formulas

According to the classical thermodynamics there are two famous approximation laws for the black-body radiation problem:

The Rayleigh-Jeans approximation for the spectral radiance which is valid for lower frequencies or higher temperatures. It is expressed as:

  $f(\nu,T)=\frac{2\nu^2kT}{c^2}$

​Wien's approximation is valid for higher frequencies (𝜈) or lower temperatures (T). It is expressed as:

  $f(\nu,T)=\frac{2h\nu^3}{c^2}e^{-\frac{h\nu}{kT}}$
 
The Planck's formula using solution for the quantum harmonic oscillator describes the Black-body radiation in a most accurate way. It is expressed as:

  $f(\nu,T)=\frac{2h\nu^3}{c^2}\frac{1}{e^{\frac{h\nu}{kT}}-1}$

where 

$c$ - speed of light, $c=3\cdot 10^8$ $\frac{m}{s}$

$h$ - planck constant, $h=6.626\cdot 10^{-34}$ $J\cdot s$

$k$ - Boltzmann constant, $k=1.28\cdot 10^{-23}$ $\frac{J}{K}$

The Stefan-Boltzmanns law describes the intensity of the thermal radiation emitted by matter in terms of that matter's temperature.

The radiant emittance R is directly proportional to the fourth power of the black body's temperature T as:

   $R=\sigma\cdot T^4$

where

$\sigma=5.670\cdot 10^{-8}$ $W\cdot m^{-2}\cdot K^{-4}$

Python program BLACK_BODY_RADIATION.py visualizes the Planck, Rayleigh-Jeans, and Wien formulas as functions of frequency and animates their behavior with a temperature slider

It uses the following steps:

1. Implements the formulas:

     Planck's formula.

     Rayleigh-Jeans formula.

     Wien's formula.

2. Plots all three formulas on a graph using Matplotlib.

3. Includes a slider widget for adjusting the temperature.

4. Calculates and displays the Stefan-Boltzmann luminosity value.
