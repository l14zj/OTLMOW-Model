# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlHardwareDomein(KeuzelijstField):
    """Lijst met gebruikte administratieve groeperingen van meerdere particuliere computernetwerken of hosts binnen dezelfde infrastructuur."""
    naam = 'KlHardwareDomein'
    label = 'Hardware domein'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#KlHardwareDomein'
    definition = 'Lijst met gebruikte administratieve groeperingen van meerdere particuliere computernetwerken of hosts binnen dezelfde infrastructuur.'
    status = 'https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlHardwareDomein'
    options = {
        'alfa': KeuzelijstWaarde(invulwaarde='alfa',
                                 label='alfa',
                                 status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                 objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlHardwareDomein/alfa'),
        'belfla': KeuzelijstWaarde(invulwaarde='belfla',
                                   label='belfla',
                                   status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                   objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlHardwareDomein/belfla')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

