# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlHuisaansluitputMateriaal(KeuzelijstField):
    """Materialen voor een huisaansluitput."""
    naam = 'KlHuisaansluitputMateriaal'
    label = 'Huisaansluitput materiaal'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlHuisaansluitputMateriaal'
    definition = 'Materialen voor een huisaansluitput.'
    status = 'https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlHuisaansluitputMateriaal'
    options = {
        'beton': KeuzelijstWaarde(invulwaarde='beton',
                                  label='beton',
                                  status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                  definitie='betonnen huisaansluitputje',
                                  objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlHuisaansluitputMateriaal/beton'),
        'gres': KeuzelijstWaarde(invulwaarde='gres',
                                 label='gres',
                                 status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                 definitie='aansluitputje in grÃ¨s.',
                                 objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlHuisaansluitputMateriaal/gres'),
        'kunststof': KeuzelijstWaarde(invulwaarde='kunststof',
                                      label='kunststof',
                                      status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                      definitie='kunstof aansluitputje',
                                      objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlHuisaansluitputMateriaal/kunststof')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

