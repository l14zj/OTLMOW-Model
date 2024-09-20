# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlDekselMateriaal(KeuzelijstField):
    """Het materiaal waaruit het deksel bestaat."""
    naam = 'KlDekselMateriaal'
    label = 'Dekselmateriaal'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlDekselMateriaal'
    definition = 'Het materiaal waaruit het deksel bestaat.'
    status = 'https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlDekselMateriaal'
    options = {
        'anders': KeuzelijstWaarde(invulwaarde='anders',
                                   label='anders',
                                   status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                   definitie='anders',
                                   objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlDekselMateriaal/anders'),
        'beton': KeuzelijstWaarde(invulwaarde='beton',
                                  label='beton',
                                  status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                  definitie='beton',
                                  objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlDekselMateriaal/beton'),
        'betonnen-segmenten': KeuzelijstWaarde(invulwaarde='betonnen-segmenten',
                                               label='betonnen segmenten',
                                               status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                               definitie='betonnen segmenten',
                                               objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlDekselMateriaal/betonnen-segmenten'),
        'cementmortel': KeuzelijstWaarde(invulwaarde='cementmortel',
                                         label='cementmortel',
                                         status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                         definitie='cementmortel',
                                         objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlDekselMateriaal/cementmortel'),
        'gewapend-beton': KeuzelijstWaarde(invulwaarde='gewapend-beton',
                                           label='gewapend beton',
                                           status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                           definitie='gewapend beton',
                                           objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlDekselMateriaal/gewapend-beton'),
        'gietijzer': KeuzelijstWaarde(invulwaarde='gietijzer',
                                      label='gietijzer',
                                      status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                      definitie='nodulair gietijzer',
                                      objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlDekselMateriaal/gietijzer'),
        'grijs-gietijzer': KeuzelijstWaarde(invulwaarde='grijs-gietijzer',
                                            label='grijs gietijzer',
                                            status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                            definitie='grijs gietijzer',
                                            objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlDekselMateriaal/grijs-gietijzer'),
        'ongeÃ¯dentificeerd-materiaal': KeuzelijstWaarde(invulwaarde='ongeÃ¯dentificeerd-materiaal',
                                                         label='ongeÃ¯dentificeerd materiaal',
                                                         status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                                         definitie='ongeÃ¯dentificeerd materiaal',
                                                         objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlDekselMateriaal/ongeÃ¯dentificeerd-materiaal'),
        'ongeÃ¯dentificeerd-type-ijzer-of-staal': KeuzelijstWaarde(invulwaarde='ongeÃ¯dentificeerd-type-ijzer-of-staal',
                                                                   label='ongeÃ¯dentificeerd type ijzer of staal',
                                                                   status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                                                   definitie='ongeÃ¯dentificeerd type ijzer of staal',
                                                                   objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlDekselMateriaal/ongeÃ¯dentificeerd-type-ijzer-of-staal'),
        'ongeÃ¯dentificeerd-type-kunststof': KeuzelijstWaarde(invulwaarde='ongeÃ¯dentificeerd-type-kunststof',
                                                              label='ongeÃ¯dentificeerd type kunststof',
                                                              status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                                              definitie='ongeÃ¯dentificeerd type kunststof',
                                                              objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlDekselMateriaal/ongeÃ¯dentificeerd-type-kunststof'),
        'smeedijzer': KeuzelijstWaarde(invulwaarde='smeedijzer',
                                       label='smeedijzer',
                                       status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                       definitie='smeedijzer',
                                       objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlDekselMateriaal/smeedijzer'),
        'staal': KeuzelijstWaarde(invulwaarde='staal',
                                  label='staal',
                                  status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                  definitie='staal',
                                  objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlDekselMateriaal/staal')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

