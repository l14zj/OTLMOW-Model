# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlCalamiteitsbordVorm(KeuzelijstField):
    """Vormen van het calamiteitsbord."""
    naam = 'KlCalamiteitsbordVorm'
    label = 'Calamiteitsbord vorm'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlCalamiteitsbordVorm'
    definition = 'Vormen van het calamiteitsbord.'
    status = 'https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlCalamiteitsbordVorm'
    options = {
        'rechthoekig': KeuzelijstWaarde(invulwaarde='rechthoekig',
                                        label='rechthoekig',
                                        status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                        definitie='Een rechthoekig calamiteitsbord.',
                                        objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlCalamiteitsbordVorm/rechthoekig'),
        'ruitvormig': KeuzelijstWaarde(invulwaarde='ruitvormig',
                                       label='ruitvormig',
                                       status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                       definitie='Een ruitvormig calamiteitsbord.',
                                       objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlCalamiteitsbordVorm/ruitvormig')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

