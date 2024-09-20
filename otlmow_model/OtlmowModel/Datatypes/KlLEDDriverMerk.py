# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlLEDDriverMerk(KeuzelijstField):
    """Het merk van de LED-driver."""
    naam = 'KlLEDDriverMerk'
    label = 'LED-driver merk'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlLEDDriverMerk'
    definition = 'Het merk van de LED-driver.'
    status = 'https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlLEDDriverMerk'
    options = {
        'mean-well': KeuzelijstWaarde(invulwaarde='mean-well',
                                      label='mean-well',
                                      status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                      definitie='mean-well',
                                      objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlLEDDriverMerk/mean-well')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

