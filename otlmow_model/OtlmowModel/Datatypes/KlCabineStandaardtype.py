# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlCabineStandaardtype(KeuzelijstField):
    """Veel voorkomende types van cabines."""
    naam = 'KlCabineStandaardtype'
    label = 'Cabine standaardtype'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlCabineStandaardtype'
    definition = 'Veel voorkomende types van cabines.'
    status = 'https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlCabineStandaardtype'
    options = {
        'aluminium-betreedbaar': KeuzelijstWaarde(invulwaarde='aluminium-betreedbaar',
                                                  label='aluminium betreedbaar',
                                                  status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                                  objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlCabineStandaardtype/aluminium-betreedbaar'),
        'aluminium-niet-betreedbaar': KeuzelijstWaarde(invulwaarde='aluminium-niet-betreedbaar',
                                                       label='aluminium niet betreedbaar',
                                                       status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                                       objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlCabineStandaardtype/aluminium-niet-betreedbaar'),
        'beton-betreedbaar': KeuzelijstWaarde(invulwaarde='beton-betreedbaar',
                                              label='beton betreedbaar',
                                              status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                              objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlCabineStandaardtype/beton-betreedbaar'),
        'beton-niet-betreedbaar-(compactstation)': KeuzelijstWaarde(invulwaarde='beton-niet-betreedbaar-(compactstation)',
                                                                    label='beton niet betreedbaar (compactstation)',
                                                                    status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                                                    objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlCabineStandaardtype/beton-niet-betreedbaar-(compactstation)'),
        'gemetst-betreedbaar': KeuzelijstWaarde(invulwaarde='gemetst-betreedbaar',
                                                label='gemetst betreedbaar',
                                                status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                                objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlCabineStandaardtype/gemetst-betreedbaar'),
        'kunststof-betreedbaar': KeuzelijstWaarde(invulwaarde='kunststof-betreedbaar',
                                                  label='kunststof betreedbaar',
                                                  status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                                  definitie='kunststof betreedbaar',
                                                  objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlCabineStandaardtype/kunststof-betreedbaar'),
        'lokaal-in-een-gebouw': KeuzelijstWaarde(invulwaarde='lokaal-in-een-gebouw',
                                                 label='lokaal in een gebouw',
                                                 status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                                 objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlCabineStandaardtype/lokaal-in-een-gebouw')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

