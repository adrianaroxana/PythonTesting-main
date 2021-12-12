import os
import unittest
from datetime import datetime
import multiple_tabs, context_menu_oop, basic_auth_oop


class MyTestSuite(unittest.TestCase):
    def test_suite(self):
        smoke_test = unittest.TestSuite()
        smoke_test.addTests([
            unittest.defaultTestLoader.loadTestsFromTestCase(multiple_tabs.TestMultipleTabs),
            unittest.defaultTestLoader.loadTestsFromTestCase(context_menu_oop.TestContext),
            unittest.defaultTestLoader.loadTestsFromTestCase(basic_auth_oop.TestAuth)]
        )  #smoke test este o variabila implementata ca obiect al clasei MyTestSuite in care sunt stocate toate testele care trebuie executate
        output_file = open(os.getcwd()+"test"+str(datetime.now())+".html","w")
        # getcwd - get current working directory
        # os - operating system
        # os.getcwd() din sistemul de operare extrage directorul curent
        # datetime.now() - data curenta


        runner = HtmlTestRunner # obiect folosit pt generarea raportului
        runner = HtmlTestRunner.HtmlTestRunner(
            combiner_reports = True,
            stream = output_file,
            report_title = "My Test Report",
            report_name = "Smoke Test"
        )
        runner.run(smoke_test)