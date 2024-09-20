# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlLEACSchokindex(KeuzelijstField):
    """De verschillende schokindices."""
    naam = 'KlLEACSchokindex'
    label = 'Schokindex'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlLEACSchokindex'
    definition = 'De verschillende schokindices.'
    status = 'https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlLEACSchokindex'
    options = {
        'a': KeuzelijstWaarde(invulwaarde='a',
                              label='a',
                              status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                              definitie='ASI <= 1.0 (zeer veilig)',
                              objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlLEACSchokindex/a'),
        'b': KeuzelijstWaarde(invulwaarde='b',
                              label='b',
                              status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                              definitie='ASI <= 1.4 (voldoende veilig)',
                              objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlLEACSchokindex/b'),
        'c': KeuzelijstWaarde(invulwaarde='c',
                              label='c',
                              status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                              definitie='ASI <= 1.9',
                              objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlLEACSchokindex/c')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

