# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlFunctieRioleringsstelsel(KeuzelijstField):
    """De verschillende mogelijke functies van het rioleringsstelsel."""
    naam = 'KlFunctieRioleringsstelsel'
    label = 'Functie van rioleringsstelsel'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#KlFunctieRioleringsstelsel'
    definition = 'De verschillende mogelijke functies van het rioleringsstelsel.'
    status = 'https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlFunctieRioleringsstelsel'
    options = {
        'aanvoerstelsel': KeuzelijstWaarde(invulwaarde='aanvoerstelsel',
                                           label='aanvoerstelsel',
                                           status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                           definitie='aanvoerstelsel',
                                           objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlFunctieRioleringsstelsel/aanvoerstelsel'),
        'afvoerstelsel': KeuzelijstWaarde(invulwaarde='afvoerstelsel',
                                          label='afvoerstelsel',
                                          status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                          definitie='afvoerstelsel',
                                          objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlFunctieRioleringsstelsel/afvoerstelsel'),
        'openbare-riolering': KeuzelijstWaarde(invulwaarde='openbare-riolering',
                                               label='openbare riolering',
                                               status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                               definitie='openbare riolering',
                                               objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlFunctieRioleringsstelsel/openbare-riolering')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

