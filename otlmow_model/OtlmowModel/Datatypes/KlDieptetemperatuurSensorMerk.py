# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlDieptetemperatuurSensorMerk(KeuzelijstField):
    """Dieptetemperatuursensor merken."""
    naam = 'KlDieptetemperatuurSensorMerk'
    label = 'Dieptetemperatuursensor merk'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlDieptetemperatuurSensorMerk'
    definition = 'Dieptetemperatuursensor merken.'
    status = 'https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlDieptetemperatuurSensorMerk'
    options = {
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

