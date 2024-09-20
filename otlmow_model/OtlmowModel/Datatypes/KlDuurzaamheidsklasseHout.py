# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlDuurzaamheidsklasseHout(KeuzelijstField):
    """De resistentie van het kernhout tegen ongunstige omstandigheden."""
    naam = 'KlDuurzaamheidsklasseHout'
    label = 'Duurzaamheidsklasse van hout'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#KlDuurzaamheidsklasseHout'
    definition = 'De resistentie van het kernhout tegen ongunstige omstandigheden.'
    status = 'https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlDuurzaamheidsklasseHout'
    options = {
        'klasse-i': KeuzelijstWaarde(invulwaarde='klasse-i',
                                     label='Klasse I',
                                     status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                     definitie='Zeer duurzaam.',
                                     objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlDuurzaamheidsklasseHout/klasse-i'),
        'klasse-ii': KeuzelijstWaarde(invulwaarde='klasse-ii',
                                      label='Klasse II',
                                      status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                      definitie='Duurzaam.',
                                      objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlDuurzaamheidsklasseHout/klasse-ii'),
        'klasse-iii': KeuzelijstWaarde(invulwaarde='klasse-iii',
                                       label='Klasse III',
                                       status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                       definitie='Matig duurzaam.',
                                       objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlDuurzaamheidsklasseHout/klasse-iii'),
        'klasse-iv': KeuzelijstWaarde(invulwaarde='klasse-iv',
                                      label='Klasse IV',
                                      status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                      definitie='Weinig duurzaam.',
                                      objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlDuurzaamheidsklasseHout/klasse-iv'),
        'klasse-v': KeuzelijstWaarde(invulwaarde='klasse-v',
                                     label='Klasse V',
                                     status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                     definitie='Niet duurzaam.',
                                     objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlDuurzaamheidsklasseHout/klasse-v')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

