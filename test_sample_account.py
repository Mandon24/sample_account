import unittest
from sample_account import Customer

class TestAccount(unittest.TestCase):

    #setup customer object for use in each test case
    def setUp(self):
        self.cust1 = Customer('Mike')
    
    #test set_balance function
    def test_set_balance(self):
        #set positive balance
        self.cust1.set_balance(50000)
        self.assertEqual(self.cust1.balance, 50000)
        
        self.cust1.set_balance(6429)
        self.assertEqual(self.cust1.balance, 6429)
        
        #set negative balance
        self.cust1.set_balance(-50000)
        self.assertEqual(self.cust1.balance, -50000)

        #set a floating point balance
        self.cust1.set_balance(12.63)
        self.assertEqual(self.cust1.balance, 12.63)

    #test withdraw function 
    def test_withdraw(self):
        #withdraw from positive balance
        self.cust1.set_balance(50000)
        self.assertEqual(self.cust1.withdraw(2000), 48000)
        
        self.cust1.set_balance(9562)
        self.assertEqual(self.cust1.withdraw(1520), 8042)
        
        #test for RuntimeError check
        with self.assertRaises(RuntimeError):
            #withdraw from a negative balance
            self.cust1.set_balance(-48266)
            self.cust1.withdraw(1520)
            
            #withdraw from an amount lower than the withdraw amount
            self.cust1.set_balance(1000)
            self.cust1.withdraw(2000)
    
    #test deposit function
    def test_deposit(self):
        #deposit to a positive balance
        self.cust1.set_balance(50000)
        self.assertEqual(self.cust1.deposit(1234), 51234)
        
        self.cust1.set_balance(3482)
        self.assertEqual(self.cust1.deposit(860), 4342)

        #deposit to a negative balance
        self.cust1.set_balance(-4800)
        self.assertEqual(self.cust1.deposit(762), -4038)

if __name__ == '__main__':
    unittest.main()
    
