#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: abhishek
# @Email: abhishek@zeroth.me
# @Date:   2015-06-01 10:18:10
# @License: Please read LICENSE file in project root.
# @Last Modified by:   abhishek
# @Last Modified time: 2015-06-01 13:56:14


#append pwd to pyhton path
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import mould
import argparse


def main(args):
	#TODO: Default action is build 
	if(not len(args)):
		args.append('build')

	mould.init(args)	
	

if __name__ == '__main__':
	main(sys.argv[1:])