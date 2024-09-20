# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlStortsteenPlaatsingswijze(KeuzelijstField):
    """De manier waarop de stenen worden geplaatst."""
    naam = 'KlStortsteenPlaatsingswijze'
    label = 'Plaatsingswijze'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlStortsteenPlaatsingswijze'
    definition = 'De manier waarop de stenen worden geplaatst.'
    status = 'https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlStortsteenPlaatsingswijze'
    options = {
        'gestapeld': KeuzelijstWaarde(invulwaarde='gestapeld',
                                      label='gestapeld',
                                      status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                      objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlStortsteenPlaatsingswijze/gestapeld'),
        'gewone-bestorting-met-fixatie-colloÃ¯daal-beton': KeuzelijstWaarde(invulwaarde='gewone-bestorting-met-fixatie-colloÃ¯daal-beton',
                                                                            label='gewone bestorting met fixatie colloÃ¯daal beton',
                                                                            status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                                                            definitie='gewone bestorting met fixatie colloÃ¯daal beton',
                                                                            objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlStortsteenPlaatsingswijze/gewone-bestorting-met-fixatie-colloÃ¯daal-beton'),
        'gewone-bestorting-zonder-fixatie-colloÃ¯daal-beton': KeuzelijstWaarde(invulwaarde='gewone-bestorting-zonder-fixatie-colloÃ¯daal-beton',
                                                                               label='gewone bestorting zonder fixatie colloÃ¯daal beton',
                                                                               status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                                                               definitie='gewone bestorting zonder fixatie colloÃ¯daal beton',
                                                                               objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlStortsteenPlaatsingswijze/gewone-bestorting-zonder-fixatie-colloÃ¯daal-beton'),
        'stroomkuilenprofiel-met-fixatie-colloÃ¯daal-beton': KeuzelijstWaarde(invulwaarde='stroomkuilenprofiel-met-fixatie-colloÃ¯daal-beton',
                                                                              label='stroomkuilenprofiel met fixatie colloÃ¯daal beton',
                                                                              status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                                                              definitie='stroomkuilenprofiel met fixatie colloÃ¯daal beton',
                                                                              objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlStortsteenPlaatsingswijze/stroomkuilenprofiel-met-fixatie-colloÃ¯daal-beton'),
        'stroomkuilenprofiel-zonder-fixatie-colloÃ¯daal-beton': KeuzelijstWaarde(invulwaarde='stroomkuilenprofiel-zonder-fixatie-colloÃ¯daal-beton',
                                                                                 label='stroomkuilenprofiel zonder fixatie colloÃ¯daal beton',
                                                                                 status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                                                                 definitie='stroomkuilenprofiel zonder fixatie colloÃ¯daal beton',
                                                                                 objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlStortsteenPlaatsingswijze/stroomkuilenprofiel-zonder-fixatie-colloÃ¯daal-beton')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

