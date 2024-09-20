# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlKabelmofType(KeuzelijstField):
    """Types voor kabel- en leidingmoffen."""
    naam = 'KlKabelmofType'
    label = 'Kabelmof type'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlKabelmofType'
    definition = 'Types voor kabel- en leidingmoffen.'
    status = 'https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlKabelmofType'
    options = {
        'geldoos': KeuzelijstWaarde(invulwaarde='geldoos',
                                    label='geldoos',
                                    status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                    objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlKabelmofType/geldoos'),
        'gietmof': KeuzelijstWaarde(invulwaarde='gietmof',
                                    label='gietmof',
                                    status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                    objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlKabelmofType/gietmof'),
        'hdpe-mof': KeuzelijstWaarde(invulwaarde='hdpe-mof',
                                     label='HDPE mof',
                                     status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                     definitie='HDPE mof',
                                     objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlKabelmofType/hdpe-mof')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

