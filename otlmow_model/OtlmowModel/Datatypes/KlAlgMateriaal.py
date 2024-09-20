# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlAlgMateriaal(KeuzelijstField):
    """Het materiaal waaruit een object voornamelijk gebouwd is."""
    naam = 'KlAlgMateriaal'
    label = 'Materiaal soorten'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlAlgMateriaal'
    definition = 'Het materiaal waaruit een object voornamelijk gebouwd is.'
    status = 'https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlAlgMateriaal'
    options = {
        'aluminium': KeuzelijstWaarde(invulwaarde='aluminium',
                                      label='aluminium',
                                      status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                      objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAlgMateriaal/aluminium'),
        'beton': KeuzelijstWaarde(invulwaarde='beton',
                                  label='beton',
                                  status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                  objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAlgMateriaal/beton'),
        'gegalvaniseerd-staal': KeuzelijstWaarde(invulwaarde='gegalvaniseerd-staal',
                                                 label='gegalvaniseerd staal',
                                                 status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                                 definitie='gegalvaniseerd staal',
                                                 objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAlgMateriaal/gegalvaniseerd-staal'),
        'glasvezelversterkt-polyester': KeuzelijstWaarde(invulwaarde='glasvezelversterkt-polyester',
                                                         label='glasvezelversterkt polyester',
                                                         status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                                         definitie='glasvezelversterkt polyester',
                                                         objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAlgMateriaal/glasvezelversterkt-polyester'),
        'hdpe': KeuzelijstWaarde(invulwaarde='hdpe',
                                 label='HDPE',
                                 status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                 definitie='HDPE',
                                 objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAlgMateriaal/hdpe'),
        'hout': KeuzelijstWaarde(invulwaarde='hout',
                                 label='hout',
                                 status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                 objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAlgMateriaal/hout'),
        'houtvezelbeton': KeuzelijstWaarde(invulwaarde='houtvezelbeton',
                                           label='houtvezelbeton',
                                           status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                           objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAlgMateriaal/houtvezelbeton'),
        'inox': KeuzelijstWaarde(invulwaarde='inox',
                                 label='Inox',
                                 status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                 definitie='Inox',
                                 objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAlgMateriaal/inox'),
        'kunstof': KeuzelijstWaarde(invulwaarde='kunstof',
                                    label='kunstof',
                                    status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/uitgebruik',
                                    definitie='kunstof',
                                    objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAlgMateriaal/kunstof'),
        'kunststof': KeuzelijstWaarde(invulwaarde='kunststof',
                                      label='kunststof',
                                      status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                      definitie='kunststof',
                                      objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAlgMateriaal/kunststof'),
        'metselwerk': KeuzelijstWaarde(invulwaarde='metselwerk',
                                       label='metselwerk',
                                       status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                       definitie='metselwerk',
                                       objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAlgMateriaal/metselwerk'),
        'polycarbonaat': KeuzelijstWaarde(invulwaarde='polycarbonaat',
                                          label='polycarbonaat',
                                          status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                          definitie='polycarbonaat',
                                          objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAlgMateriaal/polycarbonaat'),
        'pvc': KeuzelijstWaarde(invulwaarde='pvc',
                                label='PVC',
                                status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                definitie='PVC',
                                objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAlgMateriaal/pvc'),
        'roestvrijstaal': KeuzelijstWaarde(invulwaarde='roestvrijstaal',
                                           label='roestvrijstaal',
                                           status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                           objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAlgMateriaal/roestvrijstaal'),
        'rvs': KeuzelijstWaarde(invulwaarde='rvs',
                                label='RVS',
                                status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                definitie='RVS',
                                objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAlgMateriaal/rvs'),
        'staal': KeuzelijstWaarde(invulwaarde='staal',
                                  label='staal',
                                  status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                  definitie='staal',
                                  objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAlgMateriaal/staal')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

