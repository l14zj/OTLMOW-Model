# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlContactpuntModelnaam(KeuzelijstField):
    """Lijst van modelnamen van contactpunten volgens de fabrikant."""
    naam = 'KlContactpuntModelnaam'
    label = 'Modelnamen contactpunten'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlContactpuntModelnaam'
    definition = 'Lijst van modelnamen van contactpunten volgens de fabrikant.'
    status = 'https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlContactpuntModelnaam'
    options = {
        'aritech-dc-107': KeuzelijstWaarde(invulwaarde='aritech-dc-107',
                                           label='aritech-dc-107',
                                           status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                           definitie='aritech-dc-107',
                                           objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlContactpuntModelnaam/aritech-dc-107')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

