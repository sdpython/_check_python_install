"""
@brief      test log(time=1s)
"""

import unittest
from pyquickhelper.pycode import ExtTestCase
from check_python_install.check_numba import check_numba


class TestCartopy(ExtTestCase):

    def test_numba(self):
        ax = check_numba()
        self.assertNotEmpty(ax)


if __name__ == "__main__":
    unittest.main()
