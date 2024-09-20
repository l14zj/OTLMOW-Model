# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlTransformatorTrafobeveiliging(KeuzelijstField):
    """Type transformatorbeveiliging."""
    naam = 'KlTransformatorTrafobeveiliging'
    label = 'Transformator trafobeveiliging'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlTransformatorTrafobeveiliging'
    definition = 'Type transformatorbeveiliging.'
    status = 'https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlTransformatorTrafobeveiliging'
    options = {
        'gecombineerd': KeuzelijstWaarde(invulwaarde='gecombineerd',
                                         label='gecombineerd',
                                         status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                         objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlTransformatorTrafobeveiliging/gecombineerd'),
        'overdruk': KeuzelijstWaarde(invulwaarde='overdruk',
                                     label='overdruk',
                                     status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                     objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlTransformatorTrafobeveiliging/overdruk'),
        'overtemperatuur': KeuzelijstWaarde(invulwaarde='overtemperatuur',
                                            label='overtemperatuur',
                                            status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                            definitie='attributen invullen//',
                                            objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlTransformatorTrafobeveiliging/overtemperatuur')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

