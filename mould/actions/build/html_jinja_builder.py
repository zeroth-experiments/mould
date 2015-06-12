#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: abhishek
# @Email: abhishek@zeroth.me
# @Date:   2015-06-06 13:33:06
# @Last Modified by:   abhishek
# @Last Modified time: 2015-06-12 18:10:06
# @License: Please read LICENSE file in project root#!/usr/bin/env python

import sys
import os
import json
import shutil
from datetime import datetime

try:
    from jinja2 import Environment, DictLoader
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
        self.template_dictionary = self.get_template_dict(self.template_dir_path)
        self.jinja_env = Environment(loader= DictLoader(self.template_dictionary))

    def get_template_dict(self, dir_path):
        if(not os.path.exists(dir_path)):
            print "_layouts folder dose not exists"
            sys.exit(1)

        template_dict = {}
        template_file_list = os.listdir(dir_path)
        if len(template_file_list) < 1:
            print "_layouts should not be empty, put some templates there"
            sys.exit(1)
        for template_file in template_file_list:
            template_path = os.path.join(dir_path,template_file)
            if(os.path.isdir(template_path)):
                _dict = self.get_template_dict(template_path)
                if(len(_dict)>0):
                    template_dict.update(_dict)
            else:
                template_name = template_file
                fd = open(template_path, 'r')
                template_content = fd.read()
                fd.close()
                template_dict[template_name] = template_content
        #load root index as a template if available.
        root_index_path = os.path.join(self.project_base, 'index.html')
        if(not os.path.exists(root_index_path)):
            print "coudn't find Index.html at %s." % self.project_base
            return template_dict

        template_name = '__root_template__'
        fd = open(root_index_path, 'r')
        template_content = fd.read()
        fd.close()
        template_dict[template_name] = template_content

        return template_dict

    def process(self):
        #lets 1st process all the pages
        # print json.dumps(self.site, indent=2)
        if self.config['document']:
            pages = self.site['pages']
            if( self.site['pages'].has_key('documents')):
                pages_documents = pages['documents']
                
                for doc in pages_documents:
                    self.process_document(doc)
                    #TODO subdirectory feature needs to think properly

        if self.config['post']:
            posts = self.site['posts']
            for post in posts:
                post_obj = self.process_post(post)
                self.posts.append(post_obj)

            if len(self.posts) :
                self.create_post_index()

        if self.template_dictionary.has_key('__root_template__'):
            self.process_root_index()

        self.process_misc()

    def process_post(self, post):
        title = post['title']
        filename = post['filename'].split('.')[0]
        date = datetime.now()
        # if(post['header'].has_key('date')):
        #     date = datetime.strptime(post['header']['date'], '%Y-%m-%d')
        print post['header']
        date = post['header']['date']
        post_file_title = "-".join(filename.split(" "))
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
        return {'title': title, 'url': post_dir_relpath, 'description': description_html , 'body':html, 'header': post['header']}

    def create_post_index(self):
        blog_dir = os.path.join(self.project_target, BLOG_TARGET_DIR)
        if(not os.path.exists(blog_dir)):
            print "Blog content has not generated please check!"
            sys.exit(1)

        template = self.jinja_env.get_template('post_list.html');
        
        page = {
            'title': 'Blog'
        }
        sorted_post = self.get_sorted_posts()
        data = template.render(site=self.site, posts=sorted_post, page=page)
        dest_file = os.path.join(blog_dir, 'index.html')
        fd = open(dest_file, 'w')
        fd.write(data)
        fd.close()


    def process_document(self, document):
        d = document
        doc_filename = d['filename'].split('.')[0].lower()
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

    def process_root_index(self):
        template = self.jinja_env.get_template('__root_template__')
        page = {
            'title':'Home',
        }

        data = template.render(site=self.site, posts=self.posts, page=page)
        dest_file = os.path.join(self.project_target, 'index.html')
        fd = open(dest_file, 'w')
        fd.write(data)
        fd.close()
    def process_misc(self):
        #move assets to _site
        if(os.path.exists(os.path.join(self.project_target, "assets"))):
            shutil.rmtree(os.path.join(self.project_target, "assets"))
        shutil.copytree(os.path.join(self.project_base, "_assets"), os.path.join(self.project_target, "assets"))

    def get_sorted_posts(self):
        decorated_post  = [(dict_['header']['date'], dict_) for dict_ in self.posts]
        decorated_post.sort()
        decorated_post.reverse()
        sorted_post = [dict_ for (key, dict_) in decorated_post]
        return sorted_post