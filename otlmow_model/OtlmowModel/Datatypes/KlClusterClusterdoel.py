# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlClusterClusterdoel(KeuzelijstField):
    """De reden waarom de custer is opgezet."""
    naam = 'KlClusterClusterdoel'
    label = 'Cluster clusterdoel'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlClusterClusterdoel'
    definition = 'De reden waarom de custer is opgezet.'
    status = 'https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlClusterClusterdoel'
    options = {
        'groeperen-resources': KeuzelijstWaarde(invulwaarde='groeperen-resources',
                                                label='groeperen resources',
                                                status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                                objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlClusterClusterdoel/groeperen-resources'),
        'redundantie': KeuzelijstWaarde(invulwaarde='redundantie',
                                        label='redundantie',
                                        status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                        objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlClusterClusterdoel/redundantie')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

