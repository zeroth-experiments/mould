#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: abhishek
# @Email: abhishek@zeroth.me
# @Date:   2015-06-02 11:40:59
# @License: Please read LICENSE file in project root.
# @Last Modified by:   abhishek
# @Last Modified time: 2015-06-12 23:24:43

import os
import sys
import json

from .file_processor import FileProcessor
from .file_processor import Types

DOCUMENT_IGNORE_LIST = ['_posts', '_assets', 'config.json', '_layouts', '_site', 'index.html', '.git', '.gitignore']
POST_DIR = '_posts'

class Generator:
	"""docstring for Generator"""
	def __init__(self, config):
		self.config = config
		self.site = {}
		self.site['title'] = config['title']
		self.site['url'] = config['url']
		self.site['baseurl'] = config['baseurl']
		self.site['pages'] = {}
		self.site['posts'] = []
		if config['document']:
			self.create_documents(config)
		if config["post"]:
			self.create_posts(config)

	def create_posts(self, config):
		base_dir = config['source']
		post_dir = os.path.join(base_dir, POST_DIR)
		if(not os.path.exists(post_dir)):
			print "Error: _posts dose not exists"
			sys.exit(1)

		post_file_list = os.listdir(post_dir)
		for post_file in post_file_list:
			post_file_abspath = os.path.abspath(os.path.join(post_dir, post_file))
			if(os.path.exists(post_file_abspath) and os.path.isfile(post_file_abspath)):
				_post = self.process_document_file(post_file_abspath, None, config, Types.POST)
				if _post != None:
					self.site['posts'].append(_post)


	def create_documents(self, config):
		base_dir = config['source']
		base_dir_list = os.listdir(base_dir)

		dirs_to_process = os.listdir(base_dir)
		# print process_dirs

		for d in base_dir_list:
			if DOCUMENT_IGNORE_LIST.count(d.strip()):
			 	dirs_to_process.remove(d.strip())

		# go though each item if its dir then process_dir if file process_file
		for p in dirs_to_process:
			p_abspath = os.path.abspath(os.path.join(base_dir, p))
			if os.path.exists(p_abspath) and os.path.isdir(p_abspath):
				_dir = self.process_document_dir(p_abspath, config)
				if _dir != None:
					if(not self.site['pages'].has_key('directories')):
						self.site['pages']['directories'] = []
					self.site['pages']['directories'].append(_dir)

			else:
				_document = self.process_document_file(p_abspath, None, config, Types.DOCUMENT)
				if _document != None:
					if(not self.site['pages'].has_key('documents')):
						self.site['pages']['documents'] = []

					self.site['pages']['documents'].append(_document)

	def process_document_dir(self, path, config):
		dir_path = path
		dir_obj = {'path':dir_path}
		for sub_path in os.listdir(dir_path): 
			d_abspath = os.path.abspath(os.path.join(dir_path, sub_path))
			if os.path.exists(d_abspath) and os.path.isdir(d_abspath):
				sub_dir_ = self.process_document_dir(d_abspath, config)
				if(not dir_obj.has_key('directories')):
					dir_obj['directories'] = []
				dir_obj['directories'].append(sub_dir_)
			else:
				sub_document_ = self.process_document_file(d_abspath, os.path.dirname(d_abspath), config, Types.DOCUMENT)
				if sub_document_ != None:
					if(not dir_obj.has_key('documents')):
						dir_obj['documents'] = []

					dir_obj['documents'].append(sub_document_)
		return dir_obj

	def process_document_file(self, path, parent, config, file_type):
		#ignore the auto save files on linux by some editors
		#TODO: add the ignore file list in config
		if path.endswith("~"):
			return None
		document = FileProcessor(path, parent, config, file_type)
		# if document.ready():
		# 	print "__________________________\n"
		# 	print document.get_document_object()
		# 	print "__________________________\n\n\n"

		return document.get_document_object() if document.ready() else None

	def get_site(self):
		return self.site