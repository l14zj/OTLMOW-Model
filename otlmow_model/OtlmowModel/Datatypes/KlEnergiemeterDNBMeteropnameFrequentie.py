# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlEnergiemeterDNBMeteropnameFrequentie(KeuzelijstField):
    """Frequentie waarmee de meterstand opgenomen wordt door de netbeheerder."""
    naam = 'KlEnergiemeterDNBMeteropnameFrequentie'
    label = 'Energiemeter DNB meteropname frequentie'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlEnergiemeterDNBMeteropnameFrequentie'
    definition = 'Frequentie waarmee de meterstand opgenomen wordt door de netbeheerder.'
    status = 'https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlEnergiemeterDNBMeteropnameFrequentie'
    options = {
        'AMR': KeuzelijstWaarde(invulwaarde='AMR',
                                label='AMR',
                                status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                definitie='automatische meter reading',
                                objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlEnergiemeterDNBMeteropnameFrequentie/AMR'),
        'MMR': KeuzelijstWaarde(invulwaarde='MMR',
                                label='MMR',
                                status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlEnergiemeterDNBMeteropnameFrequentie/MMR'),
        'YMR': KeuzelijstWaarde(invulwaarde='YMR',
                                label='YMR',
                                status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                definitie='jaarlijks',
                                objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlEnergiemeterDNBMeteropnameFrequentie/YMR')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

