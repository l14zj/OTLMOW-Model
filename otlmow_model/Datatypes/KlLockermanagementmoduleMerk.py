# coding=utf-8
import random
from otlmow_model.BaseClasses.KeuzelijstField import KeuzelijstField


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlLockermanagementmoduleMerk(KeuzelijstField):
    """Merknamen van een lockermanagementmodule."""
    naam = 'KlLockermanagementmoduleMerk'
    label = 'Lockermanagementmodule merk'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlLockermanagementmoduleMerk'
    definition = 'Merknamen van een lockermanagementmodule.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlLockermanagementmoduleMerk'
    options = {
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

