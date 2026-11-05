import unittest

from warehouse.rates import shipping_quote


class RateTests(unittest.TestCase):
    # ------------------------------------------------------------------
    # Standard service (existing behaviour preserved)
    # ------------------------------------------------------------------

    def test_standard_local(self):
        self.assertEqual(shipping_quote(2, "local"), 8.0)

    def test_standard_regional(self):
        self.assertEqual(shipping_quote(2, "regional"), 11.0)

    def test_standard_explicit_keyword(self):
        self.assertEqual(shipping_quote(2, "local", service="standard"), 8.0)

    def test_standard_is_default(self):
        self.assertEqual(
            shipping_quote(2, "local"),
            shipping_quote(2, "local", service="standard"),
        )

    # ------------------------------------------------------------------
    # Express service (+$7 flat surcharge)
    # ------------------------------------------------------------------

    def test_express_local(self):
        self.assertEqual(shipping_quote(2, "local", service="express"), 15.0)

    def test_express_regional(self):
        self.assertEqual(shipping_quote(2, "regional", service="express"), 18.0)

    def test_express_surcharge_is_seven(self):
        """Express quote is exactly $7 more than the standard quote."""
        for zone in ("local", "regional"):
            with self.subTest(zone=zone):
                standard = shipping_quote(3, zone, service="standard")
                express = shipping_quote(3, zone, service="express")
                self.assertAlmostEqual(express - standard, 7.0)

    def test_express_fractional_weight(self):
        self.assertEqual(shipping_quote(1.5, "local", service="express"), 14.25)

    # ------------------------------------------------------------------
    # Validation
    # ------------------------------------------------------------------

    def test_invalid_weight(self):
        with self.assertRaises(ValueError):
            shipping_quote(0, "local")

    def test_invalid_zone(self):
        with self.assertRaises(ValueError):
            shipping_quote(1, "international")

    def test_invalid_service(self):
        with self.assertRaises(ValueError):
            shipping_quote(1, "local", service="overnight")
