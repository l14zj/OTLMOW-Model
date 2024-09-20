# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlTelecommunicationsAppurtenanceType(KeuzelijstField):
    """Lijst van types voor telecommunications appurtenance."""
    naam = 'KlTelecommunicationsAppurtenanceType'
    label = 'Telecommunications appurtenance type'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#KlTelecommunicationsAppurtenanceType'
    definition = 'Lijst van types voor telecommunications appurtenance.'
    status = 'https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlTelecommunicationsAppurtenanceType'
    options = {
        'spliceclosure': KeuzelijstWaarde(invulwaarde='spliceclosure',
                                          label='spliceClosure',
                                          status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                          objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlTelecommunicationsAppurtenanceType/spliceclosure'),
        'termination': KeuzelijstWaarde(invulwaarde='termination',
                                        label='termination',
                                        status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                        objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlTelecommunicationsAppurtenanceType/termination')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

