# coding=utf-8
import random
from otlmow_model.BaseClasses.KeuzelijstField import KeuzelijstField


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlFunctieRioleringsstelsel(KeuzelijstField):
    """De verschillende mogelijke functies van het rioleringsstelsel."""
    naam = 'KlFunctieRioleringsstelsel'
    label = 'Functie van rioleringsstelsel'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#KlFunctieRioleringsstelsel'
    definition = 'De verschillende mogelijke functies van het rioleringsstelsel.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlFunctieRioleringsstelsel'
    options = {
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)
