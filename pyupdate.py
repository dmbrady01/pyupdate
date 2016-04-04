#!/usr/bin/env python

"""
pyupdate.py: Maintenance function for automatically updating python modules.
"""
# Import required modules
from __future__ import absolute_import
import sys
from subprocess import call
import pip

__author__ = "DM Brady"
__datewritten__ = "12Jun2015"
__lastmodified__ = "04Apr2016"


# Updating python packages through pip
def update_py_packages():
    r"""A quick script to update any packages you have
    installed using pip. First tries to upgrade pip
    and setuptools."""

    #checks to see if python2.x or 3.x
    if sys.version_info[0] == 2:
        call("pip install --upgrade --no-binary :all: pip", shell=True)
        call("pip install --upgrade --no-binary :all: setuptools", shell=True)

        for dist in pip.get_installed_distributions():
            call("pip install --upgrade " + dist.project_name, shell=True)
    elif sys.version_info[0] == 3:
        call("pip3 install --upgrade pip", shell=True)
        call("pip3 install --upgrade setuptools", shell=True)

        for dist in pip.get_installed_distributions():
            call("pip3 install --upgrade " + dist.project_name, shell=True)


