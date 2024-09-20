# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlVerkenmerkType(KeuzelijstField):
    """Het type verkenmerk."""
    naam = 'KlVerkenmerkType'
    label = 'Verkenmerk type'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlVerkenmerkType'
    definition = 'Het type verkenmerk.'
    status = 'https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlVerkenmerkType'
    options = {
        'type-i': KeuzelijstWaarde(invulwaarde='type-i',
                                   label='Type I',
                                   status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                   definitie='Verkenmerk met de vorm van een haak. Deze wordt horizontaal aangebracht in pijlers, landhoofden, wanden en muren. De kop kan opwaarts of neerwaarts gericht zijn.',
                                   objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlVerkenmerkType/type-i'),
        'type-ii': KeuzelijstWaarde(invulwaarde='type-ii',
                                    label='Type II',
                                    status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                    definitie='Schroef met bolvormige kop met een schacht van 70 mm lengte en 12 mm diameter.',
                                    objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlVerkenmerkType/type-ii'),
        'type-ii-s': KeuzelijstWaarde(invulwaarde='type-ii-s',
                                      label='Type II S',
                                      status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                      definitie='Schroef met bolvormige kop met een schacht van 200 mm lengte en 12 mm diameter.',
                                      objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlVerkenmerkType/type-ii-s'),
        'type-iii': KeuzelijstWaarde(invulwaarde='type-iii',
                                     label='Type III',
                                     status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                     definitie='Ronde staaf, met een totale lengte van 200 mm.',
                                     objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlVerkenmerkType/type-iii'),
        'type-iii-l': KeuzelijstWaarde(invulwaarde='type-iii-l',
                                       label='Type III L',
                                       status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                       definitie='Ronde staaf, met een totale lengte van 300 mm.',
                                       objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlVerkenmerkType/type-iii-l'),
        'type-iii-s': KeuzelijstWaarde(invulwaarde='type-iii-s',
                                       label='Type III S',
                                       status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                       definitie='Ronde staaf, met een totale lengte van 250 mm.',
                                       objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlVerkenmerkType/type-iii-s'),
        'type-iv': KeuzelijstWaarde(invulwaarde='type-iv',
                                    label='Type IV',
                                    status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                    definitie='Verkenmerk met de vorm van een haak. Deze wordt schuin aangebracht. De kop wordt ofwel opwaarts gericht ofwel neerwaarts gericht.',
                                    objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlVerkenmerkType/type-iv'),
        'type-ix': KeuzelijstWaarde(invulwaarde='type-ix',
                                    label='Type IX',
                                    status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                    definitie='Reflecterende tape met richtpunt die wordt gebruikt voor tijdelijke opmetingen, vermits het verkenmerk niet op duurzame wijze kan worden bevestigd.',
                                    objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlVerkenmerkType/type-ix'),
        'type-v': KeuzelijstWaarde(invulwaarde='type-v',
                                   label='Type V',
                                   status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                   definitie='Ronde staaf met een schacht van 70 mm lengte en 12 mm diameter, voorzien van een gegraveerde zwarte kruismarkering.',
                                   objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlVerkenmerkType/type-v'),
        'type-vi': KeuzelijstWaarde(invulwaarde='type-vi',
                                    label='Type VI',
                                    status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                    definitie='Lage bolmoer volgens DIN 917 welke aan de staalstructuur gelast wordt.',
                                    objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlVerkenmerkType/type-vi'),
        'type-vii': KeuzelijstWaarde(invulwaarde='type-vii',
                                     label='Type VII',
                                     status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                     definitie='Verkenmerk dat kan worden uitgevoerd als bout-/moerverbinding met twee sluitringen in gegalvaniseerd staal, als bout met sluitring in gegalvaniseerd staal, als getapte bout met sluitring in gegalvaniseerd staal of als getapte stelschroef met binnenzeskant en gegalvaniseerde of roestvaste moer.',
                                     objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlVerkenmerkType/type-vii'),
        'type-viii': KeuzelijstWaarde(invulwaarde='type-viii',
                                      label='Type VIII',
                                      status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                      definitie='Verkenmerk dat uit een gegroefde plaat met kruis bestaat en dat gedurende de volledige levensduur op het kunstwerk blijft.',
                                      objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlVerkenmerkType/type-viii'),
        'type-x': KeuzelijstWaarde(invulwaarde='type-x',
                                   label='Type X',
                                   status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                   definitie='Vlakke meetplaat.',
                                   objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlVerkenmerkType/type-x')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

