# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlBestratingAfwerking(KeuzelijstField):
    """De manieren van afwerking van de bestrating."""
    naam = 'KlBestratingAfwerking'
    label = 'Bestrating afwerking'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlBestratingAfwerking'
    definition = 'De manieren van afwerking van de bestrating.'
    status = 'https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlBestratingAfwerking'
    options = {
        'afwerking-volgens-de-opdrachtdocumenten': KeuzelijstWaarde(invulwaarde='afwerking-volgens-de-opdrachtdocumenten',
                                                                    label='afwerking volgens de opdrachtdocumenten',
                                                                    status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                                                    definitie='afwerking volgens de opdrachtdocumenten',
                                                                    objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlBestratingAfwerking/afwerking-volgens-de-opdrachtdocumenten'),
        'gebouchardeerd': KeuzelijstWaarde(invulwaarde='gebouchardeerd',
                                           label='gebouchardeerd',
                                           status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                           definitie='gebouchardeerd',
                                           objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlBestratingAfwerking/gebouchardeerd'),
        'gefrijnd': KeuzelijstWaarde(invulwaarde='gefrijnd',
                                     label='gefrijnd',
                                     status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                     definitie='gefrijnd',
                                     objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlBestratingAfwerking/gefrijnd'),
        'gehamerd': KeuzelijstWaarde(invulwaarde='gehamerd',
                                     label='gehamerd',
                                     status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                     definitie='gehamerd',
                                     objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlBestratingAfwerking/gehamerd'),
        'gekliefd': KeuzelijstWaarde(invulwaarde='gekliefd',
                                     label='gekliefd',
                                     status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                     definitie='gekliefd',
                                     objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlBestratingAfwerking/gekliefd'),
        'geschuurd': KeuzelijstWaarde(invulwaarde='geschuurd',
                                      label='geschuurd',
                                      status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                      definitie='geschuurd',
                                      objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlBestratingAfwerking/geschuurd'),
        'geslepen': KeuzelijstWaarde(invulwaarde='geslepen',
                                     label='geslepen',
                                     status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                     definitie='geslepen',
                                     objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlBestratingAfwerking/geslepen'),
        'geslepen-en-gestraald': KeuzelijstWaarde(invulwaarde='geslepen-en-gestraald',
                                                  label='geslepen en gestraald',
                                                  status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                                  definitie='geslepen en gestraald',
                                                  objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlBestratingAfwerking/geslepen-en-gestraald'),
        'gestaaldstraald': KeuzelijstWaarde(invulwaarde='gestaaldstraald',
                                            label='gestaaldstraald',
                                            status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                            definitie='gestaaldstraald',
                                            objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlBestratingAfwerking/gestaaldstraald'),
        'getrommeld': KeuzelijstWaarde(invulwaarde='getrommeld',
                                       label='getrommeld',
                                       status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                       definitie='getrommeld',
                                       objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlBestratingAfwerking/getrommeld'),
        'gevlamd': KeuzelijstWaarde(invulwaarde='gevlamd',
                                    label='gevlamd',
                                    status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                    definitie='gevlamd',
                                    objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlBestratingAfwerking/gevlamd'),
        'gewassen': KeuzelijstWaarde(invulwaarde='gewassen',
                                     label='gewassen',
                                     status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                     definitie='gewassen',
                                     objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlBestratingAfwerking/gewassen'),
        'gezaagd': KeuzelijstWaarde(invulwaarde='gezaagd',
                                    label='gezaagd',
                                    status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                    definitie='gezaagd',
                                    objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlBestratingAfwerking/gezaagd'),
        'gezandstraald': KeuzelijstWaarde(invulwaarde='gezandstraald',
                                          label='gezandstraald',
                                          status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                          definitie='gezandstraald',
                                          objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlBestratingAfwerking/gezandstraald'),
        'onbehandeld': KeuzelijstWaarde(invulwaarde='onbehandeld',
                                        label='onbehandeld',
                                        status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                        definitie='onbehandeld',
                                        objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlBestratingAfwerking/onbehandeld'),
        'poreus': KeuzelijstWaarde(invulwaarde='poreus',
                                   label='poreus',
                                   status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                   definitie='poreus',
                                   objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlBestratingAfwerking/poreus')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

