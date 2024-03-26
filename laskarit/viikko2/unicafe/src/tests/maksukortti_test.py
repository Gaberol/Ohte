import unittest
from maksukortti import Maksukortti

class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.maksukortti = Maksukortti(1000)

    def test_luotu_kortti_on_olemassa(self):
        self.assertNotEqual(self.maksukortti, None)

    def test_tulostus_toimii(self):
        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 10.00 euroa")

    def test_kortin_saldo_oikein_alussa(self):
        self.assertEqual(self.maksukortti.saldo_euroina(), 10.0)

    def test_rahan_lataaminen_kasvattaa_saldoa_oikein(self):
        self.maksukortti.lataa_rahaa(100)

        self.assertEqual(self.maksukortti.saldo_euroina(), 11.0)

    def test_saldo_vahenee_maksun_jalkeen(self):
        self.maksukortti.ota_rahaa(100)

        self.assertEqual(self.maksukortti.saldo_euroina(), 9.0)

    def test_saldo_ei_muutu_jos_raha_ei_riita(self):
        self.maksukortti.ota_rahaa(1100)

        self.assertEqual(self.maksukortti.saldo_euroina(), 10.0)

    def test_maksu_palauttaa_true(self):
        self.assertEqual(self.maksukortti.ota_rahaa(100), True)

    def test_epaonnistunut_maksu_palauttaa_false(self):
        self.assertEqual(self.maksukortti.ota_rahaa(1100), False)
