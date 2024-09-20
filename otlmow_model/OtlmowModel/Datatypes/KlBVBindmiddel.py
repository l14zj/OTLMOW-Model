# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlBVBindmiddel(KeuzelijstField):
    """De mogelijke bindmiddelen bij de bitumineuze verharding."""
    naam = 'KlBVBindmiddel'
    label = 'BV bindmiddel'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlBVBindmiddel'
    definition = 'De mogelijke bindmiddelen bij de bitumineuze verharding.'
    status = 'https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlBVBindmiddel'
    options = {
        'bindmiddel-met-additieven': KeuzelijstWaarde(invulwaarde='bindmiddel-met-additieven',
                                                      label='bindmiddel met additieven',
                                                      status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                                      definitie='bindmiddel met additieven',
                                                      objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlBVBindmiddel/bindmiddel-met-additieven'),
        'bindmiddel-met-positief-indringingsgetal': KeuzelijstWaarde(invulwaarde='bindmiddel-met-positief-indringingsgetal',
                                                                     label='bindmiddel met positief indringingsgetal',
                                                                     status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                                                     definitie='bindmiddel met positief indringingsgetal',
                                                                     objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlBVBindmiddel/bindmiddel-met-positief-indringingsgetal'),
        'gewoon-wegenbitumen': KeuzelijstWaarde(invulwaarde='gewoon-wegenbitumen',
                                                label='gewoon wegenbitumen',
                                                status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                                definitie='gewoon wegenbitumen',
                                                objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlBVBindmiddel/gewoon-wegenbitumen'),
        'gewoon-wegenbitumen-met-natuurbitumen': KeuzelijstWaarde(invulwaarde='gewoon-wegenbitumen-met-natuurbitumen',
                                                                  label='gewoon wegenbitumen met natuurbitumen',
                                                                  status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                                                  definitie='gewoon wegenbitumen met natuurbitumen',
                                                                  objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlBVBindmiddel/gewoon-wegenbitumen-met-natuurbitumen'),
        'hard-bitumen-B-10-20-of-B15-25': KeuzelijstWaarde(invulwaarde='hard-bitumen-B-10-20-of-B15-25',
                                                           label='hard bitumen B 10-20 of B15-25',
                                                           status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                                           definitie='hard bitumen B 10/20 of B15/25',
                                                           objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlBVBindmiddel/hard-bitumen-B-10-20-of-B15-25'),
        'kleurloos-synthetisch-bindmiddel': KeuzelijstWaarde(invulwaarde='kleurloos-synthetisch-bindmiddel',
                                                             label='kleurloos synthetisch bindmiddel',
                                                             status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                                             definitie='kleurloos synthetisch bindmiddel',
                                                             objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlBVBindmiddel/kleurloos-synthetisch-bindmiddel'),
        'met-polymeren-gemodificeerd-kleurloos-synthetisch-bindmiddel': KeuzelijstWaarde(invulwaarde='met-polymeren-gemodificeerd-kleurloos-synthetisch-bindmiddel',
                                                                                         label='met polymeren gemodificeerd kleurloos synthetisch bindmiddel',
                                                                                         status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                                                                         definitie='met polymeren gemodificeerd kleurloos synthetisch bindmiddel',
                                                                                         objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlBVBindmiddel/met-polymeren-gemodificeerd-kleurloos-synthetisch-bindmiddel'),
        'niet-gespecifieerd-(keuze-van-de-aannemer)': KeuzelijstWaarde(invulwaarde='niet-gespecifieerd-(keuze-van-de-aannemer)',
                                                                       label='niet gespecifieerd (keuze van de aannemer)',
                                                                       status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                                                       definitie='niet gespecifieerd (keuze van de aannemer)',
                                                                       objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlBVBindmiddel/niet-gespecifieerd-(keuze-van-de-aannemer)'),
        'pigmenteerbaar-bitumen': KeuzelijstWaarde(invulwaarde='pigmenteerbaar-bitumen',
                                                   label='pigmenteerbaar bitumen',
                                                   status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                                   definitie='pigmenteerbaar bitumen',
                                                   objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlBVBindmiddel/pigmenteerbaar-bitumen'),
        'polymeerbitumen': KeuzelijstWaarde(invulwaarde='polymeerbitumen',
                                            label='polymeerbitumen',
                                            status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                            definitie='polymeerbitumen',
                                            objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlBVBindmiddel/polymeerbitumen')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

