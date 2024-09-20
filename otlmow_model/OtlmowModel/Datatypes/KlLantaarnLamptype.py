# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlLantaarnLamptype(KeuzelijstField):
    """Keuzelijst met LantaarnLamp types."""
    naam = 'KlLantaarnLamptype'
    label = 'Lantaarn lamptype'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#KlLantaarnLamptype'
    definition = 'Keuzelijst met LantaarnLamp types.'
    status = 'https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlLantaarnLamptype'
    options = {
        'LED': KeuzelijstWaarde(invulwaarde='LED',
                                label='LED',
                                status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                definitie='Led lamp.',
                                objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlLantaarnLamptype/LED'),
        'gasontlading': KeuzelijstWaarde(invulwaarde='gasontlading',
                                         label='gasontlading',
                                         status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                         definitie='Lamp op basis van gas.',
                                         objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlLantaarnLamptype/gasontlading'),
        'gloeilamp': KeuzelijstWaarde(invulwaarde='gloeilamp',
                                      label='gloeilamp',
                                      status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                      definitie='Gloeilamp.',
                                      objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlLantaarnLamptype/gloeilamp'),
        'halogeen': KeuzelijstWaarde(invulwaarde='halogeen',
                                     label='halogeen',
                                     status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                     definitie='Halogeenlamp.',
                                     objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlLantaarnLamptype/halogeen')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

