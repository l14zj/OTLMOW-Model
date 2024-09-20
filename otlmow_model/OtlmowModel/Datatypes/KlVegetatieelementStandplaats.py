# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlVegetatieelementStandplaats(KeuzelijstField):
    """De mogelijke standplaatsen van een vegetatieelement."""
    naam = 'KlVegetatieelementStandplaats'
    label = 'Vegetatieelement standplaats'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#KlVegetatieelementStandplaats'
    definition = 'De mogelijke standplaatsen van een vegetatieelement.'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlVegetatieelementStandplaats'
    options = {
        'gesloten-bebouwing-dorpskern': KeuzelijstWaarde(invulwaarde='gesloten-bebouwing-dorpskern',
                                                         label='gesloten bebouwing - dorpskern',
                                                         status='ingebruik',
                                                         definitie='gesloten bebouwing - dorpskern',
                                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVegetatieelementStandplaats/gesloten-bebouwing-dorpskern'),
        'open-en-halfopen-bebouwing': KeuzelijstWaarde(invulwaarde='open-en-halfopen-bebouwing',
                                                       label='open en halfopen bebouwing',
                                                       status='ingebruik',
                                                       definitie='open en halfopen bebouwing',
                                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVegetatieelementStandplaats/open-en-halfopen-bebouwing'),
        'stadscentrum': KeuzelijstWaarde(invulwaarde='stadscentrum',
                                         label='stadscentrum',
                                         status='ingebruik',
                                         definitie='stadscentrum',
                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVegetatieelementStandplaats/stadscentrum')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

