#!/usr/bin/env python


"""
pyupdate.py: Maintenance function for automatically updating python modules.
"""
from __future__ import absolute_import

__author__ = "DM Brady"
__datewritten__ = "12Jun2015"
__lastmodified__ = "15Jun2015"

# Import required modules
import pip, sys
from subprocess import call

# Updating python packages through pip
def update_py_packages():
    r"""A quick script to update any packages you have
    installed using pip. First tries to upgrade pip
    and setuptools."""

    #checks to see if python2.x or 3.x
    if sys.version_info[0] == 2:
        call("pip install --upgrade --no-use-wheel pip", shell=True)
        call("pip install --upgrade --no-use-wheel setuptools", shell=True)

        for dist in pip.get_installed_distributions():
            call("pip install --upgrade " + dist.project_name, shell=True)
    elif sys.version_info[0] == 3:
        call("pip3 install --upgrade pip", shell=True)
        call("pip3 install --upgrade setuptools", shell=True)

        for dist in pip.get_installed_distributions():
            call("pip3 install --upgrade " + dist.project_name, shell=True)


