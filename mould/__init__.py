#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: abhishek
# @Email: abhishek@zeroth.me
# @Date:   2015-06-01 09:59:47
# @License: Please read LICENSE file in project root.
# @Last Modified by:   abhishek
# @Last Modified time: 2015-06-02 11:51:53
import os
import sys
import imp
from .generator import Generator

DEFAULT_ACTIONS_DIR = 'actions'
PWD = os.path.dirname(os.path.abspath(__file__))

def init(args):
	actions_dir = os.path.join(PWD, DEFAULT_ACTIONS_DIR)
	#print actions_dir
	if(os.path.exists(actions_dir)):
		sys.path.append(actions_dir)
	else:
		print 'Actions are not in path'
		sys.exit(1)

	"""
		Idea is to run only one action per execution of the program that way things will be simple.
		and wont be some big magic.
		Thre are few rules about how to develope actions mor on them in actions/RULES
	"""
	try:
		#print args[0]
		action = __import__(args[0])
	except ImportError:
		print 'Cannot import action module %s' % args[0]
		print 'Action you are requesting dose not exist.'
		sys.exit(1)

	# Check if the action is a valid plugin 
	if not (hasattr(action, '__plugin_type__') and action.__plugin_type__ == 'action'):
		print 'Error: InvalidType Seems like plugin "%s" is not of type "action"'% args[0]
		sys.exit(1)

	# TODO: have to do somthing about configuration file
	site = Generator({'title':'Zeroth.me', 'url':'http://zeroth.me', 'source':'.'})
	
	# documents = site.documents
	# posts = site.posts
	# if(action._init_plugin_(args, site, documents, posts)):
	# 	action._run_plugin_()
