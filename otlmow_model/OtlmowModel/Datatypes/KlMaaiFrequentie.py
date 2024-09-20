# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlMaaiFrequentie(KeuzelijstField):
    """Het aantal keer dat er gemaaid wordt per jaar."""
    naam = 'KlMaaiFrequentie'
    label = 'Maaifrequentie'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/levenscyclus#KlMaaiFrequentie'
    definition = 'Het aantal keer dat er gemaaid wordt per jaar.'
    status = 'https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlMaaiFrequentie'
    options = {
        '1': KeuzelijstWaarde(invulwaarde='1',
                              label='1',
                              status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                              definitie='EÃ©n keer per jaar maaien. ',
                              objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlMaaiFrequentie/1'),
        '1-2': KeuzelijstWaarde(invulwaarde='1-2',
                                label='1/2',
                                status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                definitie='EÃ©n keer om de twee jaar maaien. ',
                                objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlMaaiFrequentie/1-2'),
        '1-3': KeuzelijstWaarde(invulwaarde='1-3',
                                label='1/3',
                                status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                definitie='EÃ©n keer om de drie jaar maaien. ',
                                objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlMaaiFrequentie/1-3'),
        '10-15': KeuzelijstWaarde(invulwaarde='10-15',
                                  label='10-15',
                                  status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                  definitie='10 tot 15 keer per jaar maaien.',
                                  objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlMaaiFrequentie/10-15'),
        '2': KeuzelijstWaarde(invulwaarde='2',
                              label='2',
                              status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                              definitie='Twee keer per jaar maaien.',
                              objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlMaaiFrequentie/2'),
        '3': KeuzelijstWaarde(invulwaarde='3',
                              label='3',
                              status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                              definitie='Drie keer per jaar maaien.',
                              objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlMaaiFrequentie/3'),
        '4-6': KeuzelijstWaarde(invulwaarde='4-6',
                                label='4-6',
                                status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                definitie='Vier tot zes keer per jaar maaien.',
                                objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlMaaiFrequentie/4-6'),
        '7-9': KeuzelijstWaarde(invulwaarde='7-9',
                                label='7-9',
                                status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                definitie='Zeven tot negen keer per jaar maaien.',
                                objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlMaaiFrequentie/7-9'),
        'minder-dan-1-3': KeuzelijstWaarde(invulwaarde='minder-dan-1-3',
                                           label='minder dan 1/3',
                                           status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                           definitie='Minder dan Ã©Ã©n keer om de drie jaar maaien. ',
                                           objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlMaaiFrequentie/minder-dan-1-3')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

