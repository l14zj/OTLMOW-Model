# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlPictogramSymbool(KeuzelijstField):
    """De mogelijke symbolen op het pictogram."""
    naam = 'KlPictogramSymbool'
    label = 'Pictogram symbool'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlPictogramSymbool'
    definition = 'De mogelijke symbolen op het pictogram.'
    status = 'https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlPictogramSymbool'
    options = {
        'halte': KeuzelijstWaarde(invulwaarde='halte',
                                  label='halte',
                                  status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                  definitie='Duidt de locatie aan waar het openbaar vervoer, bv. bus, tram of trolley, stopt om passagiers te laten in- en uitstappen.',
                                  objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlPictogramSymbool/halte'),
        'hydrant-bovengronds-(H)': KeuzelijstWaarde(invulwaarde='hydrant-bovengronds-(H)',
                                                    label='hydrant bovengronds (H)',
                                                    status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                                    objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlPictogramSymbool/hydrant-bovengronds-(H)'),
        'hydrant-ondergronds-(B)': KeuzelijstWaarde(invulwaarde='hydrant-ondergronds-(B)',
                                                    label='hydrant ondergronds (B)',
                                                    status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                                    objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlPictogramSymbool/hydrant-ondergronds-(B)'),
        'nooddeurnummer': KeuzelijstWaarde(invulwaarde='nooddeurnummer',
                                           label='nooddeurnummer',
                                           status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                           definitie='nooddeurnummer',
                                           objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlPictogramSymbool/nooddeurnummer'),
        'nummer-veiligheidsnis': KeuzelijstWaarde(invulwaarde='nummer-veiligheidsnis',
                                                  label='nummer veiligheidsnis',
                                                  status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                                  objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlPictogramSymbool/nummer-veiligheidsnis'),
        'tunnelnaam': KeuzelijstWaarde(invulwaarde='tunnelnaam',
                                       label='tunnelnaam',
                                       status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                       objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlPictogramSymbool/tunnelnaam'),
        'verbodsbord': KeuzelijstWaarde(invulwaarde='verbodsbord',
                                        label='verbodsbord',
                                        status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                        objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlPictogramSymbool/verbodsbord'),
        'vluchtend-persoon': KeuzelijstWaarde(invulwaarde='vluchtend-persoon',
                                              label='vluchtend persoon',
                                              status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                              objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlPictogramSymbool/vluchtend-persoon')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

