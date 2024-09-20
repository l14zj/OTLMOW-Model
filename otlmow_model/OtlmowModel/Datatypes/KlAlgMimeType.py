# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlAlgMimeType(KeuzelijstField):
    """De mime types van bestanden (AWVDocument) beperkt tot mime types voor toegelaten bestandstypen."""
    naam = 'KlAlgMimeType'
    label = 'Mimetype'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#KlAlgMimeType'
    definition = 'De mime types van bestanden (AWVDocument) beperkt tot mime types voor toegelaten bestandstypen.'
    status = 'https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlAlgMimeType'
    options = {
        'application-acad': KeuzelijstWaarde(invulwaarde='application-acad',
                                             label='application/acad',
                                             status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                             objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAlgMimeType/application-acad'),
        'application-acadmap': KeuzelijstWaarde(invulwaarde='application-acadmap',
                                                label='application/acadmap',
                                                status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                                objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAlgMimeType/application-acadmap'),
        'application-json': KeuzelijstWaarde(invulwaarde='application-json',
                                             label='application/json',
                                             status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                             definitie='application/json',
                                             objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAlgMimeType/application-json'),
        'application-pdf': KeuzelijstWaarde(invulwaarde='application-pdf',
                                            label='application/pdf',
                                            status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                            objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAlgMimeType/application-pdf'),
        'application-rtf': KeuzelijstWaarde(invulwaarde='application-rtf',
                                            label='application/rtf',
                                            status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                            objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAlgMimeType/application-rtf'),
        'application-rvt': KeuzelijstWaarde(invulwaarde='application-rvt',
                                            label='application/rvt',
                                            status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                            definitie='Revit project file.',
                                            objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAlgMimeType/application-rvt'),
        'application-vnd.openxmlformats-officedocument.spreadsheetml.sheet': KeuzelijstWaarde(invulwaarde='application-vnd.openxmlformats-officedocument.spreadsheetml.sheet',
                                                                                              label='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet',
                                                                                              status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                                                                              objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAlgMimeType/application-vnd.openxmlformats-officedocument.spreadsheetml.sheet'),
        'application-vnd.openxmlformats-officedocument.wordprocessingml.document': KeuzelijstWaarde(invulwaarde='application-vnd.openxmlformats-officedocument.wordprocessingml.document',
                                                                                                    label='application/vnd.openxmlformats-officedocument.wordprocessingml.document',
                                                                                                    status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                                                                                    objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAlgMimeType/application-vnd.openxmlformats-officedocument.wordprocessingml.document'),
        'application-xml': KeuzelijstWaarde(invulwaarde='application-xml',
                                            label='application/xml',
                                            status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                            objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAlgMimeType/application-xml'),
        'application-zip': KeuzelijstWaarde(invulwaarde='application-zip',
                                            label='application/zip',
                                            status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                            objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAlgMimeType/application-zip'),
        'image-dxf': KeuzelijstWaarde(invulwaarde='image-dxf',
                                      label='image/dxf',
                                      status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                      objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAlgMimeType/image-dxf'),
        'image-jpeg': KeuzelijstWaarde(invulwaarde='image-jpeg',
                                       label='image/jpeg',
                                       status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                       objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAlgMimeType/image-jpeg'),
        'image-png': KeuzelijstWaarde(invulwaarde='image-png',
                                      label='image/png',
                                      status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                      definitie='image-png',
                                      objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAlgMimeType/image-png'),
        'image-svg': KeuzelijstWaarde(invulwaarde='image-svg',
                                      label='image/svg',
                                      status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                      objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAlgMimeType/image-svg'),
        'image-tiff': KeuzelijstWaarde(invulwaarde='image-tiff',
                                       label='image/tiff',
                                       status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                       objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAlgMimeType/image-tiff'),
        'text-cfg': KeuzelijstWaarde(invulwaarde='text-cfg',
                                     label='text/cfg',
                                     status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                     definitie='text-cfg',
                                     objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAlgMimeType/text-cfg'),
        'text-csv': KeuzelijstWaarde(invulwaarde='text-csv',
                                     label='text/csv',
                                     status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                     objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAlgMimeType/text-csv'),
        'text-html': KeuzelijstWaarde(invulwaarde='text-html',
                                      label='text/html',
                                      status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                      objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAlgMimeType/text-html'),
        'text-plain': KeuzelijstWaarde(invulwaarde='text-plain',
                                       label='text/plain',
                                       status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                       definitie='text/plain',
                                       objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAlgMimeType/text-plain'),
        'text-rtf': KeuzelijstWaarde(invulwaarde='text-rtf',
                                     label='text/rtf',
                                     status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                     objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAlgMimeType/text-rtf'),
        'text-xml': KeuzelijstWaarde(invulwaarde='text-xml',
                                     label='text/xml',
                                     status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                     objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAlgMimeType/text-xml'),
        'video-avi': KeuzelijstWaarde(invulwaarde='video-avi',
                                      label='video/avi',
                                      status='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                      objectUri='https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAlgMimeType/video-avi')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

