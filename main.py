#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: abhishek
# @Email: abhishek@zeroth.me
# @Date:   2015-06-01 10:18:10
# @License: Please read LICENSE file in project root.
# @Last Modified by:   abhishek
# @Last Modified time: 2015-06-06 22:05:00


#append pwd to pyhton path
import sys
import os
import json

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import mould

cwd = os.getcwdu()

def get_configuration(path):
	config = {"source":cwd, "post":True, "document": True, "baseurl":'/'}
	config_file_path = os.path.join(path, "config.json")
	if(not os.path.exists(config_file_path)):
		print "config.json is not available in %s, please add it" % cwd
		sys.exit(1)
		return None

	config_file_fd = open(config_file_path, 'r')
	user_config = json.load(config_file_fd)
	config.update(user_config)
	return config


def main(args):
	config =  get_configuration(cwd)

	# Default action is build
	if(not len(args)):
		args.append('build')

	mould.init(args, config)
	

if __name__ == '__main__':
	main(sys.argv[1:])