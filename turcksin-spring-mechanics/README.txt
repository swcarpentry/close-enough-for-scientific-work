Writing tests for scientific applications
(Bruno Turcksin, Timo Heister, Wolfgang Bangerth)

We will discuss the way we write testsuites for whole scientific
applications. We have tried this for the ASPECT code
(http://aspect.dealii.org) but since this code is too large to play
with easily, we will instead introduce a small Python toy code that
solves a model problem from Newtonian mechanics (masses connected by a
spring).

The approach is to start with one or a small number of prototypical
input files that we run through the application. For each, we save the
output and every time we run the testsuite (preferrably with every
change to the application) we can then verify that the output equals
the previous one.

Whenever one makes changes to the code, for example by adding
functionality, one needs to write a test that exercises the new
code. The simplest way to do this is to just take one of the existing
test inputs (or, indeed, one of the prototypes) and modify it in a
minimal way so that it runs through the new code. This way, one builds
a forest of tests that (hopefully) exercise the entire code base.


...............................

Concrete example: Spring Mechanics and System Testing

Problem:

Newtonian mechanics. Say, if we built a code that simulates
the trajectory of two objects bound together by a spring (with zero rest
length). I.e.,

   m_1 x_1''(t) = -m_1 g + D (x_2-x_1)
   m_2 x_2''(t) = -m_2 g + D (x_1-x_2)

plus initial conditions. 



Plan:

./ written in python+scipy
./ application is driven by parameter files (JSON)
./ we are testing a whole application not individual functions (so "system
testing" vs. "unit testing").
./ compare output vs. reference output (might need numdiff, which is good?)
