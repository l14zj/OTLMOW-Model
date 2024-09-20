# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlKleurReflector(KeuzelijstField):
    """Kleuropties voor de reflector."""
    naam = 'KlKleurReflector'
    label = 'Kleur reflector'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlKleurReflector'
    definition = 'Kleuropties voor de reflector.'
    status = 'https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlKleurReflector'
    options = {
        'amber': KeuzelijstWaarde(invulwaarde='amber',
                                  label='amber',
                                  status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                  definitie='amber',
                                  objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlKleurReflector/amber'),
        'blauw': KeuzelijstWaarde(invulwaarde='blauw',
                                  label='blauw',
                                  status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                  definitie='blauw',
                                  objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlKleurReflector/blauw'),
        'groen': KeuzelijstWaarde(invulwaarde='groen',
                                  label='groen',
                                  status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                  definitie='groen',
                                  objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlKleurReflector/groen'),
        'rood': KeuzelijstWaarde(invulwaarde='rood',
                                 label='rood',
                                 status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                 definitie='rood',
                                 objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlKleurReflector/rood'),
        'wit': KeuzelijstWaarde(invulwaarde='wit',
                                label='wit',
                                status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                definitie='wit',
                                objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlKleurReflector/wit')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

