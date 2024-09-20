# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlWeegsensorType(KeuzelijstField):
    """Het type van de weegsensor."""
    naam = 'KlWeegsensorType'
    label = 'Weegsensor type'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlWeegsensorType'
    definition = 'Het type van de weegsensor.'
    status = 'https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlWeegsensorType'
    options = {
        'piÃ«zo-kwarts': KeuzelijstWaarde(invulwaarde='piÃ«zo-kwarts',
                                          label='piÃ«zo-kwarts',
                                          status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                          definitie='piÃ«zo-kwarts',
                                          objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlWeegsensorType/piÃ«zo-kwarts')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

