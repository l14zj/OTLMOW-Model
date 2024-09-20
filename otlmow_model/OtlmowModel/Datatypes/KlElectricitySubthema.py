# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlElectricitySubthema(KeuzelijstField):
    """Lijst voor classificatie van elektrische kabels en appurtenances."""
    naam = 'KlElectricitySubthema'
    label = 'Electricity subthema'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#KlElectricitySubthema'
    definition = 'Lijst voor classificatie van elektrische kabels en appurtenances.'
    status = 'https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlElectricitySubthema'
    options = {
        'elektriciteitdistributiehoogspanning': KeuzelijstWaarde(invulwaarde='elektriciteitdistributiehoogspanning',
                                                                 label='elektriciteitDistributieHoogspanning',
                                                                 status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                                                 objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlElectricitySubthema/elektriciteitdistributiehoogspanning'),
        'elektriciteitdistributielaagspanning': KeuzelijstWaarde(invulwaarde='elektriciteitdistributielaagspanning',
                                                                 label='elektriciteitDistributieLaagspanning',
                                                                 status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                                                 objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlElectricitySubthema/elektriciteitdistributielaagspanning'),
        'elektriciteitopenbareverlichting': KeuzelijstWaarde(invulwaarde='elektriciteitopenbareverlichting',
                                                             label='elektriciteitOpenbareVerlichting',
                                                             status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                                             objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlElectricitySubthema/elektriciteitopenbareverlichting'),
        'elektriciteittransport': KeuzelijstWaarde(invulwaarde='elektriciteittransport',
                                                   label='elektriciteitTransport',
                                                   status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                                   objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlElectricitySubthema/elektriciteittransport'),
        'elektriciteittransportplaatselijk': KeuzelijstWaarde(invulwaarde='elektriciteittransportplaatselijk',
                                                              label='elektriciteitTransportPlaatselijk',
                                                              status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                                              objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlElectricitySubthema/elektriciteittransportplaatselijk'),
        'elektriciteitverkeershandhavingssystemen': KeuzelijstWaarde(invulwaarde='elektriciteitverkeershandhavingssystemen',
                                                                     label='elektriciteitVerkeershandhavingssystemen',
                                                                     status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                                                     objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlElectricitySubthema/elektriciteitverkeershandhavingssystemen'),
        'elektriciteitverkeerslichten': KeuzelijstWaarde(invulwaarde='elektriciteitverkeerslichten',
                                                         label='elektriciteitVerkeerslichten',
                                                         status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                                         objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlElectricitySubthema/elektriciteitverkeerslichten')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

