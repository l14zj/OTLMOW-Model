# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlLEGCMateriaal(KeuzelijstField):
    """Materialen van de geluidswerende constructie."""
    naam = 'KlLEGCMateriaal'
    label = 'Materiaal geluidswerende constructie'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlLEGCMateriaal'
    definition = 'Materialen van de geluidswerende constructie.'
    status = 'https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlLEGCMateriaal'
    options = {
        'bakstenen': KeuzelijstWaarde(invulwaarde='bakstenen',
                                      label='bakstenen',
                                      status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                      definitie='bakstenen',
                                      objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlLEGCMateriaal/bakstenen'),
        'beton': KeuzelijstWaarde(invulwaarde='beton',
                                  label='beton',
                                  status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                  definitie='beton',
                                  objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlLEGCMateriaal/beton'),
        'beton---houtvezelbeton': KeuzelijstWaarde(invulwaarde='beton---houtvezelbeton',
                                                   label='beton - houtvezelbeton',
                                                   status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                                   definitie='beton - houtvezelbeton',
                                                   objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlLEGCMateriaal/beton---houtvezelbeton'),
        'beton---lichtgewichtbeton': KeuzelijstWaarde(invulwaarde='beton---lichtgewichtbeton',
                                                      label='beton - lichtgewichtbeton',
                                                      status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                                      definitie='beton - lichtgewichtbeton',
                                                      objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlLEGCMateriaal/beton---lichtgewichtbeton'),
        'beton---steenparament': KeuzelijstWaarde(invulwaarde='beton---steenparament',
                                                  label='beton - steenparament',
                                                  status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                                  definitie='Beton - steenparament',
                                                  objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlLEGCMateriaal/beton---steenparament'),
        'glas': KeuzelijstWaarde(invulwaarde='glas',
                                 label='glas',
                                 status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                 definitie='glas',
                                 objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlLEGCMateriaal/glas'),
        'groenscherm': KeuzelijstWaarde(invulwaarde='groenscherm',
                                        label='groenscherm',
                                        status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                        definitie='groenscherm',
                                        objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlLEGCMateriaal/groenscherm'),
        'hout': KeuzelijstWaarde(invulwaarde='hout',
                                 label='hout',
                                 status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                 definitie='hout',
                                 objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlLEGCMateriaal/hout'),
        'kokospanelen': KeuzelijstWaarde(invulwaarde='kokospanelen',
                                         label='kokospanelen',
                                         status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                         definitie='kokospanelen',
                                         objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlLEGCMateriaal/kokospanelen'),
        'kunststof---PMMA': KeuzelijstWaarde(invulwaarde='kunststof---PMMA',
                                             label='kunststof - PMMA',
                                             status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                             definitie='Kunststof - PMMA',
                                             objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlLEGCMateriaal/kunststof---PMMA'),
        'kunststof---PVC': KeuzelijstWaarde(invulwaarde='kunststof---PVC',
                                            label='kunststof - PVC',
                                            status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                            definitie='kunststof - PVC',
                                            objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlLEGCMateriaal/kunststof---PVC'),
        'metaal---aluminium': KeuzelijstWaarde(invulwaarde='metaal---aluminium',
                                               label='metaal - aluminium',
                                               status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                               definitie='Metaal - aluminium',
                                               objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlLEGCMateriaal/metaal---aluminium'),
        'metaal---aluminium-en-staal': KeuzelijstWaarde(invulwaarde='metaal---aluminium-en-staal',
                                                        label='metaal - aluminium en staal',
                                                        status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                                        definitie='Metaal - aluminium en staal',
                                                        objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlLEGCMateriaal/metaal---aluminium-en-staal'),
        'metaal---staal': KeuzelijstWaarde(invulwaarde='metaal---staal',
                                           label='metaal - staal',
                                           status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                           definitie='metaal - staal',
                                           objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlLEGCMateriaal/metaal---staal'),
        'stalen-raster-met-beschermnet-in-kunststof': KeuzelijstWaarde(invulwaarde='stalen-raster-met-beschermnet-in-kunststof',
                                                                       label='stalen raster met beschermnet in kunststof',
                                                                       status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                                                       definitie='stalen raster met beschermnet in kunststof',
                                                                       objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlLEGCMateriaal/stalen-raster-met-beschermnet-in-kunststof'),
        'tunnelplaat': KeuzelijstWaarde(invulwaarde='tunnelplaat',
                                        label='tunnelplaat',
                                        status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                        definitie='tunnelplaat',
                                        objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlLEGCMateriaal/tunnelplaat')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

