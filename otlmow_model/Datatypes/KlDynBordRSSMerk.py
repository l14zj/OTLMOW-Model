# coding=utf-8
import random
from otlmow_model.BaseClasses.KeuzelijstField import KeuzelijstField


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlDynBordRSSMerk(KeuzelijstField):
    """Keuzelijst met de gangbare merken van RSS borden. De merken verwijzen doorgaans naar de fabrikant of leverancier."""
    naam = 'KlDynBordRSSMerk'
    label = 'Dyn bord RSS merk'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlDynBordRSSMerk'
    definition = 'Keuzelijst met de gangbare merken van RSS borden. De merken verwijzen doorgaans naar de fabrikant of leverancier.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlDynBordRSSMerk'
    options = {
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

