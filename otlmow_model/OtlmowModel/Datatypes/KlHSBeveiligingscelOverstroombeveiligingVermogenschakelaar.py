# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlHSBeveiligingscelOverstroombeveiligingVermogenschakelaar(KeuzelijstField):
    """Directe of indirecte overstroombeveiliging van de vermogenschakelaar."""
    naam = 'KlHSBeveiligingscelOverstroombeveiligingVermogenschakelaar'
    label = 'HS-beveiligingscel overstroombeveiliging vermogenschakelaar'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlHSBeveiligingscelOverstroombeveiligingVermogenschakelaar'
    definition = 'Directe of indirecte overstroombeveiliging van de vermogenschakelaar.'
    status = 'https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlHSBeveiligingscelOverstroombeveiligingVermogenschakelaar'
    options = {
        'direct': KeuzelijstWaarde(invulwaarde='direct',
                                   label='direct',
                                   status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                   objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlHSBeveiligingscelOverstroombeveiligingVermogenschakelaar/direct'),
        'indirect': KeuzelijstWaarde(invulwaarde='indirect',
                                     label='indirect',
                                     status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                     objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlHSBeveiligingscelOverstroombeveiligingVermogenschakelaar/indirect')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

