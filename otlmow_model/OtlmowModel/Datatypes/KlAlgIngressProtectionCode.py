# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlAlgIngressProtectionCode(KeuzelijstField):
    """De IP-codering als een aanduiding voor de mate van beveiliging van de constructie van elektrische of elektronische apparatuur tegen eigen schade door gebruik in 'vijandige omgevingen' en tegen eventueel gevaar voor de gebruiker volgens IEC 60529."""
    naam = 'KlAlgIngressProtectionCode'
    label = 'Ingress Protection Codering'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlAlgIngressProtectionCode'
    definition = "De IP-codering als een aanduiding voor de mate van beveiliging van de constructie van elektrische of elektronische apparatuur tegen eigen schade door gebruik in 'vijandige omgevingen' en tegen eventueel gevaar voor de gebruiker volgens IEC 60529."
    status = 'https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlAlgIngressProtectionCode'
    options = {
        'i-p-44': KeuzelijstWaarde(invulwaarde='i-p-44',
                                   label='IP44',
                                   status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                   definitie='Bescherming tegen spitse voorwerpen en plensdicht.',
                                   objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAlgIngressProtectionCode/i-p-44'),
        'i-p-65': KeuzelijstWaarde(invulwaarde='i-p-65',
                                   label='IP65',
                                   status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                   definitie='Stofvrij en sproeidicht.',
                                   objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAlgIngressProtectionCode/i-p-65'),
        'ip44': KeuzelijstWaarde(invulwaarde='ip44',
                                 label='IP44',
                                 status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                 definitie='Bescherming tegen spitse voorwerpen en plensdicht.',
                                 objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAlgIngressProtectionCode/ip44'),
        'ip54': KeuzelijstWaarde(invulwaarde='ip54',
                                 label='IP54',
                                 status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                 definitie='Spatwaterdicht en stofvrij.',
                                 objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAlgIngressProtectionCode/ip54'),
        'ip66': KeuzelijstWaarde(invulwaarde='ip66',
                                 label='IP66',
                                 status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                 definitie='volledig beschermd is tegen stof en waterdicht is tot regen en golven van water.',
                                 objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAlgIngressProtectionCode/ip66')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

