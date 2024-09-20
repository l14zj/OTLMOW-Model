# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlWegbermBIO(KeuzelijstField):
    """Bijzonder ingerichte onderdelen van de wegbermen."""
    naam = 'KlWegbermBIO'
    label = 'Wegberm BIO'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#KlWegbermBIO'
    definition = 'Bijzonder ingerichte onderdelen van de wegbermen.'
    status = 'https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik'
    deprecated_version = '2.11.0'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlWegbermBIO'
    options = {
        'bijzondere-bedding': KeuzelijstWaarde(invulwaarde='bijzondere-bedding',
                                               label='bijzondere bedding',
                                               status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                               definitie='Gedeelte van de wegberm, uitsluitend bestemd voor voertuigen van het openbaar vervoer en andere toegelaten voertuigen.',
                                               objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlWegbermBIO/bijzondere-bedding'),
        'fietspad': KeuzelijstWaarde(invulwaarde='fietspad',
                                     label='fietspad',
                                     status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                     definitie='Gedeelte van het wegplatform, dat bestemd is voor fietsers en bromfietsers en als zodanig aangeduid.',
                                     objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlWegbermBIO/fietspad'),
        'ruiterpad': KeuzelijstWaarde(invulwaarde='ruiterpad',
                                      label='ruiterpad',
                                      status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                      definitie='Gedeelte van de wegberm, bestemd voor ruiters en als zodanig aangeduid.',
                                      objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlWegbermBIO/ruiterpad'),
        'verkeerseiland': KeuzelijstWaarde(invulwaarde='verkeerseiland',
                                           label='verkeerseiland',
                                           status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                           definitie='Heeft als doel het verkeer te geleiden en kan verhoogd zijn.',
                                           objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlWegbermBIO/verkeerseiland'),
        'vluchtheuvel': KeuzelijstWaarde(invulwaarde='vluchtheuvel',
                                         label='vluchtheuvel',
                                         status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                         definitie='Verkeersheuvel ten behoeve van voetgangers.',
                                         objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlWegbermBIO/vluchtheuvel'),
        'voetpad': KeuzelijstWaarde(invulwaarde='voetpad',
                                    label='voetpad',
                                    status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                    definitie='Gedeelte van de wegberm, bestemd voor voetgangers.',
                                    objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlWegbermBIO/voetpad')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

