# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlGekleurdWVCode(KeuzelijstField):
    """Codes voor een gekleurd wegvlak."""
    naam = 'KlGekleurdWVCode'
    label = 'Gekleurd WV code'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlGekleurdWVCode'
    definition = 'Codes voor een gekleurd wegvlak.'
    status = 'https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlGekleurdWVCode'
    options = {
        'GW-FOP': KeuzelijstWaarde(invulwaarde='GW-FOP',
                                   label='GW-FOP',
                                   status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                   definitie='Gekleurd wegvlak voor fietsoversteekplaats met blokken.',
                                   objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlGekleurdWVCode/GW-FOP'),
        'GW-FP': KeuzelijstWaarde(invulwaarde='GW-FP',
                                  label='GW-FP',
                                  status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                  definitie='Gekleurd wegvlak voor fietsoversteekplaats met lijnen.',
                                  objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlGekleurdWVCode/GW-FP'),
        'GW-FSUG': KeuzelijstWaarde(invulwaarde='GW-FSUG',
                                    label='GW-FSUG',
                                    status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                    definitie='Gekleurd wegvlak voor fietssuggestiestrook (oker,grijs).',
                                    objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlGekleurdWVCode/GW-FSUG'),
        'GW-FSUG-A': KeuzelijstWaarde(invulwaarde='GW-FSUG-A',
                                      label='GW-FSUG-A',
                                      status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                      definitie='Gekleurd wegvlak voor fietssuggestiestrook (groen,geel,rood).',
                                      objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlGekleurdWVCode/GW-FSUG-A'),
        'GW-MID': KeuzelijstWaarde(invulwaarde='GW-MID',
                                   label='GW-MID',
                                   status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                   definitie='Gekleurd wegvlak voor middengeleider(bv.groene strook)',
                                   objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlGekleurdWVCode/GW-MID'),
        'GW-MV': KeuzelijstWaarde(invulwaarde='GW-MV',
                                  label='GW-MV',
                                  status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                  definitie='Gekleurd wegvlak voor parkeerplaats mindervaliden.',
                                  objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlGekleurdWVCode/GW-MV'),
        'GW-OFOS': KeuzelijstWaarde(invulwaarde='GW-OFOS',
                                    label='GW-OFOS',
                                    status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                    definitie='Gekleurd wegvlak voor voor OFOS.',
                                    objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlGekleurdWVCode/GW-OFOS'),
        'GW-OFOS-VAR': KeuzelijstWaarde(invulwaarde='GW-OFOS-VAR',
                                        label='GW-OFOS-VAR',
                                        status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                        definitie='Gekleurd wegvlak voor OFOS variant.',
                                        objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlGekleurdWVCode/GW-OFOS-VAR'),
        'GW-PLAT': KeuzelijstWaarde(invulwaarde='GW-PLAT',
                                    label='GW-PLAT',
                                    status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                    definitie='Gekleurd wegvlak voor verkeersplateau.',
                                    objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlGekleurdWVCode/GW-PLAT'),
        'GW-VOP': KeuzelijstWaarde(invulwaarde='GW-VOP',
                                   label='GW-VOP',
                                   status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                   definitie='Gekleurd wegvlak voor voetgangers-oversteekplaats.',
                                   objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlGekleurdWVCode/GW-VOP')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

