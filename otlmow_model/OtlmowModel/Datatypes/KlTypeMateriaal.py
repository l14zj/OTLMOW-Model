# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlTypeMateriaal(KeuzelijstField):
    """Keuzelijst om aan te geven welk materiaal gebruikt wordt voor de voeg tot stand te brengen."""
    naam = 'KlTypeMateriaal'
    label = 'Type materiaal'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#KlTypeMateriaal'
    definition = 'Keuzelijst om aan te geven welk materiaal gebruikt wordt voor de voeg tot stand te brengen.'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlTypeMateriaal'
    options = {
        'None': KeuzelijstWaarde(invulwaarde='None',
                                 label='Type materiaal',
                                 status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                 definitie='De mogelijk materialen om de kokervoeg tot stand te brengen.',
                                 objectUri='https://.data.wegenenverkeer.be/id/conceptscheme/KlTypeMateriaal')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

