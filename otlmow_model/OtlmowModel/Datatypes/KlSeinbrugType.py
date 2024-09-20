# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlSeinbrugType(KeuzelijstField):
    """Types van seinbrug."""
    naam = 'KlSeinbrugType'
    label = 'Seinbrug type'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlSeinbrugType'
    definition = 'Types van seinbrug.'
    status = 'https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlSeinbrugType'
    options = {
        'enkeleLigger': KeuzelijstWaarde(invulwaarde='enkeleLigger',
                                         label='enkeleLigger',
                                         status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                         objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlSeinbrugType/enkeleLigger'),
        'koker': KeuzelijstWaarde(invulwaarde='koker',
                                  label='koker',
                                  status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                  objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlSeinbrugType/koker'),
        'nietDoorlopendeBuis': KeuzelijstWaarde(invulwaarde='nietDoorlopendeBuis',
                                                label='nietDoorlopendeBuis',
                                                status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                                objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlSeinbrugType/nietDoorlopendeBuis'),
        'vakwerk': KeuzelijstWaarde(invulwaarde='vakwerk',
                                    label='vakwerk',
                                    status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                    objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlSeinbrugType/vakwerk')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

