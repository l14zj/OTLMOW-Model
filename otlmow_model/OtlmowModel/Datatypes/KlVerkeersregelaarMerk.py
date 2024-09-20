# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlVerkeersregelaarMerk(KeuzelijstField):
    """Keuzelijst met merknamen voor Verkeersregelaar."""
    naam = 'KlVerkeersregelaarMerk'
    label = 'verkeersregelaar merk'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlVerkeersregelaarMerk'
    definition = 'Keuzelijst met merknamen voor Verkeersregelaar.'
    status = 'https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlVerkeersregelaarMerk'
    options = {
        'dynniq': KeuzelijstWaarde(invulwaarde='dynniq',
                                   label='Dynniq',
                                   status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                   definitie='Dynniq',
                                   objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlVerkeersregelaarMerk/dynniq'),
        'ko-hartog': KeuzelijstWaarde(invulwaarde='ko-hartog',
                                      label='Ko Hartog',
                                      status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                      definitie='Ko Hartog',
                                      objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlVerkeersregelaarMerk/ko-hartog'),
        'peek': KeuzelijstWaarde(invulwaarde='peek',
                                 label='Peek',
                                 status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                 definitie='Peek',
                                 objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlVerkeersregelaarMerk/peek'),
        'siemens': KeuzelijstWaarde(invulwaarde='siemens',
                                    label='Siemens',
                                    status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                    definitie='Siemens',
                                    objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlVerkeersregelaarMerk/siemens'),
        'swarco': KeuzelijstWaarde(invulwaarde='swarco',
                                   label='Swarco',
                                   status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                   definitie='Swarco (voorheen Dynniq)',
                                   objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlVerkeersregelaarMerk/swarco'),
        'yunex': KeuzelijstWaarde(invulwaarde='yunex',
                                  label='Yunex',
                                  status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                  definitie='Yunex',
                                  objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlVerkeersregelaarMerk/yunex')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

