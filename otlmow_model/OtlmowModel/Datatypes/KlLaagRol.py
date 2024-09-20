# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlLaagRol(KeuzelijstField):
    """De mogelijke rollen van de laag."""
    naam = 'KlLaagRol'
    label = 'Laag rol'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlLaagRol'
    definition = 'De mogelijke rollen van de laag.'
    status = 'https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlLaagRol'
    options = {
        'aanvulling': KeuzelijstWaarde(invulwaarde='aanvulling',
                                       label='aanvulling',
                                       status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                       definitie='De laag als aanvulling.',
                                       objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlLaagRol/aanvulling'),
        'bed-van-bestrating': KeuzelijstWaarde(invulwaarde='bed-van-bestrating',
                                               label='bed van bestrating',
                                               status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                               definitie="Dit betekent hetzelfde als 'straatlaag'. Gelieve voor deze optie 'straatlaag' aan te duiden als keuzemogelijkheid!",
                                               objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlLaagRol/bed-van-bestrating'),
        'fundering': KeuzelijstWaarde(invulwaarde='fundering',
                                      label='fundering',
                                      status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                      definitie='De laag als fundering.',
                                      objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlLaagRol/fundering'),
        'fundering-voor-lijnvormige-elementen': KeuzelijstWaarde(invulwaarde='fundering-voor-lijnvormige-elementen',
                                                                 label='fundering voor lijnvormige elementen',
                                                                 status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                                                 definitie='De laag als fundering voor lijnvormige elementen.',
                                                                 objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlLaagRol/fundering-voor-lijnvormige-elementen'),
        'omhulling': KeuzelijstWaarde(invulwaarde='omhulling',
                                      label='omhulling',
                                      status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                      definitie='De laag als omhulling.',
                                      objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlLaagRol/omhulling'),
        'onderfundering': KeuzelijstWaarde(invulwaarde='onderfundering',
                                           label='onderfundering',
                                           status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                           definitie='De laag als onderfundering.',
                                           objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlLaagRol/onderfundering'),
        'straatlaag': KeuzelijstWaarde(invulwaarde='straatlaag',
                                       label='straatlaag',
                                       status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                       definitie='De laag als straatlaag',
                                       objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlLaagRol/straatlaag'),
        'verharding': KeuzelijstWaarde(invulwaarde='verharding',
                                       label='verharding',
                                       status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                       definitie='De laag als verharding.',
                                       objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlLaagRol/verharding'),
        'wapening': KeuzelijstWaarde(invulwaarde='wapening',
                                     label='wapening',
                                     status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                     definitie='De laag als wapening en/of bescherming.',
                                     objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlLaagRol/wapening')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

