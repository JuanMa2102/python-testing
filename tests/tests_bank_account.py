import os
import unittest
from unittest.mock import patch

from src.bank_account import BankAccount
from src.exceptions import WithdrawalTimeRestrictionError

class BankAccountTests(unittest.TestCase):

    def setUp(self) -> None:
        self.account = BankAccount(balance=1000, log_file="transacciones.log")

    def tearDown(self) -> None:
        if os.path.exists( self.account.log_file ):
            os.remove( self.account.log_file )
            
    def _count_lines( self, filename ):
        with open(filename, "r") as f:
            return len(f.readlines())
    
    def test_deposit(self):
        new_balance = self.account.deposit(500)
        self.assertEqual(new_balance, 1500, "El saldo debería ser 1500")

    @patch('src.bank_account.datetime')
    def test_withdraw(self, mock_datetime):
        mock_datetime.now.return_value.hour = 10
        new_balance = self.account.withdraw(200)
        self.assertEqual(new_balance, 800, "El saldo debería ser 800")
    
    def test_get_balance(self):
        assert self.account.get_balance() == 1000
        
    def test_transaccion_log(self):
        self.account.deposit(500)
        self.assertTrue(os.path.isfile("transacciones.log"))

    def test_count_transacciones(self):
        assert self._count_lines(self.account.log_file) == 1
        self.account.deposit(500)
        assert self._count_lines(self.account.log_file) == 2
    
    @patch('src.bank_account.datetime')
    def test_withdraw_during_bussiness_hours(self, mock_datetime):
        mock_datetime.now.return_value.hour = 10
        new_balance = self.account.withdraw(500)
        self.assertEqual(new_balance, 500, "El saldo debería ser 1000")
        
    @patch('src.bank_account.datetime')
    def test_withdraw_raise_during_bussiness_hours(self, mock_datetime):
        mock_datetime.now.return_value.hour = 7
        with self.assertRaises(WithdrawalTimeRestrictionError):
            self.account.withdraw(500)
        
    @patch('src.bank_account.datetime')
    def test_withdraw_raise_5_during_bussiness_hours(self, mock_datetime):
        mock_datetime.now.return_value.hour = 5
        with self.assertRaises(WithdrawalTimeRestrictionError):
            self.account.withdraw(500)
            
    
    def test_deposit_various_amounts(self):
        test_cases = [
           { "amount" :100, "expected" : 1100},
           { "amount" :3000, "expected" : 4000},
           { "amount" :4500, "expected" : 5500}
        ]
        
        for case in test_cases:
            with self.subTest(case):
                self.account = BankAccount(balance=1000, log_file="transacciones.log")
                new_balance = self.account.deposit(case["amount"])
                self.assertEqual(new_balance, case["expected"])
        