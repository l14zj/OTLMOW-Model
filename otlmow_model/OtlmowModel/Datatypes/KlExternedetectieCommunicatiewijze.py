# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlExternedetectieCommunicatiewijze(KeuzelijstField):
    """Keuzelijst met de verschillende manieren waarop een externe detectie communiceert met een verkeersregelaar."""
    naam = 'KlExternedetectieCommunicatiewijze'
    label = 'Externedetectie communicatiewijze'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlExternedetectieCommunicatiewijze'
    definition = 'Keuzelijst met de verschillende manieren waarop een externe detectie communiceert met een verkeersregelaar.'
    status = 'https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlExternedetectieCommunicatiewijze'
    options = {
        'contact': KeuzelijstWaarde(invulwaarde='contact',
                                    label='contact',
                                    status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                    objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlExternedetectieCommunicatiewijze/contact'),
        'protocol': KeuzelijstWaarde(invulwaarde='protocol',
                                     label='protocol',
                                     status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                     objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlExternedetectieCommunicatiewijze/protocol'),
        'serieel': KeuzelijstWaarde(invulwaarde='serieel',
                                    label='serieel',
                                    status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                    objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlExternedetectieCommunicatiewijze/serieel')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

