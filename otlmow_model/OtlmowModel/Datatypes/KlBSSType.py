# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlBSSType(KeuzelijstField):
    """Types van betonstraatsteen en betontegel."""
    naam = 'KlBSSType'
    label = 'BSS type'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlBSSType'
    definition = 'Types van betonstraatsteen en betontegel.'
    status = 'https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlBSSType'
    options = {
        'gekleurde-met-anorganische-pigmenten': KeuzelijstWaarde(invulwaarde='gekleurde-met-anorganische-pigmenten',
                                                                 label='gekleurde met anorganische pigmenten',
                                                                 status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                                                 definitie='Gekleurde betonstraatstenen met anorganische pigmenten.',
                                                                 objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlBSSType/gekleurde-met-anorganische-pigmenten'),
        'gekleurde-met-kleurondersteunende-granulaten': KeuzelijstWaarde(invulwaarde='gekleurde-met-kleurondersteunende-granulaten',
                                                                         label='gekleurde met kleurondersteunende granulaten',
                                                                         status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                                                         definitie='Gekleurde betonstraatstenen met kleurondersteunende granulaten.',
                                                                         objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlBSSType/gekleurde-met-kleurondersteunende-granulaten'),
        'grijze': KeuzelijstWaarde(invulwaarde='grijze',
                                   label='grijze',
                                   status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                   definitie='Grijze betonstraatstenen.',
                                   objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlBSSType/grijze'),
        'witte-met-kleurondersteunende-granulaten': KeuzelijstWaarde(invulwaarde='witte-met-kleurondersteunende-granulaten',
                                                                     label='witte met kleurondersteunende granulaten',
                                                                     status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                                                     definitie='Witte betonstraatstenen met kleurondersteunende granulaten.',
                                                                     objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlBSSType/witte-met-kleurondersteunende-granulaten')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

