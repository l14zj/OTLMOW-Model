# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlBoomGroeifase(KeuzelijstField):
    """De verschillende fases van beheer volgens de verschillende levensfases."""
    naam = 'KlBoomGroeifase'
    label = 'Groeifasen'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlBoomGroeifase'
    definition = 'De verschillende fases van beheer volgens de verschillende levensfases.'
    status = 'https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlBoomGroeifase'
    options = {
        'dood': KeuzelijstWaarde(invulwaarde='dood',
                                 label='dood',
                                 status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                 definitie='Dood',
                                 objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlBoomGroeifase/dood'),
        'eindfase': KeuzelijstWaarde(invulwaarde='eindfase',
                                     label='eindfase',
                                     status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                     definitie='De periode waarbij regressie/aftakeling plaatsvindt Ã¢â‚¬â€œ beheer gericht op in stand houding (kroonverzorging)',
                                     objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlBoomGroeifase/eindfase'),
        'jeugdfase': KeuzelijstWaarde(invulwaarde='jeugdfase',
                                      label='jeugdfase',
                                      status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                      definitie='De periode van de lengte-ontwikkeling van de boom Ã¢â‚¬â€œ beheer gericht op tot stand brengen van de takvrije stamlengte (begeleidingssnoei,..)',
                                      objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlBoomGroeifase/jeugdfase'),
        'plantfase': KeuzelijstWaarde(invulwaarde='plantfase',
                                      label='plantfase',
                                      status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                      definitie='De periode na de aanplant waarbij het beheer gericht is op het aanslaan van de boom (water geven, boompalen verwijderen,Ã¢â‚¬Â¦)',
                                      objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlBoomGroeifase/plantfase'),
        'volwassenfase': KeuzelijstWaarde(invulwaarde='volwassenfase',
                                          label='volwassenfase',
                                          status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                          definitie='De periode van de kroonontwikkeling Ã¢â‚¬â€œ beheer gericht op in stand houden van de boom (onderhoudssnoei)',
                                          objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlBoomGroeifase/volwassenfase')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

