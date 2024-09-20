# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlBinnenverlichtingstoestelSchakelwijze(KeuzelijstField):
    """Lijst met schakelwijzen voor een binnenverlichtingstoestel."""
    naam = 'KlBinnenverlichtingstoestelSchakelwijze'
    label = 'Binnenverlichtingstoestel schakelwijze'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlBinnenverlichtingstoestelSchakelwijze'
    definition = 'Lijst met schakelwijzen voor een binnenverlichtingstoestel.'
    status = 'https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlBinnenverlichtingstoestelSchakelwijze'
    options = {
        'continu': KeuzelijstWaarde(invulwaarde='continu',
                                    label='continu',
                                    status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                    objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlBinnenverlichtingstoestelSchakelwijze/continu'),
        'schakelaar': KeuzelijstWaarde(invulwaarde='schakelaar',
                                       label='schakelaar',
                                       status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                       objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlBinnenverlichtingstoestelSchakelwijze/schakelaar'),
        'timer': KeuzelijstWaarde(invulwaarde='timer',
                                  label='timer',
                                  status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                  objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlBinnenverlichtingstoestelSchakelwijze/timer')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

