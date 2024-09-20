# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlAanplantingswijzeSierbeplanting(KeuzelijstField):
    """De mogelijke manieren van aanplanten van sierbeplanting."""
    naam = 'KlAanplantingswijzeSierbeplanting'
    label = 'aanplantingswijze sierbeplanting'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlAanplantingswijzeSierbeplanting'
    definition = 'De mogelijke manieren van aanplanten van sierbeplanting.'
    status = 'https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlAanplantingswijzeSierbeplanting'
    options = {
        'aanplanting-bol--en-knolgewassen': KeuzelijstWaarde(invulwaarde='aanplanting-bol--en-knolgewassen',
                                                             label='aanplanting bol- en knolgewassen',
                                                             status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                                             definitie='Aanplanting via bol- en knolgewassen',
                                                             objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAanplantingswijzeSierbeplanting/aanplanting-bol--en-knolgewassen'),
        'aanplanting-helm': KeuzelijstWaarde(invulwaarde='aanplanting-helm',
                                             label='aanplanting helm',
                                             status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                             definitie='Aanplanting via helm',
                                             objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAanplantingswijzeSierbeplanting/aanplanting-helm'),
        'aanplanting-zonder-helm': KeuzelijstWaarde(invulwaarde='aanplanting-zonder-helm',
                                                    label='aanplanting zonder helm',
                                                    status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                                    definitie='Aanplanting zonder helm',
                                                    objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAanplantingswijzeSierbeplanting/aanplanting-zonder-helm'),
        'd-2': KeuzelijstWaarde(invulwaarde='d-2',
                                label='d',
                                status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                definitie='dd',
                                objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAanplantingswijzeSierbeplanting/d-2')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

