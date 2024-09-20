# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlRetroreflecterendVerkeersbordGrootteorde(KeuzelijstField):
    """Opties om de grootteorde van een RetroreflecterendVerkeersbord aan te geven zoals gedefinieerd in SB250."""
    naam = 'KlRetroreflecterendVerkeersbordGrootteorde'
    label = 'Retroreflecterend verkeersbord grootteorde'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlRetroreflecterendVerkeersbordGrootteorde'
    definition = 'Opties om de grootteorde van een RetroreflecterendVerkeersbord aan te geven zoals gedefinieerd in SB250.'
    status = 'https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlRetroreflecterendVerkeersbordGrootteorde'
    options = {
        'groot': KeuzelijstWaarde(invulwaarde='groot',
                                  label='groot',
                                  status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                  objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlRetroreflecterendVerkeersbordGrootteorde/groot'),
        'klein': KeuzelijstWaarde(invulwaarde='klein',
                                  label='klein',
                                  status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                  objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlRetroreflecterendVerkeersbordGrootteorde/klein'),
        'middelgroot': KeuzelijstWaarde(invulwaarde='middelgroot',
                                        label='middelgroot',
                                        status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                        objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlRetroreflecterendVerkeersbordGrootteorde/middelgroot')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

