#!/bin/bash

set -e

echo "@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"
echo "pwd"
pwd
echo "@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"

# Unpack ORE & ORE-SWIG
tar xfz ore.tgz
ls
echo "@@@@@@@@@@@@@@@@@@@ END ORE-WHEELS @@@@@@@@@@@@@@@@@@@@@@@@"
cd ore
ls
echo "@@@@@@@@@@@@@@@@@@@ END ORE @@@@@@@@@@@@@@@@@@@@@@@@"
cd ORE-SWIG
echo "@@@@@@@@@@@@@@@@@@@ END ORE-SWIG @@@@@@@@@@@@@@@@@@@@@@@@"
cd ..
cd ..
#cp exchangerate.hpp ore/QuantLib/ql
#tar xfz oreswig.tgz
#cp setup.py oreswig/OREAnalytics-SWIG/Python/setup.py
cp oreanalytics-config.linux ore/ORE-SWIG/oreanalytics-config

