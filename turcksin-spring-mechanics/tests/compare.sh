# loop over all .json input files
for jsonfile in *.json ; do
  # execute our program on it and pipe the output into a file
  testname=`basename $jsonfile .json`
  python ../spring.py ${jsonfile} > ${testname}.output

  # then compare output; only ask 'diff' to report whether the
  # files are the same or not, and create output depending on this:
  # print an 'X' if there is a difference, a '.' if there isn't. this
  # ensures that test failures are easily visible
  if (diff ${testname}.reference ${testname}.output > /dev/null) ; then
    echo " .    ${jsonfile}" ;
  else
    echo " X    ${jsonfile}" ;
  fi
done
