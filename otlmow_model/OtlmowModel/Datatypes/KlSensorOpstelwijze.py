# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlSensorOpstelwijze(KeuzelijstField):
    """Senor opstelwijzen."""
    naam = 'KlSensorOpstelwijze'
    label = 'Sensor opstelwijze'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#KlSensorOpstelwijze'
    definition = 'Senor opstelwijzen.'
    status = 'https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlSensorOpstelwijze'
    options = {
        'rechtstreeks-op-rechte-steun': KeuzelijstWaarde(invulwaarde='rechtstreeks-op-rechte-steun',
                                                         label='rechtstreeks-op-rechte-steun',
                                                         status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                                         definitie='rechtstreeks-op-rechte-steun',
                                                         objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlSensorOpstelwijze/rechtstreeks-op-rechte-steun')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

