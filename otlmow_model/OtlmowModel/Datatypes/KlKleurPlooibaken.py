# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlKleurPlooibaken(KeuzelijstField):
    """Kleuropties voor het plooibaken."""
    naam = 'KlKleurPlooibaken'
    label = 'Kleur plooibaken'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlKleurPlooibaken'
    definition = 'Kleuropties voor het plooibaken.'
    status = 'https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlKleurPlooibaken'
    options = {
        'blauw': KeuzelijstWaarde(invulwaarde='blauw',
                                  label='blauw',
                                  status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                  definitie='blauw',
                                  objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlKleurPlooibaken/blauw'),
        'geel': KeuzelijstWaarde(invulwaarde='geel',
                                 label='geel',
                                 status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                 definitie='geel',
                                 objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlKleurPlooibaken/geel'),
        'grijs': KeuzelijstWaarde(invulwaarde='grijs',
                                  label='grijs',
                                  status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                  definitie='grijs',
                                  objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlKleurPlooibaken/grijs'),
        'groen': KeuzelijstWaarde(invulwaarde='groen',
                                  label='groen',
                                  status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                  definitie='groen',
                                  objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlKleurPlooibaken/groen'),
        'oranje': KeuzelijstWaarde(invulwaarde='oranje',
                                   label='oranje',
                                   status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                   definitie='oranje',
                                   objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlKleurPlooibaken/oranje'),
        'rood': KeuzelijstWaarde(invulwaarde='rood',
                                 label='rood',
                                 status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                 definitie='rood',
                                 objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlKleurPlooibaken/rood'),
        'zwart': KeuzelijstWaarde(invulwaarde='zwart',
                                  label='zwart',
                                  status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                  definitie='zwart',
                                  objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlKleurPlooibaken/zwart')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

