# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlTGCUitbreidingsModuleType(KeuzelijstField):
    """Keuzelijst om het type uitbreidingsmodule van een toeganscontroller te specifiëren."""
    naam = 'KlTGCUitbreidingsModuleType'
    label = 'TGC uitbreidingsmodule type'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlTGCUitbreidingsModuleType'
    definition = 'Keuzelijst om het type uitbreidingsmodule van een toeganscontroller te specifiëren.'
    status = 'https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlTGCUitbreidingsModuleType'
    options = {
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

