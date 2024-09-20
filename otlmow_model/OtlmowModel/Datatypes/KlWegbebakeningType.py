# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlWegbebakeningType(KeuzelijstField):
    """De vormen van wegbebakening."""
    naam = 'KlWegbebakeningType'
    label = 'Wegbebakening type'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlWegbebakeningType'
    definition = 'De vormen van wegbebakening.'
    status = 'https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlWegbebakeningType'
    options = {
        'type-1-(new-jersey-reclip)': KeuzelijstWaarde(invulwaarde='type-1-(new-jersey-reclip)',
                                                       label='type 1 (new jersey reclip)',
                                                       status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                                       definitie='type 1 (new jersey reclip)',
                                                       objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlWegbebakeningType/type-1-(new-jersey-reclip)'),
        'type-2-(new-jersey)': KeuzelijstWaarde(invulwaarde='type-2-(new-jersey)',
                                                label='type 2 (new jersey)',
                                                status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                                definitie='type 2 (new jersey)',
                                                objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlWegbebakeningType/type-2-(new-jersey)'),
        'type-3-(referentiepaal)': KeuzelijstWaarde(invulwaarde='type-3-(referentiepaal)',
                                                    label='type 3 (referentiepaal)',
                                                    status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                                    definitie='type 3 (referentiepaal)',
                                                    objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlWegbebakeningType/type-3-(referentiepaal)'),
        'type-A-(vangrail-reclip)': KeuzelijstWaarde(invulwaarde='type-A-(vangrail-reclip)',
                                                     label='type A (vangrail reclip)',
                                                     status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                                     definitie='type A (vangrail reclip)',
                                                     objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlWegbebakeningType/type-A-(vangrail-reclip)'),
        'type-B-(vangrail)': KeuzelijstWaarde(invulwaarde='type-B-(vangrail)',
                                              label='type B (vangrail)',
                                              status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                              definitie='type B (vangrail)',
                                              objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlWegbebakeningType/type-B-(vangrail)'),
        'type-C-(vangrail-trapezium)': KeuzelijstWaarde(invulwaarde='type-C-(vangrail-trapezium)',
                                                        label='type C (vangrail trapezium)',
                                                        status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                                        definitie='Type C (vangrail trapezium)',
                                                        objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlWegbebakeningType/type-C-(vangrail-trapezium)')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

