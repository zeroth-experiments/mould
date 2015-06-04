#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: abhishek
# @Email: abhishek@zeroth.me
# @Date:   2015-06-02 11:40:59
# @License: Please read LICENSE file in project root.
# @Last Modified by:   abhishek
# @Last Modified time: 2015-06-04 13:40:29

import os

from .document import Document

DOCUMENT_IGNORE_LIST = ['_post', '_assets', 'config.json']

class Generator:
	"""docstring for Generator"""
	def __init__(self, config):
		self.config = config

		if config['document']:
			self.create_documents(config)

	def create_documents(self, config):
		base_dir = os.path.abspath(config['source'])
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
				self.process_document_dir(p_abspath, config)
			else:
				self.process_document_file(p_abspath, None, config)


	def process_document_dir(self, path, config):
		dir_path = path
		for sub_path in os.listdir(dir_path): 
			d_abspath = os.path.abspath(os.path.join(dir_path, sub_path))
			if os.path.exists(d_abspath) and os.path.isdir(d_abspath):
				self.process_document_dir(d_abspath, config)
			else:
				#ignore the auto save files on linux by some editors
				#TODO: add the ignore file extentions list in config
				if d_abspath.endswith("~"):
					continue
				self.process_document_file(d_abspath, os.path.dirname(d_abspath), config)

	def process_document_file(self, path, parent, config):
		document = Document(path, parent, config)
		print "__________________________\n"
		print document.get_document()
		print "__________________________\n\n\n"

		