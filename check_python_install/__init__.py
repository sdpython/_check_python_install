# coding: utf-8
"""
@file
@brief Module *check_python_install*.
Checks other modules installation on CI.
"""

__version__ = "0.1.51"
__author__ = "Xavier Dupré"
__github__ = "https://github.com/sdpython/_check_python_install"
__url__ = "http://www.xavierdupre.fr/app/_check_python_install/helpsphinx/index.html"
__downloadUrl__ = "https://github.com/sdpython/_check_python_install"
__license__ = "MIT License"
__blog__ = """
<?xml version="1.0" encoding="UTF-8"?>
<opml version="1.0">
    <head>
        <title>blog</title>
    </head>
    <body>
        <outline text="_check_python_install"
            title="_check_python_install"
            type="rss"
            xmlUrl="http://www.xavierdupre.fr/app/_check_python_install/helpsphinx/_downloads/rss.xml"
            htmlUrl="http://www.xavierdupre.fr/app/_check_python_install/helpsphinx/blog/main_0000.html" />
    </body>
</opml>
"""


def check(log=False):
    """
    Checks the library is working.
    It raises an exception.
    If you want to disable the logs:

    @param      log     if True, display information, otherwise
    @return             0 or exception
    """
    return True


def _setup_hook(use_print=False):
    """
    if this function is added to the module,
    the help automation and unit tests call it first before
    anything goes on as an initialization step.
    """
    # we can check many things, needed module
    # any others things before unit tests are started
    if use_print:
        print("Success: _setup_hook")
