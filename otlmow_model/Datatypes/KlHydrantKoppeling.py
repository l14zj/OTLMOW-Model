# coding=utf-8
import random
from otlmow_model.BaseClasses.KeuzelijstField import KeuzelijstField


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlHydrantKoppeling(KeuzelijstField):
    """Keuzelijst met types koppelingen van hydranten."""
    naam = 'KlHydrantKoppeling'
    label = 'Hydrant koppeling'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlHydrantKoppeling'
    definition = 'Keuzelijst met types koppelingen van hydranten.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlHydrantKoppeling'
    options = {
    }

    @classmethod
    def create_dummy_data(cls):
        return random.choice(list(map(lambda x: x.invulwaarde,
                                      filter(lambda option: option.status == 'ingebruik', cls.options.values()))))

