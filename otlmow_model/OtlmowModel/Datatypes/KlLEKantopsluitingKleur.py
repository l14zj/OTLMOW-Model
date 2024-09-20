# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlLEKantopsluitingKleur(KeuzelijstField):
    """De kleur van de kantopsluiting."""
    naam = 'KlLEKantopsluitingKleur'
    label = 'Kantopsluiting kleur'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlLEKantopsluitingKleur'
    definition = 'De kleur van de kantopsluiting.'
    status = 'https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlLEKantopsluitingKleur'
    options = {
        'gekleurd': KeuzelijstWaarde(invulwaarde='gekleurd',
                                     label='gekleurd',
                                     status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                     definitie='gekleurd',
                                     objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlLEKantopsluitingKleur/gekleurd'),
        'grijs': KeuzelijstWaarde(invulwaarde='grijs',
                                  label='grijs',
                                  status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                  definitie='grijs',
                                  objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlLEKantopsluitingKleur/grijs'),
        'oker': KeuzelijstWaarde(invulwaarde='oker',
                                 label='oker',
                                 status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                 definitie='oker',
                                 objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlLEKantopsluitingKleur/oker'),
        'rood': KeuzelijstWaarde(invulwaarde='rood',
                                 label='rood',
                                 status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                 definitie='rood',
                                 objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlLEKantopsluitingKleur/rood'),
        'wit': KeuzelijstWaarde(invulwaarde='wit',
                                label='wit',
                                status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                definitie='wit',
                                objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlLEKantopsluitingKleur/wit'),
        'zwart': KeuzelijstWaarde(invulwaarde='zwart',
                                  label='zwart',
                                  status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                  definitie='zwart',
                                  objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlLEKantopsluitingKleur/zwart')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

