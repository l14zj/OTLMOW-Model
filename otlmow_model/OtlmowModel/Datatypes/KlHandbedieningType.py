# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlHandbedieningType(KeuzelijstField):
    """Types van handbediening voor toestellen bevestigd aan een kast."""
    naam = 'KlHandbedieningType'
    label = 'Handbediening type'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlHandbedieningType'
    definition = 'Types van handbediening voor toestellen bevestigd aan een kast.'
    status = 'https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlHandbedieningType'
    options = {
        'drukknop': KeuzelijstWaarde(invulwaarde='drukknop',
                                     label='drukknop',
                                     status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                     objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlHandbedieningType/drukknop'),
        'schakelaar': KeuzelijstWaarde(invulwaarde='schakelaar',
                                       label='schakelaar',
                                       status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                       objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlHandbedieningType/schakelaar'),
        'sleutelcontact': KeuzelijstWaarde(invulwaarde='sleutelcontact',
                                           label='sleutelcontact',
                                           status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                           objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlHandbedieningType/sleutelcontact')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

