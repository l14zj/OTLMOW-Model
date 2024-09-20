# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlMeteoFotoBeschrijving(KeuzelijstField):
    """De mogelijke beschrijvingen voor meteo-gerelateerde foto's."""
    naam = 'KlMeteoFotoBeschrijving'
    label = 'Meteo foto beschrijving'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#KlMeteoFotoBeschrijving'
    definition = "De mogelijke beschrijvingen voor meteo-gerelateerde foto's."
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlMeteoFotoBeschrijving'
    options = {
        'foto-rechte-steun-met-sensoren': KeuzelijstWaarde(invulwaarde='foto-rechte-steun-met-sensoren',
                                                           label='Foto rechte steun met sensoren',
                                                           status='ingebruik',
                                                           definitie='Foto rechte steun met sensoren',
                                                           objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlMeteoFotoBeschrijving/foto-rechte-steun-met-sensoren'),
        'foto-site-kijkrichting-noord': KeuzelijstWaarde(invulwaarde='foto-site-kijkrichting-noord',
                                                         label='Foto site kijkrichting noord',
                                                         status='ingebruik',
                                                         definitie='Foto site kijkrichting noord',
                                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlMeteoFotoBeschrijving/foto-site-kijkrichting-noord'),
        'foto-site-kijkrichting-oost': KeuzelijstWaarde(invulwaarde='foto-site-kijkrichting-oost',
                                                        label='Foto site kijkrichting oost',
                                                        status='ingebruik',
                                                        definitie='Foto site kijkrichting oost',
                                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlMeteoFotoBeschrijving/foto-site-kijkrichting-oost'),
        'foto-site-kijkrichting-west': KeuzelijstWaarde(invulwaarde='foto-site-kijkrichting-west',
                                                        label='Foto site kijkrichting west',
                                                        status='ingebruik',
                                                        definitie='Foto site kijkrichting west',
                                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlMeteoFotoBeschrijving/foto-site-kijkrichting-west'),
        'foto-site-kijkrichting-zuid': KeuzelijstWaarde(invulwaarde='foto-site-kijkrichting-zuid',
                                                        label='Foto site kijkrichting zuid',
                                                        status='ingebruik',
                                                        definitie='Foto site kijkrichting zuid',
                                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlMeteoFotoBeschrijving/foto-site-kijkrichting-zuid')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

