import datetime

from django.test import TestCase
from ..models import SportTuri, SportCenter


class SportTuriModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        # set up non-modified objects that used by following test methods
        SportTuri.objects.create(nomi="Futbol")

    def test_nomi_label(self):
        tur = SportTuri.objects.get(id=1)
        field_label = tur._meta.get_field('nomi').verbose_name
        self.assertEqual(field_label, "nomi")

    def test_nomi_max_length(self):
        tur = SportTuri.objects.get(id=1)
        max_length = tur._meta.get_field('nomi').max_length
        self.assertEqual(max_length, 255)

    def test_object_name_is_nomi(self):
        tur = SportTuri.objects.get(id=1)
        self.assertEqual(str(tur), tur.nomi)

    


class SportCenterModelTest(TestCase):
    """
        Methods to test SportCenter model
    """

    @classmethod
    def setUpTestData(cls):
        tur = SportTuri.objects.create(nomi="Futbol")
        SportCenter.objects.create(
            nomi="Arena",
            sport_turi=tur,
            manzil="Severniy mikroyon",
            telfon="+998996051709",
            opens="8:00",
            closes="22:00",
            latitude="34.232223",
            longtitude="72.232332",
        )
    
    def test_nomi_label(self):
        center = SportCenter.objects.get(id=1)
        field_label = center._meta.get_field('nomi').verbose_name
        self.assertEqual(field_label, "nomi")
    
    def test_nomi_max_length(self):
        center = SportCenter.objects.get(id=1)
        max_length = center._meta.get_field('nomi').max_length
        self.assertEqual(max_length, 255)

    def test_manzil_value(self):
        center = SportCenter.objects.get(id=1)
        self.assertEqual(center.manzil, "Severniy mikroyon")

    def test_telfon_value(self):
        center = SportCenter.objects.get(id=1)
        self.assertEqual(center.telfon, "+998996051709")

    def test_telfon_max_length(self):
        center = SportCenter.objects.get(id=1)
        max_length = center._meta.get_field('telfon').max_length
        self.assertEqual(max_length, 25)

    def test_opens_closes_time(self):
        center = SportCenter.objects.get(id=1)
        open_time = datetime.time(8, 0)
        close_time = datetime.time(22, 0)
        self.assertEqual(center.opens, open_time)
        self.assertEqual(center.closes, close_time)

    def test_is_active_default_true(self):
        center = SportCenter.objects.get(id=1)
        self.assertTrue(center.is_active)
    
    def test_object_name_is_nomi(self):
        center = SportCenter.objects.get(id=1)
        self.assertEqual(str(center), center.nomi)

    