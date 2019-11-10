"""
@brief      test log(time=1s)
"""

import unittest
from pyquickhelper.pycode import ExtTestCase
from check_python_install.check_cartopy import check_cartopy


class TestCartopy(ExtTestCase):

    def test_cartopy(self):
        ax = check_cartopy()
        self.assertNotEmpty(ax)


if __name__ == "__main__":
    unittest.main()
