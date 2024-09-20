# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlToeslagmiddelBeton(KeuzelijstField):
    """Materiaal dat aan het beton kan worden toegevoegd."""
    naam = 'KlToeslagmiddelBeton'
    label = 'Toeslagmiddel beton'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#KlToeslagmiddelBeton'
    definition = 'Materiaal dat aan het beton kan worden toegevoegd.'
    status = 'https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlToeslagmiddelBeton'
    options = {
        'fijn-toeslagmateriaal': KeuzelijstWaarde(invulwaarde='fijn-toeslagmateriaal',
                                                  label='Fijn toeslagmateriaal',
                                                  status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                                  definitie='Een korrelgrootte van kleiner dan 4 mm, meestal bestaande uit zand.',
                                                  objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlToeslagmiddelBeton/fijn-toeslagmateriaal'),
        'grof-toeslagmateriaal': KeuzelijstWaarde(invulwaarde='grof-toeslagmateriaal',
                                                  label='Grof toeslagmateriaal',
                                                  status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                                  definitie='Een korrelgrootte van gelijk aan of groter dan 4 mm, meestal bestaande uit grind.',
                                                  objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlToeslagmiddelBeton/grof-toeslagmateriaal')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

