#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: abhishek
# @Email: abhishek@zeroth.me
# @Date:   2015-06-01 08:04:45
# @License: Please read LICENSE file in project root.
# @Last Modified by:   abhishek
# @Last Modified time: 2015-06-04 13:41:47
import os
import sys
import re

SPLITTER = re.compile(r'^-{3,}$', re.MULTILINE)

class Document:
	"""
	Document structure

	______________________

	---
	title:
	[author:]
	[date:] yyyy-mm-dd
	layout:<name of the layout>
	---
	body
	
	______________________
	"""
	def __init__(self, path, config):
		if not os.path.exist(path):
			print "File %s does not exist" % path
			sys.exit(1)

		self.path = path
		self.header = {}
		self.body = None
		self.lastmodified = os.path.getmtime(path)
		self.created = os.path.getmtime(path)
		self.dated = None
		process_file(path)

	def process_file(self, path):
		

		fd = open(path, 'r')

	def get_document(self):
		print "done"



		