# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlAansluitingskabel(KeuzelijstField):
    """Keuzelijst voor de types van aansluitingskabel volgens de gebruikte verbinding."""
    naam = 'KlAansluitingskabel'
    label = 'Aansluitingskabel'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlAansluitingskabel'
    definition = 'Keuzelijst voor de types van aansluitingskabel volgens de gebruikte verbinding.'
    status = 'https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlAansluitingskabel'
    options = {
        'alarmkabel-2-10': KeuzelijstWaarde(invulwaarde='alarmkabel-2-10',
                                            label='alarmkabel 2+10',
                                            status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                            objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAansluitingskabel/alarmkabel-2-10'),
        'alarmkabel-2-4': KeuzelijstWaarde(invulwaarde='alarmkabel-2-4',
                                           label='alarmkabel 2+4',
                                           status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                           objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAansluitingskabel/alarmkabel-2-4'),
        'alarmkabel-2-6': KeuzelijstWaarde(invulwaarde='alarmkabel-2-6',
                                           label='alarmkabel 2+6',
                                           status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                           objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAansluitingskabel/alarmkabel-2-6'),
        'alarmkabel-2-8': KeuzelijstWaarde(invulwaarde='alarmkabel-2-8',
                                           label='alarmkabel 2+8',
                                           status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                           objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAansluitingskabel/alarmkabel-2-8'),
        'draadloos': KeuzelijstWaarde(invulwaarde='draadloos',
                                      label='draadloos',
                                      status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                      objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAansluitingskabel/draadloos'),
        'lihch': KeuzelijstWaarde(invulwaarde='lihch',
                                  label='LIHCH',
                                  status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                  objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAansluitingskabel/lihch'),
        'lihh': KeuzelijstWaarde(invulwaarde='lihh',
                                 label='LIHH',
                                 status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                 objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAansluitingskabel/lihh'),
        'liycy': KeuzelijstWaarde(invulwaarde='liycy',
                                  label='LIYCY',
                                  status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                  objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAansluitingskabel/liycy'),
        'liyy': KeuzelijstWaarde(invulwaarde='liyy',
                                 label='LIYY',
                                 status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                 objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAansluitingskabel/liyy'),
        'telefoonkabel': KeuzelijstWaarde(invulwaarde='telefoonkabel',
                                          label='telefoonkabel',
                                          status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                          objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAansluitingskabel/telefoonkabel'),
        'test': KeuzelijstWaarde(invulwaarde='test',
                                 label='test',
                                 status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                 definitie='test',
                                 objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAansluitingskabel/test'),
        'utp': KeuzelijstWaarde(invulwaarde='utp',
                                label='UTP',
                                status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAansluitingskabel/utp'),
        'xgb': KeuzelijstWaarde(invulwaarde='xgb',
                                label='XGB',
                                status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAansluitingskabel/xgb'),
        'xvb': KeuzelijstWaarde(invulwaarde='xvb',
                                label='XVB',
                                status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAansluitingskabel/xvb')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

