# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlBoomConflicten(KeuzelijstField):
    """De verschillende mogelijke conflicten van een boom."""
    naam = 'KlBoomConflicten'
    label = 'Boom conflicten'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlBoomConflicten'
    definition = 'De verschillende mogelijke conflicten van een boom.'
    status = 'https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik'
    deprecated_version = '2.12.0'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlBoomConflicten'
    options = {
        'andere': KeuzelijstWaarde(invulwaarde='andere',
                                   label='andere',
                                   status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                   definitie='Andere mogelijke conflicten',
                                   objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlBoomConflicten/andere'),
        'beperkte-doorwortelbare-ruimte': KeuzelijstWaarde(invulwaarde='beperkte-doorwortelbare-ruimte',
                                                           label='beperkte doorwortelbare ruimte',
                                                           status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                                           definitie='Het bodemvolume met voldoende mineralen, water en zuurstof waar de wortels van de boom zich kunnen ontwikkelen is veel lager dan verwacht',
                                                           objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlBoomConflicten/beperkte-doorwortelbare-ruimte'),
        'bodemverdichting': KeuzelijstWaarde(invulwaarde='bodemverdichting',
                                             label='bodemverdichting',
                                             status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                             definitie="Verdichting van de bodem door belasting (voetgangers, fietsers, auto's, bouwmaterialen,...)",
                                             objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlBoomConflicten/bodemverdichting'),
        'hinderende-takken': KeuzelijstWaarde(invulwaarde='hinderende-takken',
                                              label='hinderende takken',
                                              status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                              definitie='Takken die hinderlijk zijn voor de zichtbaarheid en de vrije doorrijhoogte of die luchtleidingen raken',
                                              objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlBoomConflicten/hinderende-takken'),
        'instabiel': KeuzelijstWaarde(invulwaarde='instabiel',
                                      label='instabiel',
                                      status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                      definitie='Een boom die niet stabiel in de grond staat',
                                      objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlBoomConflicten/instabiel'),
        'scheefstand': KeuzelijstWaarde(invulwaarde='scheefstand',
                                        label='scheefstand',
                                        status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                        definitie='Schuin gezakte/gegroeide boom waarbij de top van de boom in het verlengde van de stam ligt en niet verticaal opgericht is',
                                        objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlBoomConflicten/scheefstand'),
        'te-dicht-bij-rand-verharding': KeuzelijstWaarde(invulwaarde='te-dicht-bij-rand-verharding',
                                                         label='te dicht bij rand verharding',
                                                         status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                                         definitie='Verharding ligt op minder dan 50 cm van de stamvoet',
                                                         objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlBoomConflicten/te-dicht-bij-rand-verharding'),
        'verharding': KeuzelijstWaarde(invulwaarde='verharding',
                                       label='verharding',
                                       status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                       definitie='Een verhardingslaag bevindt zich zeer dicht tegen de boom',
                                       objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlBoomConflicten/verharding'),
        'wortelopdruk': KeuzelijstWaarde(invulwaarde='wortelopdruk',
                                         label='wortelopdruk',
                                         status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                         definitie='Boomwortels die (weg)verhardingselementen opdrukken',
                                         objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlBoomConflicten/wortelopdruk')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

