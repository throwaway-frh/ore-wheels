#!/bin/bash

set -e

echo "@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"
echo "pwd"
pwd
echo "@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"

# Unpack ORE & ORE-SWIG
tar xfz ore.tgz
#cp exchangerate.hpp ore/QuantLib/ql
tar xfz oreswig.tgz
#cp setup.py oreswig/OREAnalytics-SWIG/Python/setup.py
cp oreanalytics-config.linux oreswig/OREAnalytics-SWIG/oreanalytics-config

