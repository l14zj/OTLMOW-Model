# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlFolieType(KeuzelijstField):
    """Types van folie."""
    naam = 'KlFolieType'
    label = 'Folie type'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlFolieType'
    definition = 'Types van folie.'
    status = 'https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlFolieType'
    options = {
        'folietype-1': KeuzelijstWaarde(invulwaarde='folietype-1',
                                        label='folietype 1',
                                        status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                        definitie='folietype 1',
                                        objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlFolieType/folietype-1'),
        'folietype-2': KeuzelijstWaarde(invulwaarde='folietype-2',
                                        label='folietype 2',
                                        status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                        definitie='folietype 2',
                                        objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlFolieType/folietype-2'),
        'folietype-3a': KeuzelijstWaarde(invulwaarde='folietype-3a',
                                         label='folietype 3a',
                                         status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                         definitie='folietype 3a',
                                         objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlFolieType/folietype-3a'),
        'folietype-3a-en-3b': KeuzelijstWaarde(invulwaarde='folietype-3a-en-3b',
                                               label='folietype 3a en 3b',
                                               status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                               definitie='folietype 3a en 3b',
                                               objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlFolieType/folietype-3a-en-3b'),
        'folietype-3b': KeuzelijstWaarde(invulwaarde='folietype-3b',
                                         label='folietype 3b',
                                         status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                         definitie='folietype 3b',
                                         objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlFolieType/folietype-3b')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

