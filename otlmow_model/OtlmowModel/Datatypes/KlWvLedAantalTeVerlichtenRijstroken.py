# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlWvLedAantalTeVerlichtenRijstroken(KeuzelijstField):
    """Het aantal rijstroken dat verlicht wordt door het LED verlichtingstoestel."""
    naam = 'KlWvLedAantalTeVerlichtenRijstroken'
    label = 'WV LED aantal te verlichten rijstroken'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlWvLedAantalTeVerlichtenRijstroken'
    definition = 'Het aantal rijstroken dat verlicht wordt door het LED verlichtingstoestel.'
    status = 'https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlWvLedAantalTeVerlichtenRijstroken'
    options = {
        '1': KeuzelijstWaarde(invulwaarde='1',
                              label='1',
                              status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                              definitie='1',
                              objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlWvLedAantalTeVerlichtenRijstroken/1'),
        '2': KeuzelijstWaarde(invulwaarde='2',
                              label='2',
                              status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                              definitie='2',
                              objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlWvLedAantalTeVerlichtenRijstroken/2'),
        '3': KeuzelijstWaarde(invulwaarde='3',
                              label='3',
                              status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                              definitie='3',
                              objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlWvLedAantalTeVerlichtenRijstroken/3'),
        '4': KeuzelijstWaarde(invulwaarde='4',
                              label='4',
                              status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                              definitie='4',
                              objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlWvLedAantalTeVerlichtenRijstroken/4'),
        '5': KeuzelijstWaarde(invulwaarde='5',
                              label='5',
                              status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                              definitie='5',
                              objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlWvLedAantalTeVerlichtenRijstroken/5'),
        '6': KeuzelijstWaarde(invulwaarde='6',
                              label='6',
                              status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                              definitie='6',
                              objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlWvLedAantalTeVerlichtenRijstroken/6'),
        'R1': KeuzelijstWaarde(invulwaarde='R1',
                               label='R1',
                               status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/uitgebruik',
                               definitie='R1',
                               objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlWvLedAantalTeVerlichtenRijstroken/R1'),
        'R2': KeuzelijstWaarde(invulwaarde='R2',
                               label='R2',
                               status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/uitgebruik',
                               definitie='R2',
                               objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlWvLedAantalTeVerlichtenRijstroken/R2'),
        'R3': KeuzelijstWaarde(invulwaarde='R3',
                               label='R3',
                               status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/uitgebruik',
                               definitie='R3',
                               objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlWvLedAantalTeVerlichtenRijstroken/R3'),
        'R4': KeuzelijstWaarde(invulwaarde='R4',
                               label='R4',
                               status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/uitgebruik',
                               definitie='R4',
                               objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlWvLedAantalTeVerlichtenRijstroken/R4'),
        'R5': KeuzelijstWaarde(invulwaarde='R5',
                               label='R5',
                               status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/uitgebruik',
                               definitie='R5',
                               objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlWvLedAantalTeVerlichtenRijstroken/R5'),
        'R6': KeuzelijstWaarde(invulwaarde='R6',
                               label='R6',
                               status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/uitgebruik',
                               definitie='R6',
                               objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlWvLedAantalTeVerlichtenRijstroken/R6')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

