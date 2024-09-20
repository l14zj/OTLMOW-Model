# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlAantalBoompalen(KeuzelijstField):
    """Hoeveelheid palen waaruit de constructie bestaat."""
    naam = 'KlAantalBoompalen'
    label = 'Aantal boompalen'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlAantalBoompalen'
    definition = 'Hoeveelheid palen waaruit de constructie bestaat.'
    status = 'https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlAantalBoompalen'
    options = {
        '1': KeuzelijstWaarde(invulwaarde='1',
                              label='1',
                              status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                              definitie='De constructie bestaat uit 1 boompaal.',
                              objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAantalBoompalen/1'),
        '2': KeuzelijstWaarde(invulwaarde='2',
                              label='2',
                              status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                              definitie='De constructie bestaat uit 2 boompalen.',
                              objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAantalBoompalen/2'),
        '3': KeuzelijstWaarde(invulwaarde='3',
                              label='3',
                              status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                              definitie='De constructie bestaat uit 3 boompalen.',
                              objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAantalBoompalen/3'),
        '4': KeuzelijstWaarde(invulwaarde='4',
                              label='4',
                              status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                              definitie='De constructie bestaat uit 4 boompalen.',
                              objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAantalBoompalen/4'),
        '5': KeuzelijstWaarde(invulwaarde='5',
                              label='5',
                              status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                              definitie='De constructie bestaat uit 5 boompalen.',
                              objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAantalBoompalen/5'),
        '6': KeuzelijstWaarde(invulwaarde='6',
                              label='6',
                              status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                              definitie='test',
                              objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAantalBoompalen/6'),
        'een-waarde-met-d': KeuzelijstWaarde(invulwaarde='een-waarde-met-d',
                                             label='een waarde',
                                             status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                             definitie='een waarde met',
                                             objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAantalBoompalen/een-waarde-met-d'),
        'het-label-zo-tonen': KeuzelijstWaarde(invulwaarde='het-label-zo-tonen',
                                               label='Het $label_zo/tonen',
                                               status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                               definitie='Het $label_zo/tonen',
                                               objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAantalBoompalen/het-label-zo-tonen')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

