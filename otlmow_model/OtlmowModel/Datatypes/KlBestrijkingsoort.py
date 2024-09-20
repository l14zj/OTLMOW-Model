# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlBestrijkingsoort(KeuzelijstField):
    """Soorten van bestrijking."""
    naam = 'KlBestrijkingsoort'
    label = 'Bestrijkingsoort'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlBestrijkingsoort'
    definition = 'Soorten van bestrijking.'
    status = 'https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlBestrijkingsoort'
    options = {
        'eenlaagse-met-dubbele-begrinding-(EBDB)': KeuzelijstWaarde(invulwaarde='eenlaagse-met-dubbele-begrinding-(EBDB)',
                                                                    label='eenlaagse met dubbele begrinding (EBDB)',
                                                                    status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                                                    definitie='Ã©Ã©nlaagse bestrijking met dubbele begrinding (EBDB).',
                                                                    objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlBestrijkingsoort/eenlaagse-met-dubbele-begrinding-(EBDB)'),
        'eenlaagse-met-enkele-begrinding-(EBEB)': KeuzelijstWaarde(invulwaarde='eenlaagse-met-enkele-begrinding-(EBEB)',
                                                                   label='eenlaagse met enkele begrinding (EBEB)',
                                                                   status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                                                   definitie='Ã©Ã©nlaagse bestrijking met enkele begrinding (EBEB).',
                                                                   objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlBestrijkingsoort/eenlaagse-met-enkele-begrinding-(EBEB)'),
        'tweelaagse-(TB)': KeuzelijstWaarde(invulwaarde='tweelaagse-(TB)',
                                            label='tweelaagse (TB)',
                                            status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                            definitie='tweelaagse bestrijking (TB)',
                                            objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlBestrijkingsoort/tweelaagse-(TB)')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

