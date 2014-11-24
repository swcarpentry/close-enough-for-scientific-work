Spring Mechanics and System Testing

- Turcksin, Heister, Bangerth

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
