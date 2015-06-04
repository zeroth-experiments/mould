#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: abhishek
# @Email: abhishek@zeroth.me
# @Date:   2015-06-02 11:40:59
# @License: Please read LICENSE file in project root.
# @Last Modified by:   abhishek
# @Last Modified time: 2015-06-04 13:40:29

import os

import .document import Document

DOCUMENT_IGNORE_LIST = ['_post', '_assets', 'config.json']

class Generator:
	"""docstring for Generator"""
	def __init__(self, config):
		self.config = config
		self.create_documents(config['source'])

	def create_documents(self, source_dir):
		base_dir = os.path.abspath(source_dir)
		base_dir_list = os.listdir(base_dir)

		dirs_to_process = os.listdir(base_dir)
		# print process_dirs
		for d in base_dir_list:
			if DOCUMENT_IGNORE_LIST.count(d.strip()):
			 	dirs_to_process.remove(d.strip())

		# go though each item if its dir then process_dir id file process_file
		for p in dirs_to_process:
			p_abspath = os.path.abspath(os.path.join(base_dir, p))
			if os.path.exists(p_abspath) and os.path.isdir(p_abspath):
				self.process_dir(p_abspath, config)
			else:
				self.process_file(p_abspath, config)


	def process_dir(self, path, config):
		pass

	def process_file(self, path, config):
		pass
		document = Document(path, config)
		print document.get_document()

		