# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlKabelmantelKleur(KeuzelijstField):
    """Lijst van mogelijke kleuren voor de kabelmantel."""
    naam = 'KlKabelmantelKleur'
    label = 'Kabelmantel kleur'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#KlKabelmantelKleur'
    definition = 'Lijst van mogelijke kleuren voor de kabelmantel.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlKabelmantelKleur'
    options = {
        '14': KeuzelijstWaarde(invulwaarde='14',
                               label='14',
                               status='ingebruik',
                               definitie='14',
                               objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlKabelmantelKleur/14'),
        'blank-koper': KeuzelijstWaarde(invulwaarde='blank-koper',
                                        label='blank-koper',
                                        status='ingebruik',
                                        definitie='blank-koper',
                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlKabelmantelKleur/blank-koper'),
        'blauw': KeuzelijstWaarde(invulwaarde='blauw',
                                  label='blauw',
                                  status='ingebruik',
                                  definitie='blauw',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlKabelmantelKleur/blauw'),
        'ekm': KeuzelijstWaarde(invulwaarde='ekm',
                                label='ekm',
                                status='ingebruik',
                                definitie='ekm',
                                objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlKabelmantelKleur/ekm'),
        'fiber': KeuzelijstWaarde(invulwaarde='fiber',
                                  label='fiber',
                                  status='ingebruik',
                                  definitie='fiber',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlKabelmantelKleur/fiber'),
        'geel': KeuzelijstWaarde(invulwaarde='geel',
                                 label='geel',
                                 status='ingebruik',
                                 definitie='geel',
                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlKabelmantelKleur/geel'),
        'geel-grijs': KeuzelijstWaarde(invulwaarde='geel-grijs',
                                       label='geel-grijs',
                                       status='ingebruik',
                                       definitie='geel-grijs',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlKabelmantelKleur/geel-grijs'),
        'geel-groen': KeuzelijstWaarde(invulwaarde='geel-groen',
                                       label='geel-groen',
                                       status='ingebruik',
                                       definitie='geel-groen',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlKabelmantelKleur/geel-groen'),
        'geel-groen-zwart': KeuzelijstWaarde(invulwaarde='geel-groen-zwart',
                                             label='geel-groen-zwart',
                                             status='ingebruik',
                                             definitie='geel-groen-zwart',
                                             objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlKabelmantelKleur/geel-groen-zwart'),
        'geel-of-zwart': KeuzelijstWaarde(invulwaarde='geel-of-zwart',
                                          label='geel of zwart',
                                          status='ingebruik',
                                          definitie='geel of zwart',
                                          objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlKabelmantelKleur/geel-of-zwart'),
        'geel-zwart': KeuzelijstWaarde(invulwaarde='geel-zwart',
                                       label='geel-zwart',
                                       status='ingebruik',
                                       definitie='geel-zwart',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlKabelmantelKleur/geel-zwart'),
        'glasvezel': KeuzelijstWaarde(invulwaarde='glasvezel',
                                      label='glasvezel',
                                      status='ingebruik',
                                      definitie='glasvezel',
                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlKabelmantelKleur/glasvezel'),
        'grijs': KeuzelijstWaarde(invulwaarde='grijs',
                                  label='grijs',
                                  status='ingebruik',
                                  definitie='grijs',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlKabelmantelKleur/grijs'),
        'grijs-blauw': KeuzelijstWaarde(invulwaarde='grijs-blauw',
                                        label='grijs-blauw',
                                        status='ingebruik',
                                        definitie='grijs-blauw',
                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlKabelmantelKleur/grijs-blauw'),
        'groen': KeuzelijstWaarde(invulwaarde='groen',
                                  label='groen',
                                  status='ingebruik',
                                  definitie='groen',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlKabelmantelKleur/groen'),
        'groen-met-4-zwarte-strepen': KeuzelijstWaarde(invulwaarde='groen-met-4-zwarte-strepen',
                                                       label='groen met 4 zwarte strepen',
                                                       status='ingebruik',
                                                       definitie='groen met 4 zwarte strepen',
                                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlKabelmantelKleur/groen-met-4-zwarte-strepen'),
        'groen-zwart': KeuzelijstWaarde(invulwaarde='groen-zwart',
                                        label='groen-zwart',
                                        status='ingebruik',
                                        definitie='groen-zwart',
                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlKabelmantelKleur/groen-zwart'),
        'onbekend': KeuzelijstWaarde(invulwaarde='onbekend',
                                     label='onbekend',
                                     status='ingebruik',
                                     definitie='onbekend',
                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlKabelmantelKleur/onbekend'),
        'oranje': KeuzelijstWaarde(invulwaarde='oranje',
                                   label='oranje',
                                   status='ingebruik',
                                   definitie='oranje',
                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlKabelmantelKleur/oranje'),
        'rood': KeuzelijstWaarde(invulwaarde='rood',
                                 label='rood',
                                 status='ingebruik',
                                 definitie='rood',
                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlKabelmantelKleur/rood'),
        'rood-wit': KeuzelijstWaarde(invulwaarde='rood-wit',
                                     label='rood-wit',
                                     status='ingebruik',
                                     definitie='rood-wit',
                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlKabelmantelKleur/rood-wit'),
        'rood-zwart': KeuzelijstWaarde(invulwaarde='rood-zwart',
                                       label='rood-zwart',
                                       status='ingebruik',
                                       definitie='rood-zwart',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlKabelmantelKleur/rood-zwart'),
        'transparant': KeuzelijstWaarde(invulwaarde='transparant',
                                        label='transparant',
                                        status='ingebruik',
                                        definitie='transparant',
                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlKabelmantelKleur/transparant'),
        'yp': KeuzelijstWaarde(invulwaarde='yp',
                               label='yp',
                               status='ingebruik',
                               definitie='yp',
                               objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlKabelmantelKleur/yp'),
        'zwart': KeuzelijstWaarde(invulwaarde='zwart',
                                  label='zwart',
                                  status='ingebruik',
                                  definitie='zwart',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlKabelmantelKleur/zwart'),
        'zwart-rood': KeuzelijstWaarde(invulwaarde='zwart-rood',
                                       label='zwart-rood',
                                       status='ingebruik',
                                       definitie='zwart-rood',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlKabelmantelKleur/zwart-rood')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

