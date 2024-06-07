def es_bisiesto(anio):
    if (anio % 4 == 0 and anio % 100 != 0) or (anio % 400 == 0):
        return True
    else:
        return False

import unittest

class TestBisiesto(unittest.TestCase):

    def test_bisiesto_divisible_por_4_no_100(self):
        self.assertTrue(es_bisiesto(2024))
        self.assertTrue(es_bisiesto(2004))
    
    def test_no_bisiesto_divisible_por_100_no_400(self):
        self.assertFalse(es_bisiesto(1900))
        self.assertFalse(es_bisiesto(2100))
    
    def test_bisiesto_divisible_por_400(self):
        self.assertTrue(es_bisiesto(2000))
        self.assertTrue(es_bisiesto(2400))
    
    def test_no_bisiesto_no_divisible_por_4(self):
        self.assertFalse(es_bisiesto(2019))
        self.assertFalse(es_bisiesto(2018))

if __name__ == '__main__':
    unittest.main()