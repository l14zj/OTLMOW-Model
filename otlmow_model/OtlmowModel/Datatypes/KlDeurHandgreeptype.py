# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlDeurHandgreeptype(KeuzelijstField):
    """Types handgrepen van deuren."""
    naam = 'KlDeurHandgreeptype'
    label = 'Deur handgreeptype'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#KlDeurHandgreeptype'
    definition = 'Types handgrepen van deuren.'
    status = 'https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlDeurHandgreeptype'
    options = {
        'handvat': KeuzelijstWaarde(invulwaarde='handvat',
                                    label='handvat',
                                    status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                    objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlDeurHandgreeptype/handvat'),
        'hendel-RWS': KeuzelijstWaarde(invulwaarde='hendel-RWS',
                                       label='hendel RWS',
                                       status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                       objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlDeurHandgreeptype/hendel-RWS'),
        'klink': KeuzelijstWaarde(invulwaarde='klink',
                                  label='klink',
                                  status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                  objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlDeurHandgreeptype/klink')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

