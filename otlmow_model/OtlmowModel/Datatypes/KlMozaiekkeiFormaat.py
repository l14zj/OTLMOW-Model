# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlMozaiekkeiFormaat(KeuzelijstField):
    """Formaten van de mozaïekkei."""
    naam = 'KlMozaiekkeiFormaat'
    label = 'Mozaiekkei formaat'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlMozaiekkeiFormaat'
    definition = 'Formaten van de mozaïekkei.'
    status = 'https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlMozaiekkeiFormaat'
    options = {
        'bestratingen-van-mozaÃ¯ekkeien-van-het-1ste-formaat': KeuzelijstWaarde(invulwaarde='bestratingen-van-mozaÃ¯ekkeien-van-het-1ste-formaat',
                                                                                label='bestratingen van mozaÃ¯ekkeien van het 1ste formaat',
                                                                                status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                                                                definitie='Bestratingen van mozaÃ¯ekkeien van het 1ste formaat.',
                                                                                objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlMozaiekkeiFormaat/bestratingen-van-mozaÃ¯ekkeien-van-het-1ste-formaat'),
        'bestratingen-van-mozaÃ¯ekkeien-van-het-2de-formaat': KeuzelijstWaarde(invulwaarde='bestratingen-van-mozaÃ¯ekkeien-van-het-2de-formaat',
                                                                               label='bestratingen van mozaÃ¯ekkeien van het 2de formaat',
                                                                               status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                                                               definitie='Bestratingen van mozaÃ¯ekkeien van het 2de formaat.',
                                                                               objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlMozaiekkeiFormaat/bestratingen-van-mozaÃ¯ekkeien-van-het-2de-formaat'),
        'bestratingen-van-mozaÃ¯ekkeien-van-het-3de-formaat': KeuzelijstWaarde(invulwaarde='bestratingen-van-mozaÃ¯ekkeien-van-het-3de-formaat',
                                                                               label='bestratingen van mozaÃ¯ekkeien van het 3de formaat',
                                                                               status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                                                               definitie='Bestratingen van mozaÃ¯ekkeien van het 3de formaat.',
                                                                               objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlMozaiekkeiFormaat/bestratingen-van-mozaÃ¯ekkeien-van-het-3de-formaat'),
        'bestratingen-van-mozaÃ¯ekkeien-van-het-4de-formaat': KeuzelijstWaarde(invulwaarde='bestratingen-van-mozaÃ¯ekkeien-van-het-4de-formaat',
                                                                               label='bestratingen van mozaÃ¯ekkeien van het 4de formaat',
                                                                               status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                                                               definitie='Bestratingen van mozaÃ¯ekkeien van het 4de formaat.',
                                                                               objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlMozaiekkeiFormaat/bestratingen-van-mozaÃ¯ekkeien-van-het-4de-formaat'),
        'bestratingen-van-mozaÃ¯ekkeien-van-het-5de-formaat': KeuzelijstWaarde(invulwaarde='bestratingen-van-mozaÃ¯ekkeien-van-het-5de-formaat',
                                                                               label='bestratingen van mozaÃ¯ekkeien van het 5de formaat',
                                                                               status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                                                               definitie='Bestratingen van mozaÃ¯ekkeien van het 5de formaat.',
                                                                               objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlMozaiekkeiFormaat/bestratingen-van-mozaÃ¯ekkeien-van-het-5de-formaat')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

