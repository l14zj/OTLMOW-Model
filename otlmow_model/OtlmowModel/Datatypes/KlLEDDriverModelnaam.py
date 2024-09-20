# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlLEDDriverModelnaam(KeuzelijstField):
    """De modelnaam van de LED-driver."""
    naam = 'KlLEDDriverModelnaam'
    label = 'LED-driver modelnaam'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlLEDDriverModelnaam'
    definition = 'De modelnaam van de LED-driver.'
    status = 'https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlLEDDriverModelnaam'
    options = {
        'elg-100-c350b-3y': KeuzelijstWaarde(invulwaarde='elg-100-c350b-3y',
                                             label='elg-100-c350b-3y',
                                             status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                             definitie='elg-100-c350b-3y',
                                             objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlLEDDriverModelnaam/elg-100-c350b-3y')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

