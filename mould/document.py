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
	def __init__(self, document_path, parent, config):
		if not os.path.exists(document_path):
			print 'File %s does not exist' % document_path
			sys.exit(1)

		self.config = config
		self.document_path = document_path
		self.header = {}
		self.body = None
		self.lastmodified = os.path.getmtime(document_path)
		self.created = os.path.getmtime(document_path)
		self.parent = None if parent == None  else self.get_parent_relative_path(parent)
		self.process_file(document_path)

	def get_parent_relative_path(self, parent):
		project_base_dir = os.path.abspath(self.config['source'])
		return os.path.relpath(parent, project_base_dir)

	def process_file(self, path):
		fd = open(path, 'r')
		raw = fd.read()
		_, h, b = SPLITTER.split(raw, 2)
		self.header = self.header_to_dictionary(h)
		self.body = b.strip()

	def header_to_dictionary(self, head):
		lines = head.split('\n')
		result = {}
		for l in lines:
			if l.strip() == '' or l == None:
				continue
			key, val = l.strip().split(':')
			result[key.strip()] = val.strip()
		return result

	def get_document(self):
		return { 'header':self.header, 'body':self.body, 'lastmodified':self.lastmodified, 'created':self.created, 'parent': self.parent}
