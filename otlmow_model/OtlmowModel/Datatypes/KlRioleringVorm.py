# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlRioleringVorm(KeuzelijstField):
    """Vormen van de riolering."""
    naam = 'KlRioleringVorm'
    label = 'Riolering vorm'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlRioleringVorm'
    definition = 'Vormen van de riolering.'
    status = 'https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlRioleringVorm'
    options = {
        'achthoekig': KeuzelijstWaarde(invulwaarde='achthoekig',
                                       label='achthoekig',
                                       status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                       definitie='Achthoekig',
                                       objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlRioleringVorm/achthoekig'),
        'andere': KeuzelijstWaarde(invulwaarde='andere',
                                   label='andere',
                                   status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                   definitie='Andere',
                                   objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlRioleringVorm/andere'),
        'cirkelvormig': KeuzelijstWaarde(invulwaarde='cirkelvormig',
                                         label='cirkelvormig',
                                         status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                         definitie='Cirkelvormig',
                                         objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlRioleringVorm/cirkelvormig'),
        'cunette': KeuzelijstWaarde(invulwaarde='cunette',
                                    label='cunette',
                                    status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                    definitie='Cunette',
                                    objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlRioleringVorm/cunette'),
        'driehoekig': KeuzelijstWaarde(invulwaarde='driehoekig',
                                       label='driehoekig',
                                       status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                       definitie='Driehoekig',
                                       objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlRioleringVorm/driehoekig'),
        'eivormig': KeuzelijstWaarde(invulwaarde='eivormig',
                                     label='eivormig',
                                     status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                     definitie='Eivormig',
                                     objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlRioleringVorm/eivormig'),
        'gewelf': KeuzelijstWaarde(invulwaarde='gewelf',
                                   label='gewelf',
                                   status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                   definitie='Gewelf',
                                   objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlRioleringVorm/gewelf'),
        'ovaal': KeuzelijstWaarde(invulwaarde='ovaal',
                                  label='ovaal',
                                  status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                  definitie='Ovaal',
                                  objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlRioleringVorm/ovaal'),
        'rechthoekig': KeuzelijstWaarde(invulwaarde='rechthoekig',
                                        label='rechthoekig',
                                        status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                        definitie='Rechthoekig',
                                        objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlRioleringVorm/rechthoekig'),
        'u-vorm': KeuzelijstWaarde(invulwaarde='u-vorm',
                                   label='u-vorm',
                                   status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                   definitie='U-vorm',
                                   objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlRioleringVorm/u-vorm'),
        'vierkant': KeuzelijstWaarde(invulwaarde='vierkant',
                                     label='vierkant',
                                     status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                     definitie='Vierkant',
                                     objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlRioleringVorm/vierkant'),
        'zeshoekig': KeuzelijstWaarde(invulwaarde='zeshoekig',
                                      label='zeshoekig',
                                      status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                      definitie='Zeshoekig',
                                      objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlRioleringVorm/zeshoekig')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

