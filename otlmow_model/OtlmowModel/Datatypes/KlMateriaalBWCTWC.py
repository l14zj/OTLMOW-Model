# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlMateriaalBWCTWC(KeuzelijstField):
    """De mogelijke materialen voor een beweegbare waterkerende constructie of een tijdelijke waterkerende constructie."""
    naam = 'KlMateriaalBWCTWC'
    label = 'Materiaal BWC TWC'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#KlMateriaalBWCTWC'
    definition = 'De mogelijke materialen voor een beweegbare waterkerende constructie of een tijdelijke waterkerende constructie.'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlMateriaalBWCTWC'
    options = {
        'aluminium': KeuzelijstWaarde(invulwaarde='aluminium',
                                      label='aluminium',
                                      status='ingebruik',
                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlMateriaalBWCTWC/aluminium'),
        'beton': KeuzelijstWaarde(invulwaarde='beton',
                                  label='beton',
                                  status='ingebruik',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlMateriaalBWCTWC/beton'),
        'hout': KeuzelijstWaarde(invulwaarde='hout',
                                 label='hout',
                                 status='ingebruik',
                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlMateriaalBWCTWC/hout'),
        'houtvezelbeton': KeuzelijstWaarde(invulwaarde='houtvezelbeton',
                                           label='houtvezelbeton',
                                           status='ingebruik',
                                           objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlMateriaalBWCTWC/houtvezelbeton'),
        'kunststof': KeuzelijstWaarde(invulwaarde='kunststof',
                                      label='kunststof',
                                      status='ingebruik',
                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlMateriaalBWCTWC/kunststof'),
        'roestvaststaal': KeuzelijstWaarde(invulwaarde='roestvaststaal',
                                           label='roestvaststaal',
                                           status='ingebruik',
                                           objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlMateriaalBWCTWC/roestvaststaal'),
        'roestvrijstaal': KeuzelijstWaarde(invulwaarde='roestvrijstaal',
                                           label='roestvrijstaal',
                                           status='ingebruik',
                                           objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlMateriaalBWCTWC/roestvrijstaal'),
        'staal': KeuzelijstWaarde(invulwaarde='staal',
                                  label='staal',
                                  status='ingebruik',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlMateriaalBWCTWC/staal')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

