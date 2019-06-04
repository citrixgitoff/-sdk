# -*- coding: utf-8 -*-

extensions = []

project = u'SDK'
copyright = u'2019, Citrix'
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
    'citrix-cloud/index': 'citrix-cloud/index.html',
    'citrix-endpoint-management/index': 'citrix-endpoint-management/index.html',
    'citrix-hypervisor/index': 'citrix-hypervisor/index.html',
    'citrix-provisioning/index': 'citrix-provisioning/index.html',
    'citrix-virtual-apps-desktops/index': 'citrix-virtual-apps-desktops/index.html',
    'citrix-workspace/index': 'citrix-workspace/index.html',
    'citrix-networking/index': 'citrix-networking/index.html',
    'storefront/index': 'storefront/index.html',
    'citrix-workspace/index': 'citrix-workspace/index.html'
}
