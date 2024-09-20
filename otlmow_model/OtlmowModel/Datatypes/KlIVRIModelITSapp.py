# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlIVRIModelITSapp(KeuzelijstField):
    """De modelnaam van de ITSapp."""
    naam = 'KlIVRIModelITSapp'
    label = 'iVRIModelITSapp'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlIVRIModelITSapp'
    definition = 'De modelnaam van de ITSapp.'
    status = 'https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlIVRIModelITSapp'
    options = {
        'flowtack': KeuzelijstWaarde(invulwaarde='flowtack',
                                     label='Flowtack',
                                     status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                     definitie='Flowtack',
                                     objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlIVRIModelITSapp/flowtack'),
        'imflow': KeuzelijstWaarde(invulwaarde='imflow',
                                   label='Imflow',
                                   status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                   definitie='Imflow',
                                   objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlIVRIModelITSapp/imflow')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

