
# This script recursively zips up the ore and/or oreswig repos and their subrepos:
#   -o, --ore      compress ore
#   -s, --oreswig  compress oreswig (after running the swig wrapper)
# Run this script under windows to generate .zip files and under posix to generate .tgz files.
# Be sure that the given repos and their submodules are up to date.
# Before running this script, you need to ensure that swig is in your path.
# This is usually already the case on posix but not on windows.
# You also need to set some environment variables, e.g:
'''
windows:

SET ORE_DIR=C:\repos\ore.github
SET ORESWIG_DIR=C:\repos\oreswig.github
SET SWIG_DIR=C:\repos\swigwin\swigwin-4.1.1
SET PATH=%PATH%;%SWIG_DIR%

posix:

export ORE_DIR=/home/erik/repos/ore.github
export ORESWIG_DIR=/home/erik/repos/oreswig.github
'''

from git_archive_all import GitArchiver as ga
import argparse
import logging
import os
import os.path
import shutil
import subprocess
import sys

def validate_path(v):
    if v in os.environ:
        p = os.environ[v]
    else:
        raise Exception("{} not set".format(v))
    if os.path.exists(p):
        return p
    else:
        raise Exception("{} - invalid path: {}".format(v, p))

# We use git_archive_all to recursively zip up a repo and its submodules:
def git_archive(name, suffix, var):
    repo_path = validate_path(var)
    print("zipping {} repo...".format(name))
    zip_file = "{}.{}".format(name, suffix)
    handler = logging.StreamHandler(sys.stdout)
    handler.setFormatter(logging.Formatter('%(message)s'))
    ga.LOG.addHandler(handler)
    ga.LOG.setLevel(logging.INFO)
    archiver = ga(prefix=name, main_repo_abspath=repo_path)
    archiver.create(zip_file)

def run_wrapper():

    if os.name == "nt":
        shutil.unpack_archive("oreswig.zip")
    elif os.name == "posix":
        shutil.unpack_archive("oreswig.tgz")
    else:
        raise Exception("unrecognized os.name: {}".format(os.name))

    cwd = os.getcwd()
    wrapper_dir = os.path.abspath("oreswig/OREAnalytics-SWIG/Python")
    os.chdir(wrapper_dir)
    subprocess.call([PYTHON, "setup.py", "wrap"])
    os.chdir(cwd)

    if os.name == "nt":
        shutil.make_archive("oreswig", "zip", base_dir="oreswig")
    elif os.name == "posix":
        shutil.make_archive("oreswig", "gztar", base_dir="oreswig")
        os.rename("oreswig.tar.gz", "oreswig.tgz")
    else:
        raise Exception("unrecognized os.name: {}".format(os.name))

    shutil.rmtree("oreswig")

if os.name == "nt":
    suffix = "zip"
    PYTHON = "python"
elif os.name == "posix":
    suffix = "tgz"
    PYTHON = "python3"
else:
    raise Exception("unrecognized os.name: {}".format(os.name))

parser = argparse.ArgumentParser()
parser.add_argument("-o", "--ore", action="store_true", help="compress ore")
parser.add_argument("-s", "--oreswig", action="store_true", help="compress oreswig")
args = parser.parse_args()

if not args.ore and not args.oreswig:
    parser.error("at least one of -o and -s required")

if args.ore:
    git_archive("ore", suffix, "ORE_DIR")

if args.oreswig:
    git_archive("oreswig", suffix, "ORESWIG_DIR")
    run_wrapper()

