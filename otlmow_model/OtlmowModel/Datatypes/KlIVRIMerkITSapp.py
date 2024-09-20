# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlIVRIMerkITSapp(KeuzelijstField):
    """Het merk van de ITSapp."""
    naam = 'KlIVRIMerkITSapp'
    label = 'iVRIMerkITSapp'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlIVRIMerkITSapp'
    definition = 'Het merk van de ITSapp.'
    status = 'https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlIVRIMerkITSapp'
    options = {
        'peek': KeuzelijstWaarde(invulwaarde='peek',
                                 label='Peek',
                                 status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                 definitie='Peek',
                                 objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlIVRIMerkITSapp/peek'),
        'rhdhv': KeuzelijstWaarde(invulwaarde='rhdhv',
                                  label='RHDHV',
                                  status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                  definitie='RHDHV',
                                  objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlIVRIMerkITSapp/rhdhv')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

