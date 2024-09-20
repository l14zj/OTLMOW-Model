# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlBVLaagtype(KeuzelijstField):
    """Laagtypes van de bitumineuze verharding."""
    naam = 'KlBVLaagtype'
    label = 'BV laagtype'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlBVLaagtype'
    definition = 'Laagtypes van de bitumineuze verharding.'
    status = 'https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlBVLaagtype'
    options = {
        'andere-toplagen': KeuzelijstWaarde(invulwaarde='andere-toplagen',
                                            label='andere toplagen',
                                            status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                            definitie='union type om het laagtype van bitumineuze verharding te bepalen',
                                            objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlBVLaagtype/andere-toplagen'),
        'beschermingslaag': KeuzelijstWaarde(invulwaarde='beschermingslaag',
                                             label='beschermingslaag',
                                             status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                             definitie='beschermingslaag',
                                             objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlBVLaagtype/beschermingslaag'),
        'onderlaag': KeuzelijstWaarde(invulwaarde='onderlaag',
                                      label='onderlaag',
                                      status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                      definitie='Onderliggende laag van een bitumineuze verharding met een constante dikte. ',
                                      objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlBVLaagtype/onderlaag'),
        'profileerlaag': KeuzelijstWaarde(invulwaarde='profileerlaag',
                                          label='profileerlaag',
                                          status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                          definitie='union type om het laagtype van bitumineuze verharding te bepalen',
                                          objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlBVLaagtype/profileerlaag'),
        'toplaag-van-asfaltbeton': KeuzelijstWaarde(invulwaarde='toplaag-van-asfaltbeton',
                                                    label='toplaag van asfaltbeton',
                                                    status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                                    definitie='Bovenste laag van een bitumineuze verharding, die direct in contact komt met het verkeer bestaande uit asfaltbeton.',
                                                    objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlBVLaagtype/toplaag-van-asfaltbeton'),
        'toplaag-van-gietasfalt': KeuzelijstWaarde(invulwaarde='toplaag-van-gietasfalt',
                                                   label='toplaag van gietasfalt',
                                                   status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                                   definitie='union type om het laagtype van bitumineuze verharding te bepalen',
                                                   objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlBVLaagtype/toplaag-van-gietasfalt'),
        'tussenlaag': KeuzelijstWaarde(invulwaarde='tussenlaag',
                                       label='tussenlaag',
                                       status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                       definitie='Bitumineuze laag die aangebracht wordt tussen een betonverharding en de fundering. ',
                                       objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlBVLaagtype/tussenlaag')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

