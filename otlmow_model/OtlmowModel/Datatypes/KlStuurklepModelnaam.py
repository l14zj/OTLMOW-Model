# coding=utf-8
from ..BaseClasses.KeuzelijstField import KeuzelijstField


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlStuurklepModelnaam(KeuzelijstField):
    """De modelnamen van een stuurklep."""
    naam = 'KlStuurklepModelnaam'
    label = 'Stuurklep modelnaam'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlStuurklepModelnaam'
    definition = 'De modelnamen van een stuurklep.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlStuurklepModelnaam'
    options = {
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

