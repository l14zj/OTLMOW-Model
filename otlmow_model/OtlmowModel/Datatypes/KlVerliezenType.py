# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlVerliezenType(KeuzelijstField):
    """Aanduiding van het type verliezen."""
    naam = 'KlVerliezenType'
    label = 'Type verliezen'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlVerliezenType'
    definition = 'Aanduiding van het type verliezen.'
    status = 'https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlVerliezenType'
    options = {
        'a0ak': KeuzelijstWaarde(invulwaarde='a0ak',
                                 label='A0Ak',
                                 status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                 definitie='A0Ak',
                                 objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlVerliezenType/a0ak'),
        'a0bk': KeuzelijstWaarde(invulwaarde='a0bk',
                                 label='A0Bk',
                                 status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                 definitie='A0Bk',
                                 objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlVerliezenType/a0bk'),
        'a0ck': KeuzelijstWaarde(invulwaarde='a0ck',
                                 label='A0Ck',
                                 status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                 definitie='A0Ck',
                                 objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlVerliezenType/a0ck'),
        'b0ak': KeuzelijstWaarde(invulwaarde='b0ak',
                                 label='B0Ak',
                                 status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                 definitie='B0Ak',
                                 objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlVerliezenType/b0ak'),
        'b0bk': KeuzelijstWaarde(invulwaarde='b0bk',
                                 label='B0Bk',
                                 status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                 definitie='B0Bk',
                                 objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlVerliezenType/b0bk'),
        'b0ck': KeuzelijstWaarde(invulwaarde='b0ck',
                                 label='B0Ck',
                                 status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                 definitie='B0Ck',
                                 objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlVerliezenType/b0ck')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

