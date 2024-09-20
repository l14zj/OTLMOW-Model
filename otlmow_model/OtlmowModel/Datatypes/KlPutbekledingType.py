# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlPutbekledingType(KeuzelijstField):
    """Types van putbekleding."""
    naam = 'KlPutbekledingType'
    label = 'Putbekleding type'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlPutbekledingType'
    definition = 'Types van putbekleding.'
    status = 'https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlPutbekledingType'
    options = {
        'solventvrije-kunsthars': KeuzelijstWaarde(invulwaarde='solventvrije-kunsthars',
                                                   label='solventvrije kunsthars',
                                                   status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                                   definitie='solventvrije kunsthars',
                                                   objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlPutbekledingType/solventvrije-kunsthars'),
        'solventvrije-vezelversterkte-epoxyhars': KeuzelijstWaarde(invulwaarde='solventvrije-vezelversterkte-epoxyhars',
                                                                   label='solventvrije vezelversterkte epoxyhars',
                                                                   status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                                                   definitie='solventvrije vezelversterkte epoxyhars',
                                                                   objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlPutbekledingType/solventvrije-vezelversterkte-epoxyhars')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

