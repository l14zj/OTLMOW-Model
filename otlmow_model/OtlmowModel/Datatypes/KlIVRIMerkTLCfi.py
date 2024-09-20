# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlIVRIMerkTLCfi(KeuzelijstField):
    """Het merk van de TLC-fi poort."""
    naam = 'KlIVRIMerkTLCfi'
    label = 'iVRIMerkTLCfi'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlIVRIMerkTLCfi'
    definition = 'Het merk van de TLC-fi poort.'
    status = 'https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlIVRIMerkTLCfi'
    options = {
        'dynniq': KeuzelijstWaarde(invulwaarde='dynniq',
                                   label='Dynniq',
                                   status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                   definitie='Dynniq',
                                   objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlIVRIMerkTLCfi/dynniq'),
        'ko-hartog': KeuzelijstWaarde(invulwaarde='ko-hartog',
                                      label='Ko Hartog',
                                      status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                      definitie='Ko Hartog',
                                      objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlIVRIMerkTLCfi/ko-hartog'),
        'ko-hartogs': KeuzelijstWaarde(invulwaarde='ko-hartogs',
                                       label='Ko Hartogs',
                                       status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                       definitie='Ko Hartogs',
                                       objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlIVRIMerkTLCfi/ko-hartogs'),
        'siemens': KeuzelijstWaarde(invulwaarde='siemens',
                                    label='Siemens',
                                    status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                    definitie='Siemens',
                                    objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlIVRIMerkTLCfi/siemens'),
        'swarco': KeuzelijstWaarde(invulwaarde='swarco',
                                   label='Swarco',
                                   status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                   definitie='Swarco (voorheen Dynniq)',
                                   objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlIVRIMerkTLCfi/swarco'),
        'yunex': KeuzelijstWaarde(invulwaarde='yunex',
                                  label='Yunex',
                                  status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                  definitie='Yunex',
                                  objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlIVRIMerkTLCfi/yunex')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

