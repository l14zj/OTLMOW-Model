# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlKabelLeidingBescherming(KeuzelijstField):
    """Lijst met mogelijke types bijkomende mechanische bescherming van kabels of leidingen."""
    naam = 'KlKabelLeidingBescherming'
    label = 'Kabels en Leidingen bescherming'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlKabelLeidingBescherming'
    definition = 'Lijst met mogelijke types bijkomende mechanische bescherming van kabels of leidingen.'
    status = 'https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlKabelLeidingBescherming'
    options = {
        'kabeldekband': KeuzelijstWaarde(invulwaarde='kabeldekband',
                                         label='kabeldekband',
                                         status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                         objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlKabelLeidingBescherming/kabeldekband'),
        'mager-beton': KeuzelijstWaarde(invulwaarde='mager-beton',
                                        label='mager beton',
                                        status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                        objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlKabelLeidingBescherming/mager-beton'),
        'niet-gekend': KeuzelijstWaarde(invulwaarde='niet-gekend',
                                        label='niet gekend',
                                        status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                        objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlKabelLeidingBescherming/niet-gekend'),
        'omegaprofiel': KeuzelijstWaarde(invulwaarde='omegaprofiel',
                                         label='omegaprofiel',
                                         status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                         objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlKabelLeidingBescherming/omegaprofiel'),
        'synthetische-kabeldekking': KeuzelijstWaarde(invulwaarde='synthetische-kabeldekking',
                                                      label='synthetische kabeldekking',
                                                      status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                                      objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlKabelLeidingBescherming/synthetische-kabeldekking'),
        'tegels': KeuzelijstWaarde(invulwaarde='tegels',
                                   label='tegels',
                                   status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                   objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlKabelLeidingBescherming/tegels'),
        'u-ijzers': KeuzelijstWaarde(invulwaarde='u-ijzers',
                                     label='u-ijzers',
                                     status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                     objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlKabelLeidingBescherming/u-ijzers'),
        'waarschuwingslint': KeuzelijstWaarde(invulwaarde='waarschuwingslint',
                                              label='waarschuwingslint',
                                              status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                              objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlKabelLeidingBescherming/waarschuwingslint'),
        'waarschuwingsnet': KeuzelijstWaarde(invulwaarde='waarschuwingsnet',
                                             label='waarschuwingsnet',
                                             status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                             objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlKabelLeidingBescherming/waarschuwingsnet')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

