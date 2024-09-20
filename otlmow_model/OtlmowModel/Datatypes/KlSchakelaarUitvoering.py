# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlSchakelaarUitvoering(KeuzelijstField):
    """Keuzelijst voor de uitvoering van een schakelaar."""
    naam = 'KlSchakelaarUitvoering'
    label = 'Uitvoering schakelaar'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlSchakelaarUitvoering'
    definition = 'Keuzelijst voor de uitvoering van een schakelaar.'
    status = 'https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlSchakelaarUitvoering'
    options = {
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

