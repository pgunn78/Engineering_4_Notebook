#!/bin/bash
# Basic while loop
str="Hello World!"
counter=1

while [ $counter -le 10 ]
do
  echo $str
  ((counter+=1))
done
