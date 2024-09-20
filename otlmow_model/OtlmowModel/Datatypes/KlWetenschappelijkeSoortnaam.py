# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlWetenschappelijkeSoortnaam(KeuzelijstField):
    """De mogelijke wetenschappelijke soortnamen van de vegetatie."""
    naam = 'KlWetenschappelijkeSoortnaam'
    label = 'Wetenschappelijke soortnaam'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlWetenschappelijkeSoortnaam'
    definition = 'De mogelijke wetenschappelijke soortnamen van de vegetatie.'
    status = 'https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlWetenschappelijkeSoortnaam'
    options = {
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

