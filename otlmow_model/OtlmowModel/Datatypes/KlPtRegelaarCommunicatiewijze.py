# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlPtRegelaarCommunicatiewijze(KeuzelijstField):
    """Keuzelijst met de verschillende manieren waarop een PT_Regelaar communiceert met de Verkeersregelaar."""
    naam = 'KlPtRegelaarCommunicatiewijze'
    label = 'Ptregelaar communicatiewijze'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlPtRegelaarCommunicatiewijze'
    definition = 'Keuzelijst met de verschillende manieren waarop een PT_Regelaar communiceert met de Verkeersregelaar.'
    status = 'https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlPtRegelaarCommunicatiewijze'
    options = {
        'VR-PT-kaart': KeuzelijstWaarde(invulwaarde='VR-PT-kaart',
                                        label='VR PT-kaart',
                                        status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                        definitie='De PT kaart is een module die is ingebouwd in de verkeersregelaar',
                                        objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlPtRegelaarCommunicatiewijze/VR-PT-kaart'),
        'contact': KeuzelijstWaarde(invulwaarde='contact',
                                    label='contact',
                                    status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                    objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlPtRegelaarCommunicatiewijze/contact'),
        'protocol': KeuzelijstWaarde(invulwaarde='protocol',
                                     label='protocol',
                                     status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                     objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlPtRegelaarCommunicatiewijze/protocol'),
        'serieel': KeuzelijstWaarde(invulwaarde='serieel',
                                    label='serieel',
                                    status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                    objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlPtRegelaarCommunicatiewijze/serieel')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

