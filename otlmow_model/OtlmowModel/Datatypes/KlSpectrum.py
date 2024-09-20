# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlSpectrum(KeuzelijstField):
    """Mogelijke spectra"""
    naam = 'KlSpectrum'
    label = 'Spectrum'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlSpectrum'
    definition = 'Mogelijke spectra'
    status = 'https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlSpectrum'
    options = {
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

