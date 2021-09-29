from django.test import TestCase
from ..forms import SportTuriCreateForm, SportCenterCreateForm


class TestSportTuriCreateForm(TestCase):

    def test_tur_create_labels(self):
        form = SportTuriCreateForm()
        self.assertTrue(form.fields['nomi'].label is None or form.fields['nomi'].label == 'Nomi')
        self.assertTrue(form.fields['photo'].label is None or form.fields['photo'].label == 'Rasm')
    
    def test_center_create_labels(self):
        form = SportCenterCreateForm()
        self.assertTrue(
            form.fields['nomi'].label is None or form.fields['nomi'].label == 'Nomi')
        self.assertTrue(
            form.fields['opens'].label is None or form.fields['opens'].label == 'Ochiladi')
        self.assertTrue(
            form.fields['closes'].label is None or form.fields['closes'].label == 'Yopiladi')
        self.assertTrue(
            form.fields['latitude'].label is None or form.fields['latitude'].label == 'Kenglik')
        self.assertTrue(
            form.fields['longtitude'].label is None or form.fields['longtitude'].label == 'Uzunlik')
        self.assertTrue(
            form.fields['photo'].label is None or form.fields['photo'].label == 'Rasm')
        self.assertTrue(
            form.fields['is_active'].label is None or form.fields['is_active'].label == 'Active')
        
        