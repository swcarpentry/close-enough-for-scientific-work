---
highlighter: pygments
title: Introduction
encoding: UTF-8
authors: Samantha Ahern, Mayeul d\'Avezac, Adrian Harwood, Joe O\'Conner
---


Lattice-Boltzmann implementation in Julia
-----------------------------------------


The Lattice-Boltzmann method solves the Navier-Stokes equations - i.e. fluid
dynamics - using an intuitive description of how a discrete set of fictive
fluid particle populations interact on a discrete grid. Each population moves
through the grid with a distinct and fixed velocity. For instance, on a 2D
grid, there will be a population that always moves one grid point North every
time step, another population moving East one grid point, and  another
population moving South-East, and so on. To complete the model, at each time
step and each lattice site, the particles collide, exchanging member particles
between populations.

In this chapter, we will describe the test-driven development of a
Lattice-Boltzmann simulation in [Julia](http://julialang.org/). We will special
specific emphasis on how unit-testing allows us to design software with good
separation of concerns, and on how unit-testing represents a blue print of how
a specific piece of code is meant to be both used and not used. These two
aspects are key to developing code in collaborative manner.

The code used throughout the chapter is based on
[LatBo.jl](https://github.com/UCL/LatBo.jl). It was developped during the
course of a Hackathon sponsored by the [Software Sustainability
Institute](http://www.software.ac.uk/).

[LatBo.jl](https://github.com/UCL/LatBo.jl) exists as a Julia package. It can
be installed from the Julia prompt with:

{% highlight Julia %}
Pkg.clone("git@github.com:UCL/LatBo.jl.git")
Pkg.installed("LatBo")
{% endhighlight %}

The first line will install the package and the second line checks that the
install process completed. And since this about testing, we should certainly
check that all tests pass:

{% highlight Julia %}
Pkg.Test("LatBo")
{% endhighlight %}

At this point we should really figure out how to get output out of julia and
place it here. Really not sure how this can work without some sort of build
layer.
