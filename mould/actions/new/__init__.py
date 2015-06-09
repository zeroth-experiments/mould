#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: abhishek
# @Email: abhishek@zeroth.me
# @Date:   2015-06-01 10:56:26
# @License: Please read LICENSE file in project root.
# @Last Modified by:   abhishek
# @Last Modified time: 2015-06-09 13:19:23

# plugin name is just being use for debug purpose 
# it has nothing to do with actual plugin loader
# plugin loader totally depend on `path, directory name and type`
__plugin_name__ = 'new'
__plugin_type__ = 'action'

import os
import sys
import shutil

dir_name = None
def _init_plugin_(args, config):
    #TODO: build can have arguments
    if(len(args)<2):
    	print "new needs one argument use it like muld new <directory_name>"
    	sys.exit(1)

    global dir_name
    dir_name = args[1]
    return True


def _run_plugin_():
	new_plugin_path = os.path.dirname(os.path.abspath(__file__))
	cwd = os.getcwdu()
	template_path = os.path.join(new_plugin_path, "site_template")
	global dir_name
	if(os.path.exists(template_path)):
		shutil.copytree(template_path, os.path.join(cwd, dir_name))
	
