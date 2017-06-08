# -*- coding: utf-8 -*-

extensions = []

project = u'SDK'
copyright = u'2017, Citrix'
author = u'Citrix'
version = u'1.0'
release = u'1.0'
language = None

templates_path = ['templates', '.']
html_static_path = ['.']
source_suffix = '.rst'
master_doc = 'index'

exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']
pygments_style = 'sphinx'
todo_include_todos = False

html_additional_pages = {
    'index': 'index.html',
    'zh-cn/index': 'zh-cn/index.html',
}
