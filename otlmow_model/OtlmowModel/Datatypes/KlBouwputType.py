# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlBouwputType(KeuzelijstField):
    """Het type van bouwput."""
    naam = 'KlBouwputType'
    label = 'Bouwput type.'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlBouwputType'
    definition = 'Het type van bouwput.'
    status = 'https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlBouwputType'
    options = {
        'bouwput': KeuzelijstWaarde(invulwaarde='bouwput',
                                    label='bouwput',
                                    status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                    definitie='bouwput',
                                    objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlBouwputType/bouwput'),
        'intredeput': KeuzelijstWaarde(invulwaarde='intredeput',
                                       label='intredeput',
                                       status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                       definitie='intredeput',
                                       objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlBouwputType/intredeput'),
        'ontvangstput': KeuzelijstWaarde(invulwaarde='ontvangstput',
                                         label='ontvangstput',
                                         status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                         definitie='ontvangstput',
                                         objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlBouwputType/ontvangstput'),
        'persput': KeuzelijstWaarde(invulwaarde='persput',
                                    label='persput',
                                    status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                    definitie='persput',
                                    objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlBouwputType/persput')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

