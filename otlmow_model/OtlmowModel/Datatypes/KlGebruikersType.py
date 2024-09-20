# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlGebruikersType(KeuzelijstField):
    """Geeft weer welke gebruikers op elk element van de koker."""
    naam = 'KlGebruikersType'
    label = 'Koker element gebruikers type'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#KlGebruikersType'
    definition = 'Geeft weer welke gebruikers op elk element van de koker.'
    status = 'https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlGebruikersType'
    options = {
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

