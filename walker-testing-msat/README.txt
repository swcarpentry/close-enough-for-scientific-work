"Finding tests for the Matlab Seismic Anisotropy Toolkit"

Andrew Walker and James Wookey

During 2011 and 2012 we created MSAT, the Matlab Seismic Anisotropy
Toolkit [1,2]. We aimed to create a reusable, maintainable and documented
software suite to enable easer modelling of seismic anisotropy. This 
variation of seismic wave speed with direction is a property of many 
Earth materials that offers insight into processes such as the geometry
of cracks (important in hydrocarbon exploration) and the alignment
of crystals (a signature of high temperature deformation in the Earth's
interior). In creating MSAT we brought together existing software
already in use in our lab with new tools. Part of this effort involved
finding suitable tests for the various new and refurbished functions 
within MSAT. It turned out that many of the most useful of these 
functions are re-implementations of software described in published
scientific papers, often from the 1960s, '70s or '80s. We found that 
the example results commonly included in these papers make useful test
cases. Indeed, being able to reproduce these is a key to permitting
scientific reproducibility as distinct from showing that the software
"works" in other ways (e.g. fails gracefully if provided with invalid
data). In this contribution we will discuss some of the lessons we have
learned from using such literature results as test cases for scientific 
software. In particular, we will:

* Briefly introduce seismic anisotropy and MSAT for the non-specialist 
reader. Include a minimal amount of necessary background theory to 
allow the rest of the contribution to be understood.
* Point out that the literature is a good source of tests and these
tests have a special place in confirming scientific reproducibility.
* Argue that "good enough" in this context is sufficiently good to 
reproduce the published work, given the precision of the reported results.
* Make the point that it is valuable to include tests for all published
examples, not just a subset of them. Note that not doing this has caught
us out. 
* Illustrate this with an example, probably using tensor decomposition 
of Browaeys and Chevrot [3].
* Comment on the fact that this is not the only way we test MSAT.

[1] https://github.com/andreww/MSAT
[2] http://dx.doi.org/10.1016/j.cageo.2012.05.031
[3] http://dx.doi.org/10.1111/j.1365-246X.2004.02415.x





