import unittest
from sample_account import Customer

class TestAccount(unittest.TestCase):

    #self instance Attributes
    def setUp(self):
        self.cust1 = Customer('Mike')

    def test_set_balance(self):
        self.cust1.set_balance(50000)
        self.assertEqual(self.cust1.balance, 50000)

        self.cust1.set_balance(-50000)
        self.assertEqual(self.cust1.balance, -50000)

        self.cust1.set_balance(12.63)
        self.assertEqual(self.cust1.balance, 12.63)

        self.cust1.set_balance(6429)
        self.assertEqual(self.cust1.balance, 6429)

    def test_withdraw(self):
        self.cust1.set_balance(50000)
        self.assertEqual(self.cust1.withdraw(2000), 48000)

        self.cust1.set_balance(9562)
        self.assertEqual(self.cust1.withdraw(1520), 8042)

        with self.assertRaises(RuntimeError):
            self.cust1.set_balance(-48266)
            self.cust1.withdraw(1520)

            self.cust1.set_balance(1000)
            self.cust1.withdraw(2000)

    def test_deposit(self):
        self.cust1.set_balance(50000)
        self.assertEqual(self.cust1.deposit(1234), 51234)

        self.cust1.set_balance(3482)
        self.assertEqual(self.cust1.deposit(860), 4342)

        self.cust1.set_balance(-4800)
        self.assertEqual(self.cust1.deposit(762), -4038)

if __name__ == '__main__': #if we run this module directly then run the code within the conditional which is the line that follows
    unittest.main()


#self.assertRaises(ValueError, calc.divide, 10, 0)
#                 (exception that we expect, function to test, parameters of the function to test)
#we dont include parantheses to the 2nd parameter of the assertRaises because the function itself will throw that error and the test will think something failed
#there is another option we can take to do the same as we did above
#we will use the Context Manager
#with self.assertRaises(ValueError):
#   calc.divide(10, 0)
#we can use either way but context manager is better idk y lol
#setUp(self) - runs before any single test
#tearDown(self) - runs after every single test
#mocking uses - when accessing urls or things that are out of your control
