import unittest
from your_module import calculate_amortization

class TestAmortizationCalculation(unittest.TestCase):
    def test_amortization_calculation_1(self):
        self.assertAlmostEqual(calculate_amortization(100000, 5, 30), 536.82, places=2)

    def test_amortization_calculation_2(self):
        self.assertAlmostEqual(calculate_amortization(200000, 3.92, 15), 1475.82, places=2)

    def test_amortization_calculation_3(self):
        self.assertAlmostEqual(calculate_amortization(350000, 4.5, 30), 1773.37, places=2)

    def test_amortization_calculation_4(self):
        self.assertAlmostEqual(calculate_amortization(500000, 2.67, 10), 4746.70, places=2)

    def test_amortization_calculation_5(self):
        self.assertAlmostEqual(calculate_amortization(750000, 3.92, 20), 4473.52, places=2)

if __name__ == '__main__':
    unittest.main()# This file is intentionally left blank