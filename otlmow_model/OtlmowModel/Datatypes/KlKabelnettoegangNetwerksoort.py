# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlKabelnettoegangNetwerksoort(KeuzelijstField):
    """Lijst van netwerktypes die bereikbaar is via het kabelnet toegangspunt."""
    naam = 'KlKabelnettoegangNetwerksoort'
    label = 'Kabelnet toegang netwerksoort'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlKabelnettoegangNetwerksoort'
    definition = 'Lijst van netwerktypes die bereikbaar is via het kabelnet toegangspunt.'
    status = 'https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlKabelnettoegangNetwerksoort'
    options = {
        'Cu': KeuzelijstWaarde(invulwaarde='Cu',
                               label='Cu',
                               status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                               objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlKabelnettoegangNetwerksoort/Cu'),
        'FO': KeuzelijstWaarde(invulwaarde='FO',
                               label='FO',
                               status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                               objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlKabelnettoegangNetwerksoort/FO'),
        'beide': KeuzelijstWaarde(invulwaarde='beide',
                                  label='beide',
                                  status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                  definitie='beide',
                                  objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlKabelnettoegangNetwerksoort/beide'),
        'geen': KeuzelijstWaarde(invulwaarde='geen',
                                 label='geen',
                                 status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                 definitie='geen',
                                 objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlKabelnettoegangNetwerksoort/geen'),
        'glasvezel': KeuzelijstWaarde(invulwaarde='glasvezel',
                                      label='glasvezel',
                                      status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                      definitie='glasvezel',
                                      objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlKabelnettoegangNetwerksoort/glasvezel'),
        'koper': KeuzelijstWaarde(invulwaarde='koper',
                                  label='koper',
                                  status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                  definitie='koper',
                                  objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlKabelnettoegangNetwerksoort/koper')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

