#!/bin/bash

# to be run in the aspect/tests directory

(echo "graph G {" ; 
 for i in *prm ; do
   echo "node [style=filled,color=blue,label=\"\"] `echo $i | sed s/[-_]//g`;" ; 
 done ; 
 for i in *prm ; do
   cat $i | perl -pi -e 's/^[ \t]*\n//g; s/^\#.*\n//g;' > 1
   for j in *prm ; do
     if test "$i" != "$j" ; then 
       cat $j | perl -pi -e 's/^[ \t]*\n//g; s/^\#.*\n//g;' > 2
       echo "`echo $i | sed s/[-_]//g` -- `echo $j | sed s/[-_]//g` [style=invis,len=`(echo scale=8 ; echo \`diff 1 2 | wc -l\`/10) | bc`];" ; 
     fi ; 
   done ;
 done ; 
 echo "}"
) | perl -pi -e 's/\.prm//g;' > graph.dot

neato -Tsvg graph.dot -Gmaxiter=100 -o graph.svg
neato -Tpng graph.dot -Gmaxiter=100 -o graph.png
