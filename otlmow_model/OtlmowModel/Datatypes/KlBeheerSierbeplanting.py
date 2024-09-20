# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlBeheerSierbeplanting(KeuzelijstField):
    """Verschillende mogelijke beheeropties bij sierbeplanting."""
    naam = 'KlBeheerSierbeplanting'
    label = 'Beheer sierbeplanting'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/levenscyclus#KlBeheerSierbeplanting'
    definition = 'Verschillende mogelijke beheeropties bij sierbeplanting.'
    status = 'https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlBeheerSierbeplanting'
    options = {
        'bodemafdekking-boomschors': KeuzelijstWaarde(invulwaarde='bodemafdekking-boomschors',
                                                      label='bodemafdekking - boomschors',
                                                      status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                                      definitie='De bodem wordt afgedekt met boomschors.',
                                                      objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlBeheerSierbeplanting/bodemafdekking-boomschors'),
        'bodemafdekking-doek-in-jute-pla-folie': KeuzelijstWaarde(invulwaarde='bodemafdekking-doek-in-jute-pla-folie',
                                                                  label='bodemafdekking - doek in jute & PLA folie',
                                                                  status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                                                  definitie='De bodem wordt afgedekt met een doek in jute en PLA-folie.',
                                                                  objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlBeheerSierbeplanting/bodemafdekking-doek-in-jute-pla-folie'),
        'bodemafdekking-groencompost': KeuzelijstWaarde(invulwaarde='bodemafdekking-groencompost',
                                                        label='bodemafdekking - groencompost',
                                                        status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                                        definitie='De bodem wordt afgedekt met groencompost.',
                                                        objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlBeheerSierbeplanting/bodemafdekking-groencompost'),
        'bodemafdekking-houtsnippers': KeuzelijstWaarde(invulwaarde='bodemafdekking-houtsnippers',
                                                        label='bodemafdekking - houtsnippers',
                                                        status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                                        definitie='De bodem wordt afgedekt met houtsnippers.',
                                                        objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlBeheerSierbeplanting/bodemafdekking-houtsnippers'),
        'bodemafdekking-pla-doek': KeuzelijstWaarde(invulwaarde='bodemafdekking-pla-doek',
                                                    label='bodemafdekking - PLA doek',
                                                    status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                                    definitie='De bodem wordt afgedekt met een PLA-doek.',
                                                    objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlBeheerSierbeplanting/bodemafdekking-pla-doek'),
        'hakken': KeuzelijstWaarde(invulwaarde='hakken',
                                   label='hakken',
                                   status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                   definitie='Hakken van de grond tussen sierbeplantingen.',
                                   objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlBeheerSierbeplanting/hakken'),
        'niets-doen': KeuzelijstWaarde(invulwaarde='niets-doen',
                                       label='niets doen',
                                       status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                       definitie='Er wordt geen beheer uitgevoerd.',
                                       objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlBeheerSierbeplanting/niets-doen'),
        'opschikken-knippen-dood-materiaal': KeuzelijstWaarde(invulwaarde='opschikken-knippen-dood-materiaal',
                                                              label='opschikken-knippen dood materiaal',
                                                              status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                                              definitie='Opschikken/knippen van dood materiaal.',
                                                              objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlBeheerSierbeplanting/opschikken-knippen-dood-materiaal'),
        'scheren': KeuzelijstWaarde(invulwaarde='scheren',
                                    label='scheren',
                                    status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                    definitie='Het vlakvormig gelijkmatig kort afsnijden van takken van hagen, heesters en houtkanten.',
                                    objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlBeheerSierbeplanting/scheren'),
        'snoeien': KeuzelijstWaarde(invulwaarde='snoeien',
                                    label='snoeien',
                                    status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                    definitie='Het inkorten of wegnemen van stengels met snoeischaar.',
                                    objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlBeheerSierbeplanting/snoeien'),
        'wieden': KeuzelijstWaarde(invulwaarde='wieden',
                                   label='wieden',
                                   status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                   definitie='Het wieden van de grond tussen sierbeplanting. Dit is het verwijderen van onkruid.',
                                   objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlBeheerSierbeplanting/wieden')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

