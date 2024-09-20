# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlVriLusSoortvoertuig(KeuzelijstField):
    """Keuzelijst met verschillende types voertuigen die een detectielus volgens diens instellingen kan detecteren."""
    naam = 'KlVriLusSoortvoertuig'
    label = 'VRI-lus soort voertuig'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlVriLusSoortvoertuig'
    definition = 'Keuzelijst met verschillende types voertuigen die een detectielus volgens diens instellingen kan detecteren.'
    status = 'https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlVriLusSoortvoertuig'
    options = {
        'fiets': KeuzelijstWaarde(invulwaarde='fiets',
                                  label='fiets',
                                  status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                  objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlVriLusSoortvoertuig/fiets'),
        'motor': KeuzelijstWaarde(invulwaarde='motor',
                                  label='motor',
                                  status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                  objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlVriLusSoortvoertuig/motor'),
        'voertuig': KeuzelijstWaarde(invulwaarde='voertuig',
                                     label='voertuig',
                                     status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                     objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlVriLusSoortvoertuig/voertuig')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

