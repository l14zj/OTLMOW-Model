# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlLEGCSchermelementType(KeuzelijstField):
    """Schermelement types."""
    naam = 'KlLEGCSchermelementType'
    label = 'Schermelement type'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlLEGCSchermelementType'
    definition = 'Schermelement types.'
    status = 'https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik'
    deprecated_version = '2.0.0'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlLEGCSchermelementType'
    options = {
        'bloembakelement': KeuzelijstWaarde(invulwaarde='bloembakelement',
                                            label='bloembakelement',
                                            status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                            definitie='bloembakelement',
                                            objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlLEGCSchermelementType/bloembakelement'),
        'l-element': KeuzelijstWaarde(invulwaarde='l-element',
                                      label='l-element',
                                      status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                      definitie='l-element',
                                      objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlLEGCSchermelementType/l-element'),
        'schermelement-tussen-palen': KeuzelijstWaarde(invulwaarde='schermelement-tussen-palen',
                                                       label='schermelement tussen palen',
                                                       status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                                       definitie='schermelement tussen palen',
                                                       objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlLEGCSchermelementType/schermelement-tussen-palen'),
        'voertuigkerend': KeuzelijstWaarde(invulwaarde='voertuigkerend',
                                           label='voertuigkerend',
                                           status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                           definitie='voertuigkerend',
                                           objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlLEGCSchermelementType/voertuigkerend')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

