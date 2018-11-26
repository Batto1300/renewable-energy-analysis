import unittest
import importlib as imp

ERROR_MESSAGE = """renewable_energy_analysis Module not found!\
    Did you added it to the PYTHONPATH?"""


class TestImport(unittest.TestCase):
    def test_custom_module(self):
        self.assert_(imp.find_loader(
            'file_names'), ERROR_MESSAGE)
