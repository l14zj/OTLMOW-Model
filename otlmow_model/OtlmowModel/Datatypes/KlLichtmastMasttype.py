# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlLichtmastMasttype(KeuzelijstField):
    """Lijst van mogelijke types voor lichtmasten."""
    naam = 'KlLichtmastMasttype'
    label = 'lichtmast type'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlLichtmastMasttype'
    definition = 'Lijst van mogelijke types voor lichtmasten.'
    status = 'https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlLichtmastMasttype'
    options = {
        'B': KeuzelijstWaarde(invulwaarde='B',
                              label='B',
                              status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                              definitie='Betonnen paal',
                              objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlLichtmastMasttype/B'),
        'BS': KeuzelijstWaarde(invulwaarde='BS',
                               label='BS',
                               status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                               definitie='Betonnen paal op voet',
                               objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlLichtmastMasttype/BS'),
        'K': KeuzelijstWaarde(invulwaarde='K',
                              label='K',
                              status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                              definitie='Kreukelpaal met arm',
                              objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlLichtmastMasttype/K'),
        'KS': KeuzelijstWaarde(invulwaarde='KS',
                               label='KS',
                               status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                               definitie='Kreukelpaal met arm op voet',
                               objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlLichtmastMasttype/KS'),
        'M': KeuzelijstWaarde(invulwaarde='M',
                              label='M',
                              status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                              definitie='Metalen paal met arm',
                              objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlLichtmastMasttype/M'),
        'MS': KeuzelijstWaarde(invulwaarde='MS',
                               label='MS',
                               status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                               definitie='Metalen paal met arm en voet',
                               objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlLichtmastMasttype/MS'),
        'RK': KeuzelijstWaarde(invulwaarde='RK',
                               label='RK',
                               status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                               definitie='Kreukelpaal',
                               objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlLichtmastMasttype/RK'),
        'RKS': KeuzelijstWaarde(invulwaarde='RKS',
                                label='RKS',
                                status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                definitie='Kreukelpaal op voet',
                                objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlLichtmastMasttype/RKS'),
        'RM': KeuzelijstWaarde(invulwaarde='RM',
                               label='RM',
                               status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                               definitie='Rechte metalen paal',
                               objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlLichtmastMasttype/RM'),
        'RMS': KeuzelijstWaarde(invulwaarde='RMS',
                                label='RMS',
                                status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                definitie='Rechte metalen paal op voet',
                                objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlLichtmastMasttype/RMS')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

