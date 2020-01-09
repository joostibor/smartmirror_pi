#!/bin/bash

s=`pidof electron`

IFS=' ' read -ra tomb <<< "$s"

for i in "${tomb[@]}"
do
	kill $i
done
