# coding=utf-8
import random
from otlmow_model.BaseClasses.KeuzelijstField import KeuzelijstField


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlTGCUitbreidingsModuleMerk(KeuzelijstField):
    """Keuzelijst met merknamen van uitbreidingsmodules van een toegangscontroller."""
    naam = 'KlTGCUitbreidingsModuleMerk'
    label = 'TGC uitbreidingsmodule merk'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlTGCUitbreidingsModuleMerk'
    definition = 'Keuzelijst met merknamen van uitbreidingsmodules van een toegangscontroller.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlTGCUitbreidingsModuleMerk'
    options = {
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

