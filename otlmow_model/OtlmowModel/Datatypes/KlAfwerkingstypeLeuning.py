# coding=utf-8
from ..BaseClasses.KeuzelijstField import KeuzelijstField
from ..BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlAfwerkingstypeLeuning(KeuzelijstField):
    """Geeft de afwerking van de leuning weer."""
    naam = 'KlAfwerkingstypeLeuning'
    label = 'Afwerkingstype leuning'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#KlAfwerkingstypeLeuning'
    definition = 'Geeft de afwerking van de leuning weer.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlAfwerkingstypeLeuning'
    options = {
        'gegalvaniseerd': KeuzelijstWaarde(invulwaarde='gegalvaniseerd',
                                           label='Gegalvaniseerd',
                                           status='ingebruik',
                                           objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAfwerkingstypeLeuning/gegalvaniseerd'),
        'geverfd': KeuzelijstWaarde(invulwaarde='geverfd',
                                    label='Geverfd',
                                    status='ingebruik',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAfwerkingstypeLeuning/geverfd')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

