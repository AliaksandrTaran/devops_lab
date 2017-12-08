#!/usr/bin/env python
import unittest
import task_6
import os
class TestSys(unittest.TestCase):
    def setUp(self):
	pass

    def test_check_for_files(self):
        self.assertFalse(task_6.info_catcher(), (os.path.isdir('./json_rep.json')))
        self.assertFalse(task_6.info_catcher(), (os.path.isdir('./yaml_rep.yaml')))

if __name__=='__main__':
        unittest.main()
