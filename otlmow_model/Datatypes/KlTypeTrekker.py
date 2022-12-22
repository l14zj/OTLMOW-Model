# coding=utf-8
import random
from otlmow_model.BaseClasses.KeuzelijstField import KeuzelijstField


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlTypeTrekker(KeuzelijstField):
    """Het type trekker."""
    naam = 'KlTypeTrekker'
    label = 'Type trekker'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#KlTypeTrekker'
    definition = 'Het type trekker.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlTypeTrekker'
    options = {
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

