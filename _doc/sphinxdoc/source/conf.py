# coding: utf-8
import sys
import os
import alabaster
from pyquickhelper.helpgen.default_conf import set_sphinx_variables

sys.path.insert(0, os.path.abspath(os.path.join(os.path.split(__file__)[0])))

set_sphinx_variables(__file__, "check_python_install", "Xavier Dupré", 2021,
                     "alabaster", alabaster.get_path(), locals(), add_extensions=['alabaster'],
                     extlinks=dict(issue=(
                         'https://github.com/sdpython/_check_python_install/issues/%s',
                         'issue %s')))

blog_root = "http://www.xavierdupre.fr/app/_check_python_install/helpsphinx/"
html_logo = "phdoc_static/project_ico.png"

notebooks_urls = "http://www.xavierdupre.fr/app/_check_python_install/helpsphinx/notebooks/"

nblinks = {
    'slideshowrst': notebooks_urls + 'slide_show.html',
}

epkg_dictionary.update({
    'cartopy': 'https://scitools.org.uk/cartopy/docs/latest/',
})
