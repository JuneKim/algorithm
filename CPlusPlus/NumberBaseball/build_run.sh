#!/bin/sh

exe_file=numberBaseball

if [ -f $exe_file ];
then
rm -f $exe_file
fi

g++ -o $exe_file numberbaseball.cpp main.cpp

if [ -f $exe_file ];
then
chmod 755 $exe_file
./$exe_file
else
echo "file $exe_file is not exist"
fi
