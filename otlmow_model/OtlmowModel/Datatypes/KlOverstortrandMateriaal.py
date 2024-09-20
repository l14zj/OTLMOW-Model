# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlOverstortrandMateriaal(KeuzelijstField):
    """De materialen van de overstortrand."""
    naam = 'KlOverstortrandMateriaal'
    label = 'Overstortrand materiaal'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlOverstortrandMateriaal'
    definition = 'De materialen van de overstortrand.'
    status = 'https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlOverstortrandMateriaal'
    options = {
        'hout': KeuzelijstWaarde(invulwaarde='hout',
                                 label='hout',
                                 status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                 definitie='Een overstortrand uit hout.',
                                 objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlOverstortrandMateriaal/hout'),
        'inox': KeuzelijstWaarde(invulwaarde='inox',
                                 label='inox',
                                 status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                 definitie='Een overstortrand uit inox.',
                                 objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlOverstortrandMateriaal/inox'),
        'metselwerk': KeuzelijstWaarde(invulwaarde='metselwerk',
                                       label='metselwerk',
                                       status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                       definitie='Een overstortrand uit metselwerk.',
                                       objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlOverstortrandMateriaal/metselwerk')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

