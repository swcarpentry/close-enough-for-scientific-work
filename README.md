# Close Enough for Scientific Work

This repository hosts a collaborative book
in which scientists show one another how they test their software.
Contributions should be aimed at sophomores in science and engineering,
and each should be sized to fit a one-hour lecture.
While the format of each entry will vary according to its content,
we expect most will follow this template:

1.  Introduce the problem.

2.  Present a simple solution (100-200 lines of code).

3.  Show how to test that code, explaining:
    *   what tests have been chosen,
    *   why they have been chosen, and
    *   how the author decided on the tolerances for those tests.

4.  (Optional) Add a feature, or extend the program in some other way,
    and show:
    *   how the tests are extended to handle the change, and
    *   how the testing pays off.

## Details

Authors will retain the copyright on their work,
but all material must be made available under
the Creative Commons - Attribution (CC-BY) license,
and all software must be made available under the MIT License.

Note that we are primarily interested in *short* examples,
similar in size to:

*   [Lorena Barba's "12 Steps to Navier Stokes"](http://lorenabarba.com/blog/cfd-python-12-steps-to-navier-stokes/)
*   entries in [the N-body benchmark game](http://benchmarksgame.alioth.debian.org/u32/performance.php?test=nbody)
*   Software Carpentry's [invasion percolation example](http://software-carpentry.org/v4/invperc/index.html)

You may use any (widely-used) format and programming language you like ---
we will employ a professional editor to handle copy editing and production.
However, we ask that you *don't*:

*   explain unit testing, the difference between verification and validation, etc. (we'll do that),
*   explain how floating point works or that it's hard (ditto), or
*   use math that even your close colleagues would have to look up.

If you would like to contribute, please either:

1.  submit a pull request to this repository that follows the rules described below, or
2.  [mail Greg Wilson](mailto:gvwilson@software-carpentry.org).

## Layout

> If you are wondering, "Is X allowed?"
> [mail Greg Wilson](mailto:gvwilson@software-carpentry.org).
> The answer will almost certainly be "yes",
> since we would rather have you writing content
> than worrying about formatting rules.

1.  Each contribution will be a sub-directory of this repository
    with a descriptive, hyphenated name,
    such as `wilson-invasion-percolation`.

2.  That sub-directory must contain a plain text file called `README.txt`
    with the contributor's name
    and a single paragraph describing the problem to be tackled.

3.  Code, images, and data files may be put in the same sub-directory
    or in sub-sub-directories as contributors think best.

4.  Finished contributions *must* include a file called `SETUP.txt`
    that describes how to install any software needed
    to re-run the code in the chapter.

5.  We strongly prefer vector formats such as SVG for diagrams,
    plots, etc.
