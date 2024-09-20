# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlSleutelplan(KeuzelijstField):
    """Een keuzelijst met verschillende types van sleutel."""
    naam = 'KlSleutelplan'
    label = 'Sleutelplan'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlSleutelplan'
    definition = 'Een keuzelijst met verschillende types van sleutel.'
    status = 'https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlSleutelplan'
    options = {
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

