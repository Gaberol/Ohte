import unittest
from maksukortti import Maksukortti
from kassapaate import Kassapaate

class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.kassa = Kassapaate()
        self.maksukortti = Maksukortti(1000)

    def test_kassapaatteen_saldo_oikea_alusa(self):
        self.assertEqual(self.kassa.kassassa_rahaa, 100000)

    def test_lounaita_myyty_nolla_alussa(self):
        self.assertEqual(self.kassa.edulliset, 0)
        self.assertEqual(self.kassa.maukkaat, 0)

    def test_edullinen_osto_kasvattaa_saldoa(self):
        self.kassa.syo_edullisesti_kateisella(300)

        self.assertEqual(self.kassa.kassassa_rahaa_euroina(), 1002.4)

    def test_edullinen_osto_antaa_vaihtorahat_oikein(self):
        self.assertEqual(self.kassa.syo_edullisesti_kateisella(300), 60)

    def test_edullinen_osto_kasvattaa_myytyjen_lounaiden_maaraa(self):
        self.kassa.syo_edullisesti_kateisella(300)

        self.assertEqual(self.kassa.edulliset, 1)