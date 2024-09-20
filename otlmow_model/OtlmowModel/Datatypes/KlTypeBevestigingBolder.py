# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlTypeBevestigingBolder(KeuzelijstField):
    """De mogelijke bevestigingstypes van een bolder."""
    naam = 'KlTypeBevestigingBolder'
    label = 'Type bevestiging bolder'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlTypeBevestigingBolder'
    definition = 'De mogelijke bevestigingstypes van een bolder.'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlTypeBevestigingBolder'
    options = {
        'breekbout': KeuzelijstWaarde(invulwaarde='breekbout',
                                      label='breekbout',
                                      status='ingebruik',
                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlTypeBevestigingBolder/breekbout'),
        'breekbout-op-onderlegplaat': KeuzelijstWaarde(invulwaarde='breekbout-op-onderlegplaat',
                                                       label='breekbout op onderlegplaat',
                                                       status='ingebruik',
                                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlTypeBevestigingBolder/breekbout-op-onderlegplaat'),
        'draadstang': KeuzelijstWaarde(invulwaarde='draadstang',
                                       label='draadstang',
                                       status='ingebruik',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlTypeBevestigingBolder/draadstang'),
        'draadstang-ingestort-in-beton': KeuzelijstWaarde(invulwaarde='draadstang-ingestort-in-beton',
                                                          label='draadstang ingestort in beton',
                                                          status='ingebruik',
                                                          objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlTypeBevestigingBolder/draadstang-ingestort-in-beton'),
        'ingestort': KeuzelijstWaarde(invulwaarde='ingestort',
                                      label='ingestort',
                                      status='ingebruik',
                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlTypeBevestigingBolder/ingestort'),
        'ingestorte-bolderconstructie': KeuzelijstWaarde(invulwaarde='ingestorte-bolderconstructie',
                                                         label='ingestorte bolderconstructie',
                                                         status='ingebruik',
                                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlTypeBevestigingBolder/ingestorte-bolderconstructie')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

