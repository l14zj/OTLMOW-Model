# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlBouwmethode(KeuzelijstField):
    """Keuzelijst om aan te geven welke bouwmethode gebruikt is om het koker element tot stand te brengen."""
    naam = 'KlBouwmethode'
    label = 'type bouwmethode'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#KlBouwmethode'
    definition = 'Keuzelijst om aan te geven welke bouwmethode gebruikt is om het koker element tot stand te brengen.'
    status = 'https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlBouwmethode'
    options = {
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

