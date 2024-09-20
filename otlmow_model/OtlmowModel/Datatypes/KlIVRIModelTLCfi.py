# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlIVRIModelTLCfi(KeuzelijstField):
    """De modelnaam van de TLC-fi poort."""
    naam = 'KlIVRIModelTLCfi'
    label = 'iVRIModelTLCfi'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlIVRIModelTLCfi'
    definition = 'De modelnaam van de TLC-fi poort.'
    status = 'https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlIVRIModelTLCfi'
    options = {
        'civa-2020': KeuzelijstWaarde(invulwaarde='civa-2020',
                                      label='CIVA 2020',
                                      status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                      definitie='CIVA 2020',
                                      objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlIVRIModelTLCfi/civa-2020'),
        'civa-2020s': KeuzelijstWaarde(invulwaarde='civa-2020s',
                                       label='CIVA 2020s',
                                       status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                       definitie='CIVA 2020S',
                                       objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlIVRIModelTLCfi/civa-2020s'),
        'flownode': KeuzelijstWaarde(invulwaarde='flownode',
                                     label='FlowNode',
                                     status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                     definitie='FlowNode',
                                     objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlIVRIModelTLCfi/flownode'),
        'flownodes': KeuzelijstWaarde(invulwaarde='flownodes',
                                      label='FlowNodes',
                                      status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                      definitie='FlowNodes',
                                      objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlIVRIModelTLCfi/flownodes'),
        'tlc-fi-broker': KeuzelijstWaarde(invulwaarde='tlc-fi-broker',
                                          label='TLC-FI broker',
                                          status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                          definitie='TLC-FI broker',
                                          objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlIVRIModelTLCfi/tlc-fi-broker')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

