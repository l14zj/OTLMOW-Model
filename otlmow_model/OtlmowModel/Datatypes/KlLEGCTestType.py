# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlLEGCTestType(KeuzelijstField):
    """Het test type van het geluidswerend scherm."""
    naam = 'KlLEGCTestType'
    label = 'Test type'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlLEGCTestType'
    definition = 'Het test type van het geluidswerend scherm.'
    status = 'https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlLEGCTestType'
    options = {
        'geluidsabsorptie': KeuzelijstWaarde(invulwaarde='geluidsabsorptie',
                                             label='geluidsabsorptie',
                                             status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                             definitie='Proef : De Ã©Ã©ngetalsaanduiding als waarde voor de geluidsabsorptie.',
                                             objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlLEGCTestType/geluidsabsorptie'),
        'luchtgeluidsisolatie': KeuzelijstWaarde(invulwaarde='luchtgeluidsisolatie',
                                                 label='luchtgeluidsisolatie',
                                                 status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                                 definitie='Proef : De Ã©Ã©ngetalsaanduiding voor luchtgeluidsisolatie.',
                                                 objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlLEGCTestType/luchtgeluidsisolatie')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

