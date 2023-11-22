# coding=utf-8
from ..BaseClasses.KeuzelijstField import KeuzelijstField


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlBatterijladerModelnaam(KeuzelijstField):
    """Lijst van modelnamen van batterijladers volgens de fabrikant."""
    naam = 'KlBatterijladerModelnaam'
    label = 'Modelnamen batterijladers'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlBatterijladerModelnaam'
    definition = 'Lijst van modelnamen van batterijladers volgens de fabrikant.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlBatterijladerModelnaam'
    options = {
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)
