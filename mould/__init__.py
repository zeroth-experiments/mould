#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: abhishek
# @Email: abhishek@zeroth.me
# @Date:   2015-06-01 09:59:47
# @License: Please read LICENSE file in project root.
# @Last Modified by:   abhishek
# @Last Modified time: 2015-06-01 13:58:25
import os
import sys
import imp

DEFAULT_ACTIONS_DIR = 'actions'
PWD = os.path.dirname(os.path.abspath(__file__))

def init(args):
	actions_dir = os.path.join(PWD, DEFAULT_ACTIONS_DIR)
	print actions_dir
	if(os.path.exists(actions_dir)):
		sys.path.append(actions_dir)
	else:
		print 'Actions are not in path'
		sys.exit(1)

	# for dirpath in os.listdir(actions_dir):
	try:
		print args[0]
		action = __import__(args[0])
	except ImportError:
		print "Cannot import action module %s" % args[0]
		print "Action you are requesting dose not exist."
		sys.exit(1)

	# we have the actions now lets use it
	print action.__plugin_name__

