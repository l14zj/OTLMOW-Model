# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlDatakabelType(KeuzelijstField):
    """Lijst van types voor datakabels volgens hun constructieve kenmerken."""
    naam = 'KlDatakabelType'
    label = 'Datakabel types'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlDatakabelType'
    definition = 'Lijst van types voor datakabels volgens hun constructieve kenmerken.'
    status = 'https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlDatakabelType'
    options = {
        'andere': KeuzelijstWaarde(invulwaarde='andere',
                                   label='andere',
                                   status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                   definitie='Elk types telecommunicatie- of datakabel dat niet opgenomen is in het Standaardbestek 270 en waarover een akkoord bestaat dat die mag gebruikt worden.',
                                   objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlDatakabelType/andere'),
        'eo-ymekaszh': KeuzelijstWaarde(invulwaarde='eo-ymekaszh',
                                        label='EO-YMeKaszh',
                                        status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                        definitie='EO-YMeKaszh',
                                        objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlDatakabelType/eo-ymekaszh'),
        'f-utp': KeuzelijstWaarde(invulwaarde='f-utp',
                                  label='F-UTP',
                                  status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                  definitie='F-UTP',
                                  objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlDatakabelType/f-utp'),
        'f-utp-cat-5': KeuzelijstWaarde(invulwaarde='f-utp-cat-5',
                                        label='F/UTP cat 5',
                                        status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                        definitie='U/UTP Categorie 5E.',
                                        objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlDatakabelType/f-utp-cat-5'),
        'f-utp-cat-5-outdoor': KeuzelijstWaarde(invulwaarde='f-utp-cat-5-outdoor',
                                                label='F/UTP cat 5 outdoor',
                                                status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                                definitie='U/UTP Categorie 5E.',
                                                objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlDatakabelType/f-utp-cat-5-outdoor'),
        'f-utp-cat-5e': KeuzelijstWaarde(invulwaarde='f-utp-cat-5e',
                                         label='F/UTP cat 5E',
                                         status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                         definitie='U/UTP Categorie 5E.',
                                         objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlDatakabelType/f-utp-cat-5e'),
        'f-utp-cat-5e-outdoor': KeuzelijstWaarde(invulwaarde='f-utp-cat-5e-outdoor',
                                                 label='F/UTP cat 5E outdoor',
                                                 status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                                 definitie='U/UTP Categorie 5E.',
                                                 objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlDatakabelType/f-utp-cat-5e-outdoor'),
        'f-utp-cat-6': KeuzelijstWaarde(invulwaarde='f-utp-cat-6',
                                        label='F/UTP cat 6',
                                        status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                        definitie='F/UTP Categorie 6.',
                                        objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlDatakabelType/f-utp-cat-6'),
        'f-utp-cat5': KeuzelijstWaarde(invulwaarde='f-utp-cat5',
                                       label='F-UTP Cat5',
                                       status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                       definitie='F-UTP Cat5',
                                       objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlDatakabelType/f-utp-cat5'),
        'f-utp-cat5-outdoor': KeuzelijstWaarde(invulwaarde='f-utp-cat5-outdoor',
                                               label='F-UTP Cat5 outdoor',
                                               status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                               definitie='F-UTP Cat5 outdoor',
                                               objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlDatakabelType/f-utp-cat5-outdoor'),
        'f-utp-cat5e': KeuzelijstWaarde(invulwaarde='f-utp-cat5e',
                                        label='F-UTP Cat5E',
                                        status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                        definitie='F-UTP Cat5E',
                                        objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlDatakabelType/f-utp-cat5e'),
        'f-utp-cat5e-outdoor': KeuzelijstWaarde(invulwaarde='f-utp-cat5e-outdoor',
                                                label='F-UTP Cat5E outdoor',
                                                status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                                definitie='F-UTP Cat5E outdoor',
                                                objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlDatakabelType/f-utp-cat5e-outdoor'),
        'f-utp-cat6': KeuzelijstWaarde(invulwaarde='f-utp-cat6',
                                       label='F-UTP Cat6',
                                       status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                       definitie='F-UTP Cat6',
                                       objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlDatakabelType/f-utp-cat6'),
        'f-utp-cat6-outdoor': KeuzelijstWaarde(invulwaarde='f-utp-cat6-outdoor',
                                               label='F-UTP Cat6 outdoor',
                                               status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                               definitie='F-UTP Cat6 outdoor',
                                               objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlDatakabelType/f-utp-cat6-outdoor'),
        'f-utp-cat6outdoor': KeuzelijstWaarde(invulwaarde='f-utp-cat6outdoor',
                                              label='F-UTP Cat6outdoor',
                                              status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/uitgebruik',
                                              definitie='F-UTP Cat6outdoor',
                                              objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlDatakabelType/f-utp-cat6outdoor'),
        'fo-so': KeuzelijstWaarde(invulwaarde='fo-so',
                                  label='FO/SO',
                                  status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                  objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlDatakabelType/fo-so'),
        'j-h(st)h-bd': KeuzelijstWaarde(invulwaarde='j-h(st)h-bd',
                                        label='J-H(St)H-BD',
                                        status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                        definitie='Halogeenvrije telefoniekabel.',
                                        objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlDatakabelType/j-h(st)h-bd'),
        'je-h(st)h-rf-1h': KeuzelijstWaarde(invulwaarde='je-h(st)h-rf-1h',
                                            label='JE-H(St)H Rf 1h',
                                            status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                            definitie='Telefoniekabel met functiebehoud.',
                                            objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlDatakabelType/je-h(st)h-rf-1h'),
        'rg11': KeuzelijstWaarde(invulwaarde='rg11',
                                 label='RG11',
                                 status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                 definitie='RG 11 Coaxkabel.',
                                 objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlDatakabelType/rg11'),
        'rg12': KeuzelijstWaarde(invulwaarde='rg12',
                                 label='RG12',
                                 status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                 definitie='RG 12 Coaxkabel.',
                                 objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlDatakabelType/rg12'),
        'rg59': KeuzelijstWaarde(invulwaarde='rg59',
                                 label='RG59',
                                 status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                 definitie='RG 59 Coaxkabel.',
                                 objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlDatakabelType/rg59'),
        'rg6': KeuzelijstWaarde(invulwaarde='rg6',
                                label='RG6',
                                status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                definitie='RG 6 Coaxkabel.',
                                objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlDatakabelType/rg6'),
        'stralende-kabel': KeuzelijstWaarde(invulwaarde='stralende-kabel',
                                            label='Stralende kabel',
                                            status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                            definitie='Stralende kabel.',
                                            objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlDatakabelType/stralende-kabel'),
        'tpgf': KeuzelijstWaarde(invulwaarde='tpgf',
                                 label='TPGF',
                                 status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                 definitie='Halogeenvrije telefoniekabel met enkel afgeschermde paren voor binnen.',
                                 objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlDatakabelType/tpgf'),
        'twavb': KeuzelijstWaarde(invulwaarde='twavb',
                                  label='TWAVB',
                                  status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                  definitie='TWAVB',
                                  objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlDatakabelType/twavb'),
        'u-utp-cat-5e': KeuzelijstWaarde(invulwaarde='u-utp-cat-5e',
                                         label='U/UTP cat 5E',
                                         status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                         definitie='U/UTP Categorie 5E.',
                                         objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlDatakabelType/u-utp-cat-5e'),
        'u-utp-cat-6e': KeuzelijstWaarde(invulwaarde='u-utp-cat-6e',
                                         label='U/UTP cat 6E',
                                         status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                         definitie='U/UTP Categorie 6.',
                                         objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlDatakabelType/u-utp-cat-6e'),
        'u-utp-cat-6e-outdoor': KeuzelijstWaarde(invulwaarde='u-utp-cat-6e-outdoor',
                                                 label='U/UTP cat 6E outdoor',
                                                 status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                                 definitie='U/UTP Categorie 6.',
                                                 objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlDatakabelType/u-utp-cat-6e-outdoor'),
        'u-utp-categorie-5e-outdoor': KeuzelijstWaarde(invulwaarde='u-utp-categorie-5e-outdoor',
                                                       label='U/UTP categorie 5E outdoor',
                                                       status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                                       definitie='U/UTP Categorie 5E.',
                                                       objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlDatakabelType/u-utp-categorie-5e-outdoor'),
        'utp': KeuzelijstWaarde(invulwaarde='utp',
                                label='UTP',
                                status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                definitie='UTP',
                                objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlDatakabelType/utp'),
        'utp-cat5': KeuzelijstWaarde(invulwaarde='utp-cat5',
                                     label='UTP Cat5',
                                     status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                     definitie='UTP Cat5',
                                     objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlDatakabelType/utp-cat5'),
        'utp-cat5e': KeuzelijstWaarde(invulwaarde='utp-cat5e',
                                      label='UTP Cat5E',
                                      status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                      definitie='UTP Cat5E',
                                      objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlDatakabelType/utp-cat5e'),
        'utp-cat5e-outdoor': KeuzelijstWaarde(invulwaarde='utp-cat5e-outdoor',
                                              label='UTP Cat5E outdoor',
                                              status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                              definitie='UTP Cat5E outdoor',
                                              objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlDatakabelType/utp-cat5e-outdoor'),
        'utp-cat6': KeuzelijstWaarde(invulwaarde='utp-cat6',
                                     label='UTP Cat6',
                                     status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                     definitie='UTP Cat6',
                                     objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlDatakabelType/utp-cat6'),
        'utp-cat6-outdoor': KeuzelijstWaarde(invulwaarde='utp-cat6-outdoor',
                                             label='UTP Cat6 outdoor',
                                             status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                             definitie='UTP Cat6 outdoor',
                                             objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlDatakabelType/utp-cat6-outdoor'),
        'utp-cat6outdoor': KeuzelijstWaarde(invulwaarde='utp-cat6outdoor',
                                            label='UTP Cat6outdoor',
                                            status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/uitgebruik',
                                            definitie='UTP Cat6outdoor',
                                            objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlDatakabelType/utp-cat6outdoor'),
        'uxl': KeuzelijstWaarde(invulwaarde='uxl',
                                label='UXL',
                                status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                definitie='UXL',
                                objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlDatakabelType/uxl')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

