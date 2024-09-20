# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlTypeBolder(KeuzelijstField):
    """De mogelijke typen van een bolder."""
    naam = 'KlTypeBolder'
    label = 'Type bolder'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlTypeBolder'
    definition = 'De mogelijke typen van een bolder.'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlTypeBolder'
    options = {
        'andere': KeuzelijstWaarde(invulwaarde='andere',
                                   label='andere',
                                   status='ingebruik',
                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlTypeBolder/andere'),
        'dubbele-kikker': KeuzelijstWaarde(invulwaarde='dubbele-kikker',
                                           label='dubbele kikker',
                                           status='ingebruik',
                                           objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlTypeBolder/dubbele-kikker'),
        'dubbele-kruis': KeuzelijstWaarde(invulwaarde='dubbele-kruis',
                                          label='dubbele kruis',
                                          status='ingebruik',
                                          objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlTypeBolder/dubbele-kruis'),
        'dubbele-paddenstoel': KeuzelijstWaarde(invulwaarde='dubbele-paddenstoel',
                                                label='dubbele paddenstoel',
                                                status='ingebruik',
                                                objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlTypeBolder/dubbele-paddenstoel'),
        'dubbele-t-hoofd': KeuzelijstWaarde(invulwaarde='dubbele-t-hoofd',
                                            label='dubbele T-hoofd',
                                            status='ingebruik',
                                            objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlTypeBolder/dubbele-t-hoofd'),
        'dubbelekikker': KeuzelijstWaarde(invulwaarde='dubbelekikker',
                                          label='dubbeleKikker',
                                          status='ingebruik',
                                          objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlTypeBolder/dubbelekikker'),
        'dubbelekruis': KeuzelijstWaarde(invulwaarde='dubbelekruis',
                                         label='dubbeleKruis',
                                         status='ingebruik',
                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlTypeBolder/dubbelekruis'),
        'dubbelepaddenstoel': KeuzelijstWaarde(invulwaarde='dubbelepaddenstoel',
                                               label='dubbelepaddenstoel',
                                               status='ingebruik',
                                               objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlTypeBolder/dubbelepaddenstoel'),
        'dubbelet-hoofd': KeuzelijstWaarde(invulwaarde='dubbelet-hoofd',
                                           label='dubbeleT-hoofd',
                                           status='ingebruik',
                                           objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlTypeBolder/dubbelet-hoofd'),
        'hoorns': KeuzelijstWaarde(invulwaarde='hoorns',
                                   label='hoorns',
                                   status='ingebruik',
                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlTypeBolder/hoorns'),
        'horens': KeuzelijstWaarde(invulwaarde='horens',
                                   label='horens',
                                   status='ingebruik',
                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlTypeBolder/horens'),
        'kikker': KeuzelijstWaarde(invulwaarde='kikker',
                                   label='kikker',
                                   status='ingebruik',
                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlTypeBolder/kikker'),
        'kruis': KeuzelijstWaarde(invulwaarde='kruis',
                                  label='kruis',
                                  status='ingebruik',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlTypeBolder/kruis'),
        'paddenstoel': KeuzelijstWaarde(invulwaarde='paddenstoel',
                                        label='paddenstoel',
                                        status='ingebruik',
                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlTypeBolder/paddenstoel'),
        'quick-release': KeuzelijstWaarde(invulwaarde='quick-release',
                                          label='quick release',
                                          status='ingebruik',
                                          objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlTypeBolder/quick-release'),
        't-hoofd': KeuzelijstWaarde(invulwaarde='t-hoofd',
                                    label='t-hoofd',
                                    status='ingebruik',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlTypeBolder/t-hoofd')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

