# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlBatterijModelnaam(KeuzelijstField):
    """De modelnaam van de batterij."""
    naam = 'KlBatterijModelnaam'
    label = 'Batterij modelnaam'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlBatterijModelnaam'
    definition = 'De modelnaam van de batterij.'
    status = 'https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlBatterijModelnaam'
    options = {
        'batzelt': KeuzelijstWaarde(invulwaarde='batzelt',
                                    label='batzelt',
                                    status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                    definitie='batzelt',
                                    objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlBatterijModelnaam/batzelt'),
        'nsa-lp12-55-t6': KeuzelijstWaarde(invulwaarde='nsa-lp12-55-t6',
                                           label='NSA LP12-55 T6',
                                           status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                           definitie='NSA LP12-55 T6',
                                           objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlBatterijModelnaam/nsa-lp12-55-t6')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

