# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlLEGCOpeningType(KeuzelijstField):
    """Types van opening."""
    naam = 'KlLEGCOpeningType'
    label = 'Opening type'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlLEGCOpeningType'
    definition = 'Types van opening.'
    status = 'https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik'
    deprecated_version = '2.1.0'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlLEGCOpeningType'
    options = {
        'dienstopening': KeuzelijstWaarde(invulwaarde='dienstopening',
                                          label='dienstopening',
                                          status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/verwijderd',
                                          definitie='dienstopening',
                                          objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlLEGCOpeningType/dienstopening'),
        'nooddeur': KeuzelijstWaarde(invulwaarde='nooddeur',
                                     label='nooddeur',
                                     status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/verwijderd',
                                     definitie='nooddeur',
                                     objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlLEGCOpeningType/nooddeur'),
        'sas': KeuzelijstWaarde(invulwaarde='sas',
                                label='sas',
                                status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/verwijderd',
                                definitie='sas',
                                objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlLEGCOpeningType/sas'),
        'vluchtopening': KeuzelijstWaarde(invulwaarde='vluchtopening',
                                          label='vluchtopening',
                                          status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/verwijderd',
                                          definitie='vluchtopening',
                                          objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlLEGCOpeningType/vluchtopening')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

