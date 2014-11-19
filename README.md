# Close Enough for Scientific Work

This repository hosts a collaborative book
in which scientists show one another how they test their software.
Contributions should be aimed at sophomores in science and engineering,
similar in mathematical complexity to:

*   [Lorena Barba's "12 Steps to Navier Stokes"](http://lorenabarba.com/blog/cfd-python-12-steps-to-navier-stokes/)
*   entries in [the N-body benchmark game](http://benchmarksgame.alioth.debian.org/u32/performance.php?test=nbody)
*   Software Carpentry's [invasion percolation example](http://software-carpentry.org/v4/invperc/index.html)

Each should cover about as much material
as would normally fit in a one-hour lecture.
The format of each entry will vary according to its content,
but we expect most will follow this template:

1.  Introduce the problem.

2.  Present a simple solution (100-200 lines of code).

3.  Show how to test that code, explaining:
    *   what tests have been chosen,
    *   why they have been chosen,
    *   why the author chose to implement the tests the way she did, and
    *   how she decided on the tolerances for those tests.

4.  (Optional) Add a feature, or extend the program in some other way,
    and show:
    *   how the tests are extended to handle the change, and
    *   how the testing pays off.

## Details

1.  Authors will retain the copyright on their work,
    but all material must be made available under
    the Creative Commons - Attribution (CC-BY) license,
    and all software must be made available under the MIT License.

2.  You may use any (widely-used) format and programming language you like ---
    we will employ a professional editor to handle copy editing and production.
    However, we ask that you *don't*:

    *   explain unit testing, the difference between verification and validation, etc. (we'll do that),
    *   explain how floating point works or that it's hard (ditto), or
    *   use math that even your close colleagues would have to look up.

3.  We would like to have contributions by April 2015,
    so that we can have the first printed book ready for Fall 2015.

4.  If you would like to contribute, please either:

    *   submit a pull request to this repository that follows the rules described below, or
    *   [mail Greg Wilson](mailto:gvwilson@software-carpentry.org).

## Layout

> If you are wondering, "Is X allowed?"
> [mail Greg Wilson](mailto:gvwilson@software-carpentry.org).
> The answer will almost certainly be "yes",
> since we would rather have you writing content
> than worrying about formatting rules.

1.  We will use `gh-pages` as the main branch of our repository
    rather than `master` so that material is immediately available at
    [http://swcarpentry.github.io/close-enough-for-scientific-work](http://swcarpentry.github.io/close-enough-for-scientific-work).

2.  Each contribution will be a sub-directory of this repository
    with a descriptive, hyphenated name,
    such as `wilson-invasion-percolation`.

3.  That sub-directory must contain a plain text file called `README.txt`
    with the contributor's name
    and a single paragraph describing the problem to be tackled.

4.  Code, images, and data files may be put in the same sub-directory
    or in sub-sub-directories as contributors think best.

5.  Finished contributions *must* include a file called `SETUP.txt`
    that describes how to install any software needed
    to re-run the code in the chapter.

6.  We strongly prefer vector formats such as SVG for diagrams,
    plots, etc.

## FAQ

*   *Why not an e-book or a website*?

    We will produce both of those as well.

*   *Why "sized to fit in a one-hour lecture"?*

    To signal that we don't want hundred-page contributions,
    and because we hope people actually will use contributions
    as lectures in various courses.
