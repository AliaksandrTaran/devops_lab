#!/usr/bin/env python
import unittest
import task_6
import os
class TestSys(unittest.TestCase):
    def setUp(self):
	pass

    def test_check_for_files(self):
        self.assertTrue(task_6.info_catcher(), (os.path.exists('./json_rep.json') == True))
        self.assertTrue(task_6.info_catcher(), (os.path.exists('./yaml_rep.yaml') == True))

if __name__=='__main__':
        unittest.main()
