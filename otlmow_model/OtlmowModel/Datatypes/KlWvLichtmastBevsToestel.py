# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlWvLichtmastBevsToestel(KeuzelijstField):
    """De standaard bevestigingen van verlichtingstoestellen aan lichtmasten."""
    naam = 'KlWvLichtmastBevsToestel'
    label = 'Bevestiging voor wegverlichtingstoestellen'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlWvLichtmastBevsToestel'
    definition = 'De standaard bevestigingen van verlichtingstoestellen aan lichtmasten.'
    status = 'https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlWvLichtmastBevsToestel'
    options = {
        'arm-60mm': KeuzelijstWaarde(invulwaarde='arm-60mm',
                                     label='arm 60mm',
                                     status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                     definitie='arm 60mm',
                                     objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlWvLichtmastBevsToestel/arm-60mm'),
        'kroon': KeuzelijstWaarde(invulwaarde='kroon',
                                  label='kroon',
                                  status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                  definitie='keuzelijst (Niet van toepassing, T-stuk, Mediaanbalk I, Mediaanbalk U, Mediaanbalk H, Ossenkop, Kroon, Andere)./ CLASS : VPLMAST',
                                  objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlWvLichtmastBevsToestel/kroon'),
        'mediaanbalk-H': KeuzelijstWaarde(invulwaarde='mediaanbalk-H',
                                          label='mediaanbalk H',
                                          status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                          definitie='keuzelijst (Niet van toepassing, T-stuk, Mediaanbalk I, Mediaanbalk U, Mediaanbalk H, Ossenkop, Kroon, Andere)./ CLASS : VPLMAST',
                                          objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlWvLichtmastBevsToestel/mediaanbalk-H'),
        'mediaanbalk-I': KeuzelijstWaarde(invulwaarde='mediaanbalk-I',
                                          label='mediaanbalk I',
                                          status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                          definitie='keuzelijst (Niet van toepassing, T-stuk, Mediaanbalk I, Mediaanbalk U, Mediaanbalk H, Ossenkop, Kroon, Andere)./ CLASS : VPLMAST',
                                          objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlWvLichtmastBevsToestel/mediaanbalk-I'),
        'mediaanbalk-U': KeuzelijstWaarde(invulwaarde='mediaanbalk-U',
                                          label='mediaanbalk U',
                                          status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                          definitie='keuzelijst (Niet van toepassing, T-stuk, Mediaanbalk I, Mediaanbalk U, Mediaanbalk H, Ossenkop, Kroon, Andere)./ CLASS : VPLMAST',
                                          objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlWvLichtmastBevsToestel/mediaanbalk-U'),
        'ossenkop': KeuzelijstWaarde(invulwaarde='ossenkop',
                                     label='ossenkop',
                                     status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                     definitie='keuzelijst (Niet van toepassing, T-stuk, Mediaanbalk I, Mediaanbalk U, Mediaanbalk H, Ossenkop, Kroon, Andere)./ CLASS : VPLMAST',
                                     objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlWvLichtmastBevsToestel/ossenkop'),
        'paaltop-108mm': KeuzelijstWaarde(invulwaarde='paaltop-108mm',
                                          label='paaltop 108mm',
                                          status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                          objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlWvLichtmastBevsToestel/paaltop-108mm'),
        'paaltop-60mm': KeuzelijstWaarde(invulwaarde='paaltop-60mm',
                                         label='paaltop 60mm',
                                         status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                         objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlWvLichtmastBevsToestel/paaltop-60mm'),
        'paaltop-76mm': KeuzelijstWaarde(invulwaarde='paaltop-76mm',
                                         label='paaltop 76mm',
                                         status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                         objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlWvLichtmastBevsToestel/paaltop-76mm'),
        'plaat': KeuzelijstWaarde(invulwaarde='plaat',
                                  label='plaat',
                                  status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                  objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlWvLichtmastBevsToestel/plaat'),
        't-stuk': KeuzelijstWaarde(invulwaarde='t-stuk',
                                   label='t-stuk',
                                   status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                   definitie='keuzelijst (Niet van toepassing, T-stuk, Mediaanbalk I, Mediaanbalk U, Mediaanbalk H, Ossenkop, Kroon, Andere)./ CLASS : VPLMAST',
                                   objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlWvLichtmastBevsToestel/t-stuk')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

