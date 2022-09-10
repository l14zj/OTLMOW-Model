# coding=utf-8
import random
from otlmow_model.BaseClasses.KeuzelijstField import KeuzelijstField


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlVerwarmingselementModelnaam(KeuzelijstField):
    """Keuzelijst van modellen van verwarmingselementen voor alle relevante merken."""
    naam = 'KlVerwarmingselementModelnaam'
    label = 'Verwarmingselement model naam'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlVerwarmingselementModelnaam'
    definition = 'Keuzelijst van modellen van verwarmingselementen voor alle relevante merken.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlVerwarmingselementModelnaam'
    options = {
    }

    @classmethod
    def create_dummy_data(cls):
        return random.choice(list(map(lambda x: x.invulwaarde,
                                      filter(lambda option: option.status == 'ingebruik', cls.options.values()))))

