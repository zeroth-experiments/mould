#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: abhishek
# @Email: abhishek@zeroth.me
# @Date:   2015-06-01 08:04:45
# @License: Please read LICENSE file in project root.
# @Last Modified by:   abhishek
# @Last Modified time: 2015-06-02 11:47:02

from .document import Document
class Site:
	"""docstring for Site"""
	def __init__(self, config):
		self.config = config
		self.document = Document(config.source)
		self.documents = self._document.all_documents()

