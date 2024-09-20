# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlOmvormerMerk(KeuzelijstField):
    """Het merk van de omvormer."""
    naam = 'KlOmvormerMerk'
    label = 'Omvormer merk'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlOmvormerMerk'
    definition = 'Het merk van de omvormer.'
    status = 'https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlOmvormerMerk'
    options = {
        'axis': KeuzelijstWaarde(invulwaarde='axis',
                                 label='Axis',
                                 status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                 definitie='Axis',
                                 objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlOmvormerMerk/axis'),
        'bosch': KeuzelijstWaarde(invulwaarde='bosch',
                                  label='Bosch',
                                  status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                  definitie='Bosch',
                                  objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlOmvormerMerk/bosch')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

