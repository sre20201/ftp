#!/bin/bash 
for hour in {00..23}
do
  for month in {09..23} 
  do 
    echo "OP12${month}${hour}"
  done 
done > /tmp/files