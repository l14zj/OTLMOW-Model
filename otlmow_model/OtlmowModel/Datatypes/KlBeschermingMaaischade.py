# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlBeschermingMaaischade(KeuzelijstField):
    """De middelen als bescherming tegen maaischade."""
    naam = 'KlBeschermingMaaischade'
    label = 'Bescherming maaischade'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlBeschermingMaaischade'
    definition = 'De middelen als bescherming tegen maaischade.'
    status = 'https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlBeschermingMaaischade'
    options = {
        'houten-paal': KeuzelijstWaarde(invulwaarde='houten-paal',
                                        label='houten paal',
                                        status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                        definitie='Bescherming dmv een houten paal.',
                                        objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlBeschermingMaaischade/houten-paal'),
        'kunststof': KeuzelijstWaarde(invulwaarde='kunststof',
                                      label='kunststof',
                                      status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                      definitie='Bescherming in kunststof.',
                                      objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlBeschermingMaaischade/kunststof')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

