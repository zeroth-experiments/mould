#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: abhishek
# @Email: abhishek@zeroth.me
# @Date:   2015-06-06 13:33:06
# @Last Modified by:   abhishek
# @Last Modified time: 2015-06-09 12:03:51
# @License: Please read LICENSE file in project root#!/usr/bin/env python

import sys
import os
import json
import shutil
from datetime import datetime

try:
    from jinja2 import Environment, FileSystemLoader
except ImportError:
    print 'You require Jinja2 to use Mould'
    sys.exit(1)
try:
    from markdown import Markdown
except ImportError:
    print 'you require markdown to Mould'
    sys.exit(1)

TARGET= '_site'
TEMPLATEDIR = '_layouts'
BLOG_TARGET_DIR = 'blog'

class JinjaBuilder:
    def __init__(self, args, site, config):
        self.args = args
        self.site = site
        self.config = config
        self.project_base = config['source']
        self.project_target = os.path.join(self.project_base, TARGET)
        self.posts = []
        
        if(not os.path.exists(self.project_target)):
                os.mkdir(self.project_target)
        
        self.markdown = Markdown()
        self.template_dir_path = os.path.join(self.project_base, TEMPLATEDIR)
        self.jinja_env = Environment(loader= FileSystemLoader(self.template_dir_path))

    def process(self):
        #lets 1st process all the pages
        # print json.dumps(self.site, indent=2)
        pages = self.site['pages']
        pages_documents = pages['documents']
        
        for doc in pages_documents:
            self.process_document(doc)
            #TODO subdirectory feature needs to think properly

        posts = self.site['posts']
        for post in posts:
            post_obj = self.process_post(post)
            self.posts.append(post_obj)

        if len(self.posts) :
            self.create_post_index(self.config)

        self.process_misc()

    def process_post(self, post):
        title = post['title']
        date = datetime.now()
        # if(post['header'].has_key('date')):
        #     date = datetime.strptime(post['header']['date'], '%Y-%m-%d')
        date = post['header']['date']
        post_file_title = "-".join(title.split(" "))
        post_dir_relpath = "%s/%s/%s/%s/%s" %(BLOG_TARGET_DIR, date.year, date.month, date.day, post_file_title)
        post_dir_abspath = os.path.join(self.project_target, post_dir_relpath)
        if(not os.path.exists(post_dir_abspath)):
            os.makedirs(post_dir_abspath)

        body = post['body']
        html = self.markdown.convert(body)
        template = self.jinja_env.get_template('post.html');
        page = {
            'body': html,
            'title': post['title'],
            'date': date
        }

        data = template.render(site=self.site, page=page)
        dest_file = os.path.join(post_dir_abspath, 'index.html')
        fd = open(dest_file, 'w')
        fd.write(data)
        fd.close()
        description = "\n".join(body.split('\n')[:2])
        description_html = self.markdown.convert(description)
        return {'title': title, 'url': post_dir_relpath, 'description': description_html , 'body':html}

    def create_post_index(self, config):
        blog_dir = os.path.join(self.project_target, BLOG_TARGET_DIR)
        if(not os.path.exists(blog_dir)):
            print "Blog content has not generated please check!"
            sys.exit(1)

        template = self.jinja_env.get_template('post_list.html');
        
        page = {
            'title': 'Blog'
        }

        data = template.render(site=self.site, posts=self.posts, page=page)
        dest_file = os.path.join(blog_dir, 'index.html')
        fd = open(dest_file, 'w')
        fd.write(data)
        fd.close()


    def process_document(self, document):
        d = document
        doc_filename = d['filename'].split('.')[0]
        doc_dir_name = '_'.join(doc_filename.split())
        doc_target_dir = os.path.join(self.project_target, doc_dir_name)

        if(not os.path.exists(doc_target_dir)):
            os.mkdir(doc_target_dir)
        
        html = self.markdown.convert(d['body'])
        template = self.jinja_env.get_template('page.html');
        page = {
            'body': html,
            'title': d['title']
        }

        data = template.render(site=self.site, page=page)
        dest_file = os.path.join(doc_target_dir, 'index.html')
        fd = open(dest_file, 'w')
        fd.write(data)
        fd.close()

    def process_misc(self):
        #move assets to _site
        if(os.path.exists(os.path.join(self.project_target, "assets"))):
            shutil.rmtree(os.path.join(self.project_target, "assets"))
        shutil.copytree(os.path.join(self.project_base, "_assets"), os.path.join(self.project_target, "assets"))