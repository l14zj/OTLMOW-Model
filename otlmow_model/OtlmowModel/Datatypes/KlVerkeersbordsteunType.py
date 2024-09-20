# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlVerkeersbordsteunType(KeuzelijstField):
    """Types voor een verkeersbordsteun."""
    naam = 'KlVerkeersbordsteunType'
    label = 'Verkeersbordsteuntype'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlVerkeersbordsteunType'
    definition = 'Types voor een verkeersbordsteun.'
    status = 'https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlVerkeersbordsteunType'
    options = {
        'botsvriendelijke-steun': KeuzelijstWaarde(invulwaarde='botsvriendelijke-steun',
                                                   label='botsvriendelijke steun',
                                                   status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                                   definitie='Constructie die na aanrijding zijn oorspronkelijke positie hersteld',
                                                   objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlVerkeersbordsteunType/botsvriendelijke-steun'),
        'botsvriendelijke-steun-type-100NE2': KeuzelijstWaarde(invulwaarde='botsvriendelijke-steun-type-100NE2',
                                                               label='botsvriendelijke steun type 100NE2',
                                                               status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                                               objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlVerkeersbordsteunType/botsvriendelijke-steun-type-100NE2'),
        'botsvriendelijke-steun-type-100NE3': KeuzelijstWaarde(invulwaarde='botsvriendelijke-steun-type-100NE3',
                                                               label='botsvriendelijke steun type 100NE3',
                                                               status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                                               objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlVerkeersbordsteunType/botsvriendelijke-steun-type-100NE3'),
        'galgpaal': KeuzelijstWaarde(invulwaarde='galgpaal',
                                     label='galgpaal',
                                     status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                     definitie='Een keuzelijst om het type verkeersbordpaal te bepalen',
                                     objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlVerkeersbordsteunType/galgpaal'),
        'rechte-paal': KeuzelijstWaarde(invulwaarde='rechte-paal',
                                        label='rechte paal',
                                        status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                        definitie='Een rechte paal met als doel een verkeersbord te bevestigen',
                                        objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlVerkeersbordsteunType/rechte-paal'),
        'seinbrug': KeuzelijstWaarde(invulwaarde='seinbrug',
                                     label='seinbrug',
                                     status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                     definitie='Metalen constructie bestaande uit 2 of meer verticale steunen met voetplaat en uit een enkele of een dubbel uitgevoerde horizontale dwarsverbinding, allen kokervormig met rechthoekige doorsnede. Ook wel portiek of portaal genoemd',
                                     objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlVerkeersbordsteunType/seinbrug'),
        'vakwerksteun': KeuzelijstWaarde(invulwaarde='vakwerksteun',
                                         label='vakwerksteun',
                                         status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                         definitie='Een keuzelijst om het type verkeersbordpaal te bepalen',
                                         objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlVerkeersbordsteunType/vakwerksteun')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

