# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlAfmetingsensorMerk(KeuzelijstField):
    """Het merk van de afmetingsensor."""
    naam = 'KlAfmetingsensorMerk'
    label = 'Afmetingsensor merk'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlAfmetingsensorMerk'
    definition = 'Het merk van de afmetingsensor.'
    status = 'https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlAfmetingsensorMerk'
    options = {
        'Sick': KeuzelijstWaarde(invulwaarde='Sick',
                                 label='Sick',
                                 status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                 definitie='Dave def toegevoegd',
                                 objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAfmetingsensorMerk/Sick'),
        'dave-s-optie': KeuzelijstWaarde(invulwaarde='dave-s-optie',
                                         label="Dave's optie",
                                         status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                         definitie="Def Dave's optie",
                                         objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAfmetingsensorMerk/dave-s-optie'),
        'dave-test-2': KeuzelijstWaarde(invulwaarde='dave-test-2',
                                        label='Dave test 2',
                                        status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                        definitie='Def Dave test 2',
                                        objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAfmetingsensorMerk/dave-test-2')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

