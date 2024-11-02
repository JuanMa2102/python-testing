import unittest
SERVER = 'server a'
class AllAssertsTests(unittest.TestCase):

    def test_assert_equal(self):
        self.assertEqual(10, 10)
        self.assertEqual("Hola", "Hola")

    def test_assert_true_or_false(self):
        self.assertTrue(True)
        self.assertFalse(False)

    def test_assert_raises(self):
        with self.assertRaises(ValueError):
            int("no_soy_un_numero")

    def test_assert_in(self):
        self.assertIn(10, [2, 4, 5, 10])
        self.assertNotIn(5, [2, 4, 10])

    def test_assert_dicts(self):
        user = {"first_name": "Luis", "last_name": "Martinez"}
        self.assertDictEqual(
            {"first_name": "Luis", "last_name": "Martinez"},
            user
        )
        self.assertSetEqual(
            {1, 2, 3},
            {1, 2, 3}
        )
    
    @unittest.skip("Development in progress")
    def test_skip(self):
        self.assertEqual('hola', 'adios')
        
    @unittest.skipIf(SERVER == 'server a', 'saltado por ser el server a')
    def test_skip_if( self):
        self.assertEqual(SERVER, 'server b')
    
    @unittest.expectedFailure
    def test_expect_fail(self):
        self.assertEqual(10, 5)