# coding=utf-8
import random
from otlmow_model.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlLETrottoirbandType(KeuzelijstField):
    """Types van trottoirband."""
    naam = 'KlLETrottoirbandType'
    label = 'Trottoirband type'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlLETrottoirbandType'
    definition = 'Types van trottoirband.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlLETrottoirbandType'
    options = {
        'beton-type-I-A': KeuzelijstWaarde(invulwaarde='beton-type-I-A',
                                           label='beton type I A',
                                           status='ingebruik',
                                           definitie='type I A',
                                           objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLETrottoirbandType/beton-type-I-A'),
        'beton-type-I-B': KeuzelijstWaarde(invulwaarde='beton-type-I-B',
                                           label='beton type I B',
                                           status='ingebruik',
                                           definitie='type I B',
                                           objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLETrottoirbandType/beton-type-I-B'),
        'beton-type-I-C1': KeuzelijstWaarde(invulwaarde='beton-type-I-C1',
                                            label='beton type I C1',
                                            status='ingebruik',
                                            definitie='type I C1',
                                            objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLETrottoirbandType/beton-type-I-C1'),
        'beton-type-I-C2': KeuzelijstWaarde(invulwaarde='beton-type-I-C2',
                                            label='beton type I C2',
                                            status='ingebruik',
                                            definitie='type I C2',
                                            objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLETrottoirbandType/beton-type-I-C2'),
        'beton-type-I-D1': KeuzelijstWaarde(invulwaarde='beton-type-I-D1',
                                            label='beton type I D1',
                                            status='ingebruik',
                                            definitie='type I D1',
                                            objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLETrottoirbandType/beton-type-I-D1'),
        'beton-type-I-D2': KeuzelijstWaarde(invulwaarde='beton-type-I-D2',
                                            label='beton type I D2',
                                            status='ingebruik',
                                            definitie='type I D2',
                                            objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLETrottoirbandType/beton-type-I-D2'),
        'beton-type-I-D3': KeuzelijstWaarde(invulwaarde='beton-type-I-D3',
                                            label='beton type I D3',
                                            status='ingebruik',
                                            definitie='type I D3',
                                            objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLETrottoirbandType/beton-type-I-D3'),
        'beton-type-I-D4': KeuzelijstWaarde(invulwaarde='beton-type-I-D4',
                                            label='beton type I D4',
                                            status='ingebruik',
                                            definitie='type I D4',
                                            objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLETrottoirbandType/beton-type-I-D4'),
        'beton-type-I-E': KeuzelijstWaarde(invulwaarde='beton-type-I-E',
                                           label='beton type I E',
                                           status='ingebruik',
                                           definitie='type I E',
                                           objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLETrottoirbandType/beton-type-I-E'),
        'beton-type-I-F1': KeuzelijstWaarde(invulwaarde='beton-type-I-F1',
                                            label='beton type I F1',
                                            status='ingebruik',
                                            definitie='type I F1',
                                            objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLETrottoirbandType/beton-type-I-F1'),
        'beton-type-I-F2': KeuzelijstWaarde(invulwaarde='beton-type-I-F2',
                                            label='beton type I F2',
                                            status='ingebruik',
                                            definitie='type I F2',
                                            objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLETrottoirbandType/beton-type-I-F2'),
        'beton-type-I-H': KeuzelijstWaarde(invulwaarde='beton-type-I-H',
                                           label='beton type I H',
                                           status='ingebruik',
                                           definitie='type I H',
                                           objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLETrottoirbandType/beton-type-I-H'),
        'natuursteen-type-A-I-1': KeuzelijstWaarde(invulwaarde='natuursteen-type-A-I-1',
                                                   label='natuursteen type A I 1',
                                                   status='ingebruik',
                                                   definitie='natuursteen type A I 1',
                                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLETrottoirbandType/natuursteen-type-A-I-1'),
        'natuursteen-type-A-I-2': KeuzelijstWaarde(invulwaarde='natuursteen-type-A-I-2',
                                                   label='natuursteen type A I 2',
                                                   status='ingebruik',
                                                   definitie='natuursteen type A I 2',
                                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLETrottoirbandType/natuursteen-type-A-I-2'),
        'natuursteen-type-A-I-3': KeuzelijstWaarde(invulwaarde='natuursteen-type-A-I-3',
                                                   label='natuursteen type A I 3',
                                                   status='ingebruik',
                                                   definitie='natuursteen type A I 3',
                                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLETrottoirbandType/natuursteen-type-A-I-3'),
        'natuursteen-type-A-II-1': KeuzelijstWaarde(invulwaarde='natuursteen-type-A-II-1',
                                                    label='natuursteen type A II 1',
                                                    status='ingebruik',
                                                    definitie='natuursteen type A II 1',
                                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLETrottoirbandType/natuursteen-type-A-II-1'),
        'natuursteen-type-A-II-2': KeuzelijstWaarde(invulwaarde='natuursteen-type-A-II-2',
                                                    label='natuursteen type A II 2',
                                                    status='ingebruik',
                                                    definitie='natuursteen type A II 2',
                                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLETrottoirbandType/natuursteen-type-A-II-2'),
        'natuursteen-type-A-II-3': KeuzelijstWaarde(invulwaarde='natuursteen-type-A-II-3',
                                                    label='natuursteen type A II 3',
                                                    status='ingebruik',
                                                    definitie='natuursteen type A II 3',
                                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLETrottoirbandType/natuursteen-type-A-II-3'),
        'natuursteen-type-B-I-1': KeuzelijstWaarde(invulwaarde='natuursteen-type-B-I-1',
                                                   label='natuursteen type B I 1',
                                                   status='ingebruik',
                                                   definitie='natuursteen type B I 1',
                                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLETrottoirbandType/natuursteen-type-B-I-1'),
        'natuursteen-type-B-I-2': KeuzelijstWaarde(invulwaarde='natuursteen-type-B-I-2',
                                                   label='natuursteen type B I 2',
                                                   status='ingebruik',
                                                   definitie='natuursteen type B I 2',
                                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLETrottoirbandType/natuursteen-type-B-I-2'),
        'natuursteen-type-B-II': KeuzelijstWaarde(invulwaarde='natuursteen-type-B-II',
                                                  label='natuursteen type B II',
                                                  status='ingebruik',
                                                  definitie='natuursteen type B II',
                                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLETrottoirbandType/natuursteen-type-B-II'),
        'natuursteen-type-C-I-1': KeuzelijstWaarde(invulwaarde='natuursteen-type-C-I-1',
                                                   label='natuursteen type C I 1',
                                                   status='ingebruik',
                                                   definitie='natuursteen type C I 1',
                                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLETrottoirbandType/natuursteen-type-C-I-1'),
        'natuursteen-type-C-I-2': KeuzelijstWaarde(invulwaarde='natuursteen-type-C-I-2',
                                                   label='natuursteen type C I 2',
                                                   status='ingebruik',
                                                   definitie='natuursteen type C I 2',
                                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLETrottoirbandType/natuursteen-type-C-I-2'),
        'natuursteen-type-C-II-1': KeuzelijstWaarde(invulwaarde='natuursteen-type-C-II-1',
                                                    label='natuursteen type C II 1',
                                                    status='ingebruik',
                                                    definitie='natuursteen type C II 1',
                                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLETrottoirbandType/natuursteen-type-C-II-1'),
        'natuursteen-type-C-II-2': KeuzelijstWaarde(invulwaarde='natuursteen-type-C-II-2',
                                                    label='natuursteen type C II 2',
                                                    status='ingebruik',
                                                    definitie='natuursteen type C II 2',
                                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLETrottoirbandType/natuursteen-type-C-II-2')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

