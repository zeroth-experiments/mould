#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: abhishek
# @Email: abhishek@zeroth.me
# @Date:   2015-06-01 09:59:47
# @License: Please read LICENSE file in project root.
# @Last Modified by:   abhishek
# @Last Modified time: 2015-06-11 09:57:18
import os
import sys
import imp


DEFAULT_ACTIONS_DIR = 'actions'
PWD = os.path.dirname(os.path.abspath(__file__))

def init(args, config):
	actions_dir = os.path.join(PWD, DEFAULT_ACTIONS_DIR)
	#print actions_dir
	if(os.path.exists(actions_dir)):
		sys.path.insert(0, actions_dir)
	else:
		print 'Actions are not in path'
		sys.exit(1)

	"""
		Idea is to run only one action per execution of the program that way things will be simple.
		and wont be some big magic.
		Thre are few rules about how to develope actions mor on them in actions/RULES
	"""
	try:
		action = __import__(args[0])
	except ImportError:
		print 'Cannot import action module %s' % args[0]
		print 'Action you are requesting dose not exist.'
		sys.exit(1)

	# Check if the action is a valid plugin
	if not (hasattr(action, '__plugin_type__') and action.__plugin_type__ == 'action'):
		print 'Error: InvalidType Seems like plugin "%s" is not of type "action"'% args[0]
		sys.exit(1)

	if(action._init_plugin_(args, config)):
		action._run_plugin_()
