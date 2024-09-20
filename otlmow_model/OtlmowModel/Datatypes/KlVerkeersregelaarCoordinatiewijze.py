# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlVerkeersregelaarCoordinatiewijze(KeuzelijstField):
    """Keuzelijst met de voorkomende manieren van coordinate voor verkeersregelaars."""
    naam = 'KlVerkeersregelaarCoordinatiewijze'
    label = 'Verkeersregelaar coordinatiewijze'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlVerkeersregelaarCoordinatiewijze'
    definition = 'Keuzelijst met de voorkomende manieren van coordinate voor verkeersregelaars.'
    status = 'https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlVerkeersregelaarCoordinatiewijze'
    options = {
        'centraal': KeuzelijstWaarde(invulwaarde='centraal',
                                     label='centraal',
                                     status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                     objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlVerkeersregelaarCoordinatiewijze/centraal'),
        'geen': KeuzelijstWaarde(invulwaarde='geen',
                                 label='geen',
                                 status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                 objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlVerkeersregelaarCoordinatiewijze/geen'),
        'its-app': KeuzelijstWaarde(invulwaarde='its-app',
                                    label='ITS-app',
                                    status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                    definitie='Coordinatie door ITS-app.',
                                    objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlVerkeersregelaarCoordinatiewijze/its-app'),
        'klok': KeuzelijstWaarde(invulwaarde='klok',
                                 label='klok',
                                 status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                 objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlVerkeersregelaarCoordinatiewijze/klok'),
        'master': KeuzelijstWaarde(invulwaarde='master',
                                   label='master',
                                   status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                   objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlVerkeersregelaarCoordinatiewijze/master'),
        'pulsen': KeuzelijstWaarde(invulwaarde='pulsen',
                                   label='pulsen',
                                   status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                   objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlVerkeersregelaarCoordinatiewijze/pulsen'),
        'slave': KeuzelijstWaarde(invulwaarde='slave',
                                  label='slave',
                                  status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                  objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlVerkeersregelaarCoordinatiewijze/slave')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

