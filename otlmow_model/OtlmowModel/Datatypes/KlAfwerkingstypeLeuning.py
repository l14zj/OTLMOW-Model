# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlAfwerkingstypeLeuning(KeuzelijstField):
    """Geeft de afwerking van de leuning weer."""
    naam = 'KlAfwerkingstypeLeuning'
    label = 'Afwerkingstype leuning'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#KlAfwerkingstypeLeuning'
    definition = 'Geeft de afwerking van de leuning weer.'
    status = 'https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlAfwerkingstypeLeuning'
    options = {
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

