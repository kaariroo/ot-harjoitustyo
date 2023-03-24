import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti

class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.maksukortti = Maksukortti(1000)

class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.kassa = Kassapaate()
        self.kassassa_rahaa = 100000
        self.edulliset = 0
        self.maukkaat = 0
    
    def test_luotu_kassa_oikein(self):
    	self.assertEqual(self.kassassa_rahaa, 100000)
    	self.assertEqual(self.edulliset, 0)
    	self.assertEqual(self.maukkaat, 0)
    	
    def test_edullinen_kateisosto_toimii(self):
    	maksu = 300
    	self.kassa.syo_edullisesti_kateisella(maksu)
    	
    	self.assertEqual(self.kassa.kassassa_rahaa, 100240)
    	self.assertEqual(self.kassa.edulliset, 1)
    	self.assertEqual(self.kassa.syo_edullisesti_kateisella(maksu), maksu-240)
    
    def test_edullinen_kateisosto_ei_toimi(self):
    	maksu = 100
    	self.kassa.syo_edullisesti_kateisella(maksu)
    	
    	self.assertEqual(self.kassa.kassassa_rahaa, 100000)
    	self.assertEqual(self.kassa.edulliset, 0)
    	self.assertEqual(self.kassa.syo_edullisesti_kateisella(maksu), maksu)
    
    def test_maukas_kateisosto_toimii(self):
    	maksu = 1000
    	self.kassa.syo_maukkaasti_kateisella(maksu)
    	
    	self.assertEqual(self.kassa.kassassa_rahaa, 100400)
    	self.assertEqual(self.kassa.maukkaat, 1)
    	self.assertEqual(self.kassa.syo_maukkaasti_kateisella(maksu), maksu-400)
    
    def test_maukas_kateisosto_ei_toimi(self):
    	maksu = 100
    	self.kassa.syo_maukkaasti_kateisella(maksu)
    	
    	self.assertEqual(self.kassa.kassassa_rahaa, 100000)
    	self.assertEqual(self.kassa.maukkaat, 0)
    	self.assertEqual(self.kassa.syo_maukkaasti_kateisella(maksu), maksu)
    	
    		
    def test_maksukortti_toimii_edullisessa(self):
    	kortti = Maksukortti(1000)
    	self.kassa.syo_edullisesti_kortilla(kortti)
    	
    	self.assertEqual(kortti.saldo, 760)
    	self.assertEqual(self.kassa.edulliset, 1)
    	self.assertEqual(self.kassa.kassassa_rahaa, 100000)
    	
    def test_maksukortti_toimii_maukkaassa(self):
    	kortti = Maksukortti(1000)
    	self.kassa.syo_maukkaasti_kortilla(kortti)
    	
    	self.assertEqual(kortti.saldo, 600)
    	self.assertEqual(self.kassa.maukkaat, 1)
    	self.assertEqual(self.kassa.kassassa_rahaa, 100000)
    	
    def test_maksukortti_ei_toimii_edullisessa(self):
    	kortti = Maksukortti(100)
    	self.kassa.syo_edullisesti_kortilla(kortti)
    	
    	self.assertEqual(kortti.saldo, 100)
    	self.assertEqual(self.kassa.edulliset, 0)
    	self.assertEqual(self.kassa.kassassa_rahaa, 100000)
    	
    def test_maksukortti_ei_toimii_maukkaassa(self):
    	kortti = Maksukortti(100)
    	self.kassa.syo_maukkaasti_kortilla(kortti)
    	
    	self.assertEqual(kortti.saldo, 100)
    	self.assertEqual(self.kassa.maukkaat, 0)
    	self.assertEqual(self.kassa.kassassa_rahaa, 100000)
    	
    def test_rahan_lataus_toimii(self):
    	kortti = Maksukortti(1000)
    	self.kassa.lataa_rahaa_kortille(kortti, 100)
    	
    	self.assertEqual(kortti.saldo, 1100)
    	self.assertEqual(self.kassa.kassassa_rahaa, 100100)
    	self.assertEqual(self.kassa.lataa_rahaa_kortille(kortti, -100), None)
