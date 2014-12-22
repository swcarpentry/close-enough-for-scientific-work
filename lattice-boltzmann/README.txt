Lattice-Boltzmann implementation in Julia
-----------------------------------------

Authors: Samantha Ahern, Mayeul d'Avezac, Adrian Harwood, Joe O'Conner  

The Lattice-Boltzmann method solves the Navier-Stokes equations - i.e. fluid
dynamics - using an intuitive description of how a discrete set of fictive
fluid particle populations interact on a discrete grid. Each population moves
through the grid with a distinct and fixed velocity. At each time step, the
populations collide and exchange particles. In this chapter, we will describe
the test-driven development of a Lattice-Boltzmann simulation in
[Julia](http://julialang.org/). We will given special specific emphasis to how
unit-testing allows us to design software with good
separation of concerns, and on how unit-testing represents a blue print of how
a specific piece of code is meant to be both used and not used. These two
aspects are key to developing code in collaborative manner.

The code used throughout the chapter is based on
[LatBo.jl](https://github.com/UCL/LatBo.jl). It was developped during the
course of a Hackathon sponsored by the [Software Sustainability
Institute](http://www.software.ac.uk/).
