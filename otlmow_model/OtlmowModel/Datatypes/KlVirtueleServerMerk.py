# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlVirtueleServerMerk(KeuzelijstField):
    """Het merk van de virtuele server."""
    naam = 'KlVirtueleServerMerk'
    label = 'Virtuele server merk'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlVirtueleServerMerk'
    definition = 'Het merk van de virtuele server.'
    status = 'https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlVirtueleServerMerk'
    options = {
        'hp': KeuzelijstWaarde(invulwaarde='hp',
                               label='HP',
                               status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                               definitie='HP',
                               objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlVirtueleServerMerk/hp'),
        'peek': KeuzelijstWaarde(invulwaarde='peek',
                                 label='Peek',
                                 status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                 definitie='Peek.',
                                 objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlVirtueleServerMerk/peek'),
        'ram': KeuzelijstWaarde(invulwaarde='ram',
                                label='RAM',
                                status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                definitie='RAM',
                                objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlVirtueleServerMerk/ram')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

