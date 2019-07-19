import unittest,sys,os
sys.path.append(os.path.abspath(os.path.dirname(os.path.dirname(__file__))))#当前目录上一级目录
from seleniumDemo.doclever_test import Demo
suite = unittest.TestSuite()
tests = [Demo('test_1_login'),Demo('test_2_logout')]
suite.addTests(tests)
with open(os.path.join(os.path.abspath(os.path.dirname(__file__)), "UnittestTextReport.txt"), 'a') as  f:
       runner = unittest.TextTestRunner(stream=f,verbosity=2,failfast=True)
       runner.run(suite)
