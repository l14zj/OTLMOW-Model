# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlMIVMeetpuntAfmetingen(KeuzelijstField):
    """Lijst van standaardafmetingen van een lus van een MIV meetpunt."""
    naam = 'KlMIVMeetpuntAfmetingen'
    label = 'MIV meetpunt afmetingen'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#KlMIVMeetpuntAfmetingen'
    definition = 'Lijst van standaardafmetingen van een lus van een MIV meetpunt.'
    status = 'https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlMIVMeetpuntAfmetingen'
    options = {
        '1-5x1-8': KeuzelijstWaarde(invulwaarde='1-5x1-8',
                                    label='1.5x1.8',
                                    status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                    definitie='1.5x1.8',
                                    objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlMIVMeetpuntAfmetingen/1-5x1-8'),
        '1-5x2-4': KeuzelijstWaarde(invulwaarde='1-5x2-4',
                                    label='1.5x2.4',
                                    status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                    definitie='1.5x2.4',
                                    objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlMIVMeetpuntAfmetingen/1-5x2-4'),
        '1-5x4': KeuzelijstWaarde(invulwaarde='1-5x4',
                                  label='1.5x4',
                                  status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                  definitie='1.5x4',
                                  objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlMIVMeetpuntAfmetingen/1-5x4')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

