# coding=utf-8
import random
from otlmow_model.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlSDRKlasse(KeuzelijstField):
    """De verhouding tussen de wanddikte en de diameter van de persleiding."""
    naam = 'KlSDRKlasse'
    label = 'SDR klasse'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlSDRKlasse'
    definition = 'De verhouding tussen de wanddikte en de diameter van de persleiding.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlSDRKlasse'
    options = {
        '11': KeuzelijstWaarde(invulwaarde='11',
                               label='11',
                               status='ingebruik',
                               definitie='11',
                               objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlSDRKlasse/11'),
        '17': KeuzelijstWaarde(invulwaarde='17',
                               label='17',
                               status='ingebruik',
                               definitie='17',
                               objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlSDRKlasse/17')
    }

    @classmethod
    def create_dummy_data(cls):
        return random.choice(list(map(lambda x: x.invulwaarde,
                                      filter(lambda option: option.status == 'ingebruik', cls.options.values()))))

