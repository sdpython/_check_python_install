"""
@brief      test log(time=2s)
"""

import unittest
from pyquickhelper.pycode import ExtTestCase, skipif_azure_linux
from check_python_install.check_cartopy import check_cartopy


class TestCartopy(ExtTestCase):

    @skipif_azure_linux('Crashes on linux with azuredevops')
    def test_cartopy(self):
        ax = check_cartopy()
        self.assertNotEmpty(ax)


if __name__ == "__main__":
    unittest.main()
