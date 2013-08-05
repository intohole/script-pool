#!/bin/sh
# ftree: Usage: ftree [any directory]
dir=${1:-.}
(cd $dir; pwd)
find $dir  -print 2
