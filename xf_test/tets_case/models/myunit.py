from xf_test.tets_case.models.driver import driver_browser
from xf_test.tets_case.models.db import MyDB
import unittest


class MyTest(unittest.TestCase):
    """继承TestCase类"""

    def setUp(self) -> None:
        self.driver = driver_browser()
        self.driver.implicitly_wait(15)
        self.driver.maximize_window()

    def tearDown(self) -> None:
        self.driver.close()
        MyDB().close_db()






















