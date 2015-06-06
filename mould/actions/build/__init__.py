#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: abhishek
# @Email: abhishek@zeroth.me
# @Date:   2015-06-01 10:56:26
# @License: Please read LICENSE file in project root.
# @Last Modified by:   abhishek
# @Last Modified time: 2015-06-06 14:13:09

# plugin name is just being use for debug purpose 
# it has nothing to do with actual plugin loader
# plugin loader totally depend on `path, directory name and type`
__plugin_name__ = 'build'
__plugin_type__ = 'action'

from .html_jinja_builder import JinjaBuilder
# parser = argparse.ArgumentParser(prog='mould', description='mould is a static site generator')
# parser.add_argument('build')
# parser.add_argument('-s', '--source', const='.', default='.', nargs='?', help="directory to perform build operations on.")
# args = parser.parse_args()
rednder = None

def _init_plugin_(args, site, config):
    #TODO: build can have arguments
    global rednder
    rednder = JinjaBuilder(args, site, config)
    return True


def _run_plugin_():
    global rednder
    rednder.process()
