# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlCameraMerk(KeuzelijstField):
    """Het merk van de camera."""
    naam = 'KlCameraMerk'
    label = 'Camera merk'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlCameraMerk'
    definition = 'Het merk van de camera.'
    status = 'https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlCameraMerk'
    options = {
        'bosch': KeuzelijstWaarde(invulwaarde='bosch',
                                  label='Bosch',
                                  status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                  definitie='Bosch',
                                  objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlCameraMerk/bosch'),
        'macq': KeuzelijstWaarde(invulwaarde='macq',
                                 label='Macq',
                                 status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                 definitie='Macq',
                                 objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlCameraMerk/macq'),
        'videotec': KeuzelijstWaarde(invulwaarde='videotec',
                                     label='Videotec',
                                     status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                     definitie='Videotec',
                                     objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlCameraMerk/videotec')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

