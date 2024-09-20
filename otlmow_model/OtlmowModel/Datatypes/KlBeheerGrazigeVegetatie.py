# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlBeheerGrazigeVegetatie(KeuzelijstField):
    """De verschillende soorten van beheer voor grazige vegetatie."""
    naam = 'KlBeheerGrazigeVegetatie'
    label = 'Beheer grazige vegetatie'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/levenscyclus#KlBeheerGrazigeVegetatie'
    definition = 'De verschillende soorten van beheer voor grazige vegetatie.'
    status = 'https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlBeheerGrazigeVegetatie'
    options = {
        'afboorden': KeuzelijstWaarde(invulwaarde='afboorden',
                                      label='afboorden',
                                      status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                      definitie='Het afsteken van de overgroeiende vegetatie langs de rand van de verharding. (wordt afranden genoemd in SB250) ',
                                      objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlBeheerGrazigeVegetatie/afboorden'),
        'aflagen': KeuzelijstWaarde(invulwaarde='aflagen',
                                    label='aflagen',
                                    status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                    definitie='Het verwijderen van de bovenste grondlaag met begroeiing om afwatering te garanderen',
                                    objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlBeheerGrazigeVegetatie/aflagen'),
        'begrazing': KeuzelijstWaarde(invulwaarde='begrazing',
                                      label='begrazing',
                                      status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                      definitie='De vegetatie wordt begraasd door dieren.',
                                      objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlBeheerGrazigeVegetatie/begrazing'),
        'beluchten': KeuzelijstWaarde(invulwaarde='beluchten',
                                      label='beluchten',
                                      status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                      definitie='Beluchten van grazige vegetatie.',
                                      objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlBeheerGrazigeVegetatie/beluchten'),
        'bestrijden-ongewenste-vegetatie': KeuzelijstWaarde(invulwaarde='bestrijden-ongewenste-vegetatie',
                                                            label='bestrijden ongewenste vegetatie',
                                                            status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                                            definitie='Bestrijden van ongewenste vegetatie die zich bevingt in het perceel van grazige vegetatie..',
                                                            objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlBeheerGrazigeVegetatie/bestrijden-ongewenste-vegetatie'),
        'konijnenbeheer': KeuzelijstWaarde(invulwaarde='konijnenbeheer',
                                           label='konijnenbeheer',
                                           status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                           definitie='Het reduceren van konijnenpopulaties om de stabilietit van taluds te blijven garanderen',
                                           objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlBeheerGrazigeVegetatie/konijnenbeheer'),
        'maaisel-verwijderen-directe-opzuig': KeuzelijstWaarde(invulwaarde='maaisel-verwijderen-directe-opzuig',
                                                               label='maaisel verwijderen directe opzuig',
                                                               status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                                               definitie='het verwijderen van het maaisel met een maaizuigcombinatie',
                                                               objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlBeheerGrazigeVegetatie/maaisel-verwijderen-directe-opzuig'),
        'maaisel-verwijderen-hooien-oprapen': KeuzelijstWaarde(invulwaarde='maaisel-verwijderen-hooien-oprapen',
                                                               label='maaisel verwijderen hooien-oprapen',
                                                               status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                                               definitie='het maaisel wordt gehooid en binnen de 10 dagen opgeraapt en verwijderd',
                                                               objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlBeheerGrazigeVegetatie/maaisel-verwijderen-hooien-oprapen'),
        'niets-doen': KeuzelijstWaarde(invulwaarde='niets-doen',
                                       label='niets doen',
                                       status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                       definitie='Er wordt geen beheer uitgevoerd',
                                       objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlBeheerGrazigeVegetatie/niets-doen'),
        'plaggen': KeuzelijstWaarde(invulwaarde='plaggen',
                                    label='plaggen',
                                    status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                    definitie='Plaggen is het verwijderen van de bovenste grondlaag met begroeiing om grond te verschralen',
                                    objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlBeheerGrazigeVegetatie/plaggen'),
        'profielherstelling-zonder-herinzaaien': KeuzelijstWaarde(invulwaarde='profielherstelling-zonder-herinzaaien',
                                                                  label='profielherstelling zonder herinzaaien',
                                                                  status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                                                  definitie='Profielherstelling zonder herinzaaiing van grazige vegetatie.',
                                                                  objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlBeheerGrazigeVegetatie/profielherstelling-zonder-herinzaaien'),
        'reiten': KeuzelijstWaarde(invulwaarde='reiten',
                                   label='reiten',
                                   status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                   definitie='Het inkorten van het riet tot ongeveer 10 cm boven het wateroppervlak met maaikorf. Maaisel wordt verwijderd.',
                                   objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlBeheerGrazigeVegetatie/reiten'),
        'uitharken': KeuzelijstWaarde(invulwaarde='uitharken',
                                      label='uitharken',
                                      status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                      definitie='Uitharken van grazige vegetatie.',
                                      objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlBeheerGrazigeVegetatie/uitharken')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

