# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlCorrosiebelastingscategorie(KeuzelijstField):
    """De mogelijke codes om de mate van corrosieve belasting in een bepaalde omgeving te beschrijven."""
    naam = 'KlCorrosiebelastingscategorie'
    label = 'Corrosiebelastingscategorie'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#KlCorrosiebelastingscategorie'
    definition = 'De mogelijke codes om de mate van corrosieve belasting in een bepaalde omgeving te beschrijven.'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlCorrosiebelastingscategorie'
    options = {
        'c1-zeer-laag': KeuzelijstWaarde(invulwaarde='c1-zeer-laag',
                                         label='C1 - Zeer Laag',
                                         status='ingebruik',
                                         definitie='Binnen : Verwarmde gebouwen met een schone atmosfeer.',
                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlCorrosiebelastingscategorie/c1-zeer-laag'),
        'c2-laag': KeuzelijstWaarde(invulwaarde='c2-laag',
                                    label='C2 - Laag',
                                    status='ingebruik',
                                    definitie='Binnen: Niet-verwarmde gebouwen waar condensatie kan optreden, zoals bv. magazijnen en sporthallen. Buiten: Atmosferen met lage vervuilingsniveaus; meestal landelijke gebieden.',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlCorrosiebelastingscategorie/c2-laag'),
        'c3-gemiddeld': KeuzelijstWaarde(invulwaarde='c3-gemiddeld',
                                         label='C3 - Gemiddeld',
                                         status='ingebruik',
                                         definitie='Binnen: Ruimten met een hoge luchtvochtigheid en enige vervuiling, zoals brouwerijen, melkerijen, washuizen. Buiten: Stedelijke en industriële gebieden met matige zwaveldioxidevervuiling; kustgebieden met lage zoutniveaus.',
                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlCorrosiebelastingscategorie/c3-gemiddeld'),
        'c4-hoog': KeuzelijstWaarde(invulwaarde='c4-hoog',
                                    label='C4 - Hoog',
                                    status='ingebruik',
                                    definitie='Binnen: Chemische fabrieken, zwembaden, kustscheepswerven. Buiten: Industriële gebieden en kustgebieden met matig zoutgehalte.',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlCorrosiebelastingscategorie/c4-hoog'),
        'c5-i-industrieel-zeer-hoog': KeuzelijstWaarde(invulwaarde='c5-i-industrieel-zeer-hoog',
                                                       label='C5-I (Industrieel) - Zeer Hoog',
                                                       status='ingebruik',
                                                       definitie='Binnen: Gebouwen of gebieden met bijna constante condensatie en hoge vervuiling. Buiten: Industriële gebieden met hoge vochtigheid en agressieve atmosfeer.',
                                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlCorrosiebelastingscategorie/c5-i-industrieel-zeer-hoog'),
        'c5-m-marien-zeer-hoog': KeuzelijstWaarde(invulwaarde='c5-m-marien-zeer-hoog',
                                                  label='C5-M (Marien) - Zeer Hoog',
                                                  status='ingebruik',
                                                  definitie='Binnen: Gebouwen of gebieden met bijna constante condensatie en hoge vervuiling. Buiten: Kust- en offshore-gebieden met hoge zoutconcentraties.',
                                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlCorrosiebelastingscategorie/c5-m-marien-zeer-hoog')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

