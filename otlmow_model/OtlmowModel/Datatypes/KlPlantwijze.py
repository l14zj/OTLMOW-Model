# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlPlantwijze(KeuzelijstField):
    """De mogelijke (aanplant)plantmanieren."""
    naam = 'KlPlantwijze'
    label = 'Plantwijze'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#KlPlantwijze'
    definition = 'De mogelijke (aanplant)plantmanieren.'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlPlantwijze'
    options = {
        'in-bospark': KeuzelijstWaarde(invulwaarde='in-bospark',
                                       label='in bospark',
                                       status='ingebruik',
                                       definitie='in bospark',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlPlantwijze/in-bospark'),
        'in-groep-2-5-stuks': KeuzelijstWaarde(invulwaarde='in-groep-2-5-stuks',
                                               label='in groep (2-5 stuks)',
                                               status='ingebruik',
                                               definitie='in groep (2-5 stuks)',
                                               objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlPlantwijze/in-groep-2-5-stuks'),
        'in-grotere-groepen': KeuzelijstWaarde(invulwaarde='in-grotere-groepen',
                                               label='in grotere groepen',
                                               status='ingebruik',
                                               definitie='in grotere groepen',
                                               objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlPlantwijze/in-grotere-groepen'),
        'in-rijbeplanting': KeuzelijstWaarde(invulwaarde='in-rijbeplanting',
                                             label='in rijbeplanting',
                                             status='ingebruik',
                                             definitie='in rijbeplanting',
                                             objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlPlantwijze/in-rijbeplanting'),
        'solitair': KeuzelijstWaarde(invulwaarde='solitair',
                                     label='solitair',
                                     status='ingebruik',
                                     definitie='solitair',
                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlPlantwijze/solitair')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

