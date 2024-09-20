# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlBestratingSteenverband(KeuzelijstField):
    """De steenverbanden van de bestrating."""
    naam = 'KlBestratingSteenverband'
    label = 'Bestrating steenverband'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlBestratingSteenverband'
    definition = 'De steenverbanden van de bestrating.'
    status = 'https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlBestratingSteenverband'
    options = {
        'blokverband': KeuzelijstWaarde(invulwaarde='blokverband',
                                        label='blokverband',
                                        status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                        definitie='Blokverband',
                                        objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlBestratingSteenverband/blokverband'),
        'elleboogverband': KeuzelijstWaarde(invulwaarde='elleboogverband',
                                            label='elleboogverband',
                                            status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                            definitie='Elleboogverband',
                                            objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlBestratingSteenverband/elleboogverband'),
        'halfsteensverband': KeuzelijstWaarde(invulwaarde='halfsteensverband',
                                              label='halfsteensverband',
                                              status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                              definitie='Halfsteensverband',
                                              objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlBestratingSteenverband/halfsteensverband'),
        'keperverband': KeuzelijstWaarde(invulwaarde='keperverband',
                                         label='keperverband',
                                         status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                         definitie='Keperverband',
                                         objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlBestratingSteenverband/keperverband'),
        'schelpen--of-pauwstaartverband': KeuzelijstWaarde(invulwaarde='schelpen--of-pauwstaartverband',
                                                           label='schelpen- of pauwstaartverband',
                                                           status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                                           definitie='Schelpen- of pauwstaartverband',
                                                           objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlBestratingSteenverband/schelpen--of-pauwstaartverband'),
        'schubbenverband': KeuzelijstWaarde(invulwaarde='schubbenverband',
                                            label='schubbenverband',
                                            status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                            definitie='Schubbenverband',
                                            objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlBestratingSteenverband/schubbenverband'),
        'segmentverband': KeuzelijstWaarde(invulwaarde='segmentverband',
                                           label='segmentverband',
                                           status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                           definitie='Segmentverband',
                                           objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlBestratingSteenverband/segmentverband'),
        'visgraatverband': KeuzelijstWaarde(invulwaarde='visgraatverband',
                                            label='visgraatverband',
                                            status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                            definitie='Visgraatverband',
                                            objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlBestratingSteenverband/visgraatverband'),
        'waaierverband': KeuzelijstWaarde(invulwaarde='waaierverband',
                                          label='waaierverband',
                                          status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                          definitie='Waaierverband',
                                          objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlBestratingSteenverband/waaierverband')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

