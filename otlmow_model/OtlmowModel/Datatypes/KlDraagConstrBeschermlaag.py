# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlDraagConstrBeschermlaag(KeuzelijstField):
    """De manieren van aanbrengen van een beschermlaag ter voorkoming van roestvorming."""
    naam = 'KlDraagConstrBeschermlaag'
    label = 'Draagconstructie beschermlaag'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlDraagConstrBeschermlaag'
    definition = 'De manieren van aanbrengen van een beschermlaag ter voorkoming van roestvorming.'
    status = 'https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlDraagConstrBeschermlaag'
    options = {
        'gecoat': KeuzelijstWaarde(invulwaarde='gecoat',
                                   label='gecoat',
                                   status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                   definitie='Een mengsel van stoffen aangebracht om roest te voorkomen.',
                                   objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlDraagConstrBeschermlaag/gecoat'),
        'gegalvaniseerd': KeuzelijstWaarde(invulwaarde='gegalvaniseerd',
                                           label='gegalvaniseerd',
                                           status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                           definitie='Een laag zink aangebracht om roest te voorkomen.',
                                           objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlDraagConstrBeschermlaag/gegalvaniseerd'),
        'geschilderd': KeuzelijstWaarde(invulwaarde='geschilderd',
                                        label='geschilderd',
                                        status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                        definitie='Een laag verf aangebracht om roest te voorkomen.',
                                        objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlDraagConstrBeschermlaag/geschilderd')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

