# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlMIVLuskaartType(KeuzelijstField):
    """Mogelijke types voor de uitvoering van luskaarten van Meten In Vlaanderen"""
    naam = 'KlMIVLuskaartType'
    label = 'MIV luskaart type'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlMIVLuskaartType'
    definition = 'Mogelijke types voor de uitvoering van luskaarten van Meten In Vlaanderen'
    status = 'https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlMIVLuskaartType'
    options = {
        '19-inch-3h': KeuzelijstWaarde(invulwaarde='19-inch-3h',
                                       label='19 inch 3H',
                                       status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                       definitie='19 inch 3H',
                                       objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlMIVLuskaartType/19-inch-3h'),
        '19-inch-6h': KeuzelijstWaarde(invulwaarde='19-inch-6h',
                                       label='19 inch 6H',
                                       status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                       definitie='19 inch 6H',
                                       objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlMIVLuskaartType/19-inch-6h'),
        'compact': KeuzelijstWaarde(invulwaarde='compact',
                                    label='compact',
                                    status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                    definitie='compact',
                                    objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlMIVLuskaartType/compact')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

