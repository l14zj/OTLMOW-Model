# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlLokaalTerreinType(KeuzelijstField):
    """Lokale terrein types."""
    naam = 'KlLokaalTerreinType'
    label = 'Lokaal terreintype'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#KlLokaalTerreinType'
    definition = 'Lokale terrein types.'
    status = 'https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlLokaalTerreinType'
    options = {
        'golvend-zonder-bomen': KeuzelijstWaarde(invulwaarde='golvend-zonder-bomen',
                                                 label='Golvend zonder bomen',
                                                 status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                                 definitie='Golvend zonder bomen',
                                                 objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlLokaalTerreinType/golvend-zonder-bomen'),
        'vlak-en-overwegend-bomen-struiken': KeuzelijstWaarde(invulwaarde='vlak-en-overwegend-bomen-struiken',
                                                              label='Vlak en overwegend bomen / struiken',
                                                              status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                                              definitie='Vlak en overwegend bomen / struiken',
                                                              objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlLokaalTerreinType/vlak-en-overwegend-bomen-struiken'),
        'vlak-en-verspreid-bomen-struiken': KeuzelijstWaarde(invulwaarde='vlak-en-verspreid-bomen-struiken',
                                                             label='Vlak en verspreid bomen / struiken',
                                                             status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                                             definitie='Vlak en verspreid bomen / struiken',
                                                             objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlLokaalTerreinType/vlak-en-verspreid-bomen-struiken'),
        'vlak-zonder-bomen': KeuzelijstWaarde(invulwaarde='vlak-zonder-bomen',
                                              label='Vlak zonder bomen',
                                              status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                              definitie='Vlak zonder bomen',
                                              objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlLokaalTerreinType/vlak-zonder-bomen')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

