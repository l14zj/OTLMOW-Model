# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlCBVOppervlaktebehandeling(KeuzelijstField):
    """Oppervalktebehandelingen van de cement/beton verharding."""
    naam = 'KlCBVOppervlaktebehandeling'
    label = 'CBV oppervlaktebehandeling'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlCBVOppervlaktebehandeling'
    definition = 'Oppervalktebehandelingen van de cement/beton verharding.'
    status = 'https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlCBVOppervlaktebehandeling'
    options = {
        'Reinigen-met-water-onder-hoge-druk-(minstens-50-bar)-': KeuzelijstWaarde(invulwaarde='Reinigen-met-water-onder-hoge-druk-(minstens-50-bar)-',
                                                                                  label='Reinigen met water onder hoge druk (minstens 50 bar) ',
                                                                                  status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                                                                  definitie='Reinigen met water onder hoge druk (minstens 50 bar) ',
                                                                                  objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlCBVOppervlaktebehandeling/Reinigen-met-water-onder-hoge-druk-(minstens-50-bar)-'),
        'bezemen': KeuzelijstWaarde(invulwaarde='bezemen',
                                    label='bezemen',
                                    status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                    definitie='Bezemen',
                                    objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlCBVOppervlaktebehandeling/bezemen'),
        'eenvoudig-dwars-bezemen': KeuzelijstWaarde(invulwaarde='eenvoudig-dwars-bezemen',
                                                    label='eenvoudig dwars bezemen',
                                                    status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                                    definitie='Eenvoudig dwars bezemen',
                                                    objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlCBVOppervlaktebehandeling/eenvoudig-dwars-bezemen'),
        'eenvoudig-langs-bezemen': KeuzelijstWaarde(invulwaarde='eenvoudig-langs-bezemen',
                                                    label='eenvoudig langs bezemen',
                                                    status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                                    definitie='Eenvoudig langs bezemen',
                                                    objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlCBVOppervlaktebehandeling/eenvoudig-langs-bezemen'),
        'figureren': KeuzelijstWaarde(invulwaarde='figureren',
                                      label='figureren',
                                      status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                      definitie='Figureren',
                                      objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlCBVOppervlaktebehandeling/figureren'),
        'uitwassen-van-het-steenslagskelet': KeuzelijstWaarde(invulwaarde='uitwassen-van-het-steenslagskelet',
                                                              label='uitwassen van het steenslagskelet',
                                                              status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                                              definitie='Uitwassen van het steenslagskelet',
                                                              objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlCBVOppervlaktebehandeling/uitwassen-van-het-steenslagskelet')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

