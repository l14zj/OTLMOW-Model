# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlDwarseMarkeringCode(KeuzelijstField):
    """Codes van de dwarse markering."""
    naam = 'KlDwarseMarkeringCode'
    label = 'Dwarse markering code'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlDwarseMarkeringCode'
    definition = 'Codes van de dwarse markering.'
    status = 'https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlDwarseMarkeringCode'
    options = {
        'DAMBRD': KeuzelijstWaarde(invulwaarde='DAMBRD',
                                   label='DAMBRD',
                                   status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                   definitie='Dambord',
                                   objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlDwarseMarkeringCode/DAMBRD'),
        'DREMPEL-1.2': KeuzelijstWaarde(invulwaarde='DREMPEL-1.2',
                                        label='DREMPEL 1.2',
                                        status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                        definitie='Verkeersdrempel markering',
                                        objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlDwarseMarkeringCode/DREMPEL-1.2'),
        'DRH-fiets-(0.3)': KeuzelijstWaarde(invulwaarde='DRH-fiets-(0.3)',
                                            label='DRH fiets (0.3)',
                                            status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                            definitie='Driehoek fiets',
                                            objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlDwarseMarkeringCode/DRH-fiets-(0.3)'),
        'DRH-std-(0.7)': KeuzelijstWaarde(invulwaarde='DRH-std-(0.7)',
                                          label='DRH std (0.7)',
                                          status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                          definitie='Driehoek standaard',
                                          objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlDwarseMarkeringCode/DRH-std-(0.7)'),
        'FLV': KeuzelijstWaarde(invulwaarde='FLV',
                                label='FLV',
                                status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                definitie='Verbindingsmarkering voor fietsers.',
                                objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlDwarseMarkeringCode/FLV'),
        'FOP': KeuzelijstWaarde(invulwaarde='FOP',
                                label='FOP',
                                status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                definitie='Fietsoversteekplaats met blokken',
                                objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlDwarseMarkeringCode/FOP'),
        'PARKEER': KeuzelijstWaarde(invulwaarde='PARKEER',
                                    label='PARKEER',
                                    status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                    definitie='Parkeerstrook',
                                    objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlDwarseMarkeringCode/PARKEER'),
        'RIBBELSTROOK---AFREMMINGSSTREPEN': KeuzelijstWaarde(invulwaarde='RIBBELSTROOK---AFREMMINGSSTREPEN',
                                                             label='RIBBELSTROOK - AFREMMINGSSTREPEN',
                                                             status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                                             definitie='Afremmingsstreep',
                                                             objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlDwarseMarkeringCode/RIBBELSTROOK---AFREMMINGSSTREPEN'),
        'STOPSTRP': KeuzelijstWaarde(invulwaarde='STOPSTRP',
                                     label='STOPSTRP',
                                     status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                     definitie='Code voor de stopstreep',
                                     objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlDwarseMarkeringCode/STOPSTRP'),
        'STOPSTRP-OFOS': KeuzelijstWaarde(invulwaarde='STOPSTRP-OFOS',
                                          label='STOPSTRP-OFOS',
                                          status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                          definitie='Code voor de stopstreep OFOS',
                                          objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlDwarseMarkeringCode/STOPSTRP-OFOS'),
        'VOP-(3)': KeuzelijstWaarde(invulwaarde='VOP-(3)',
                                    label='VOP (3)',
                                    status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                    definitie='Voetgangers-oversteekplaats (3 meter)',
                                    objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlDwarseMarkeringCode/VOP-(3)'),
        'VOP-(4)': KeuzelijstWaarde(invulwaarde='VOP-(4)',
                                    label='VOP (4)',
                                    status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                    definitie='Voetgangers-oversteekplaats (4 meter)',
                                    objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlDwarseMarkeringCode/VOP-(4)'),
        'VOP-(var)': KeuzelijstWaarde(invulwaarde='VOP-(var)',
                                      label='VOP (var)',
                                      status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                      definitie='Voetgangers-oversteekplaats (te meten)',
                                      objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlDwarseMarkeringCode/VOP-(var)'),
        'VVA-0.4-(0.6)': KeuzelijstWaarde(invulwaarde='VVA-0.4-(0.6)',
                                          label='VVA 0.4 (0.6)',
                                          status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                          definitie='Verdrijvingsvlak (40 % opp. v.h. vlak)',
                                          objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlDwarseMarkeringCode/VVA-0.4-(0.6)'),
        'VVA-1-(2)': KeuzelijstWaarde(invulwaarde='VVA-1-(2)',
                                      label='VVA 1 (2)',
                                      status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                      definitie='Verdrijvingsvlak (33 % opp. v.h. vlak)',
                                      objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlDwarseMarkeringCode/VVA-1-(2)')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

