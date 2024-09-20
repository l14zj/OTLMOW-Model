# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlToegangspoortMerk(KeuzelijstField):
    """Lijst met merknamen voor allerlei types van toegangspoorten volgens de fabrikant"""
    naam = 'KlToegangspoortMerk'
    label = 'Toegangspoort merk'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlToegangspoortMerk'
    definition = 'Lijst met merknamen voor allerlei types van toegangspoorten volgens de fabrikant'
    status = 'https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlToegangspoortMerk'
    options = {
        'bm-technics': KeuzelijstWaarde(invulwaarde='bm-technics',
                                        label='BM Technics',
                                        status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                        objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlToegangspoortMerk/bm-technics'),
        'hormann': KeuzelijstWaarde(invulwaarde='hormann',
                                    label='Hormann',
                                    status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                    definitie='HÃƒÂ¶rmann',
                                    objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlToegangspoortMerk/hormann')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

