Peter Steinbach 
"Reproducible Randomness" 
- Unit Testing Statistical Estimators -

Statistics and statistical estimators are at the heart of every data analysis. In order to reduce the complexity of data, large sets of information are condensed to single numbers that are hoped to carry the core information content. In this section, I set out to program the median estimator of a fixed sample and unit test it along the way. I'll start out with a straight forward implementation of to demonstrate the hallmarks of unit testing. The crucial part here is to validate and verify the median given random data without jeopardizing reproducibility. After that, the unit tests will be used to perform regression tests and re-implement the median to improve performance given larger data sets.
