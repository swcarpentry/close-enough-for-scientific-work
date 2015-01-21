# loop over all .json input files
for jsonfile in *.json ; do
  # execute our program on it and pipe the output into a file
  python ../spring.py ${jsonfile} > ${jsonfile}.new

  # then compare output; only ask 'diff' to report whether the
  # files are the same or not, and create output depending on this:
  # print an 'X' if there is a difference, a '.' if there isn't. this
  # ensures that test failures are easily visible
  if (diff ${jsonfile}.output ${jsonfile}.new > /dev/null) ; then
    echo " .    ${jsonfile}" ;
  else 
    echo " X    ${jsonfile}" ;
  fi
done