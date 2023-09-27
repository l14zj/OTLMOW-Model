# coding=utf-8
import random
from otlmow_model.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlVerlichtingstoestelModelnaam(KeuzelijstField):
    """De modelnaam van het verlichtingstoestel."""
    naam = 'KlVerlichtingstoestelModelnaam'
    label = 'Verlichtingstoestel modelnaam'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#KlVerlichtingstoestelModelnaam'
    definition = 'De modelnaam van het verlichtingstoestel.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlVerlichtingstoestelModelnaam'
    options = {
        'ARC': KeuzelijstWaarde(invulwaarde='ARC',
                                label='ARC',
                                status='ingebruik',
                                definitie='ARC',
                                objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVerlichtingstoestelModelnaam/ARC'),
        'Belgica': KeuzelijstWaarde(invulwaarde='Belgica',
                                    label='Belgica',
                                    status='ingebruik',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVerlichtingstoestelModelnaam/Belgica'),
        'Calypso': KeuzelijstWaarde(invulwaarde='Calypso',
                                    label='Calypso',
                                    status='ingebruik',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVerlichtingstoestelModelnaam/Calypso'),
        'Corus': KeuzelijstWaarde(invulwaarde='Corus',
                                  label='Corus',
                                  status='ingebruik',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVerlichtingstoestelModelnaam/Corus'),
        'DTN': KeuzelijstWaarde(invulwaarde='DTN',
                                label='DTN',
                                status='ingebruik',
                                objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVerlichtingstoestelModelnaam/DTN'),
        'Evolo': KeuzelijstWaarde(invulwaarde='Evolo',
                                  label='Evolo',
                                  status='ingebruik',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVerlichtingstoestelModelnaam/Evolo'),
        'Focal': KeuzelijstWaarde(invulwaarde='Focal',
                                  label='Focal',
                                  status='ingebruik',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVerlichtingstoestelModelnaam/Focal'),
        'GSM': KeuzelijstWaarde(invulwaarde='GSM',
                                label='GSM',
                                status='ingebruik',
                                objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVerlichtingstoestelModelnaam/GSM'),
        'GTMB': KeuzelijstWaarde(invulwaarde='GTMB',
                                 label='GTMB',
                                 status='ingebruik',
                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVerlichtingstoestelModelnaam/GTMB'),
        'GTNB': KeuzelijstWaarde(invulwaarde='GTNB',
                                 label='GTNB',
                                 status='ingebruik',
                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVerlichtingstoestelModelnaam/GTNB'),
        'GZM': KeuzelijstWaarde(invulwaarde='GZM',
                                label='GZM',
                                status='ingebruik',
                                objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVerlichtingstoestelModelnaam/GZM'),
        'Gema': KeuzelijstWaarde(invulwaarde='Gema',
                                 label='Gema',
                                 status='ingebruik',
                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVerlichtingstoestelModelnaam/Gema'),
        'HCI-TS': KeuzelijstWaarde(invulwaarde='HCI-TS',
                                   label='HCI-TS',
                                   status='ingebruik',
                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVerlichtingstoestelModelnaam/HCI-TS'),
        'Iridium': KeuzelijstWaarde(invulwaarde='Iridium',
                                    label='Iridium',
                                    status='ingebruik',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVerlichtingstoestelModelnaam/Iridium'),
        'MNF300': KeuzelijstWaarde(invulwaarde='MNF300',
                                   label='MNF300',
                                   status='ingebruik',
                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVerlichtingstoestelModelnaam/MNF300'),
        'MWF230': KeuzelijstWaarde(invulwaarde='MWF230',
                                   label='MWF230',
                                   status='ingebruik',
                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVerlichtingstoestelModelnaam/MWF230'),
        'MY11': KeuzelijstWaarde(invulwaarde='MY11',
                                 label='MY11',
                                 status='ingebruik',
                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVerlichtingstoestelModelnaam/MY11'),
        'Neos': KeuzelijstWaarde(invulwaarde='Neos',
                                 label='Neos',
                                 status='ingebruik',
                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVerlichtingstoestelModelnaam/Neos'),
        'Onyx': KeuzelijstWaarde(invulwaarde='Onyx',
                                 label='Onyx',
                                 status='ingebruik',
                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVerlichtingstoestelModelnaam/Onyx'),
        'RT3NB': KeuzelijstWaarde(invulwaarde='RT3NB',
                                  label='RT3NB',
                                  status='ingebruik',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVerlichtingstoestelModelnaam/RT3NB'),
        'RT3SB': KeuzelijstWaarde(invulwaarde='RT3SB',
                                  label='RT3SB',
                                  status='ingebruik',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVerlichtingstoestelModelnaam/RT3SB'),
        'RXN': KeuzelijstWaarde(invulwaarde='RXN',
                                label='RXN',
                                status='ingebruik',
                                objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVerlichtingstoestelModelnaam/RXN'),
        'RXS': KeuzelijstWaarde(invulwaarde='RXS',
                                label='RXS',
                                status='ingebruik',
                                objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVerlichtingstoestelModelnaam/RXS'),
        'Radial': KeuzelijstWaarde(invulwaarde='Radial',
                                   label='Radial',
                                   status='ingebruik',
                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVerlichtingstoestelModelnaam/Radial'),
        'SRS201': KeuzelijstWaarde(invulwaarde='SRS201',
                                   label='SRS201',
                                   status='ingebruik',
                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVerlichtingstoestelModelnaam/SRS201'),
        'Safir': KeuzelijstWaarde(invulwaarde='Safir',
                                  label='Safir',
                                  status='ingebruik',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVerlichtingstoestelModelnaam/Safir'),
        'Saturnus': KeuzelijstWaarde(invulwaarde='Saturnus',
                                     label='Saturnus',
                                     status='ingebruik',
                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVerlichtingstoestelModelnaam/Saturnus'),
        'Squalo': KeuzelijstWaarde(invulwaarde='Squalo',
                                   label='Squalo',
                                   status='ingebruik',
                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVerlichtingstoestelModelnaam/Squalo'),
        'Syntra': KeuzelijstWaarde(invulwaarde='Syntra',
                                   label='Syntra',
                                   status='ingebruik',
                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVerlichtingstoestelModelnaam/Syntra'),
        'VTP': KeuzelijstWaarde(invulwaarde='VTP',
                                label='VTP',
                                status='ingebruik',
                                objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVerlichtingstoestelModelnaam/VTP'),
        'Z18': KeuzelijstWaarde(invulwaarde='Z18',
                                label='Z18',
                                status='ingebruik',
                                objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVerlichtingstoestelModelnaam/Z18'),
        'Z2': KeuzelijstWaarde(invulwaarde='Z2',
                               label='Z2',
                               status='ingebruik',
                               objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVerlichtingstoestelModelnaam/Z2'),
        'Z21': KeuzelijstWaarde(invulwaarde='Z21',
                                label='Z21',
                                status='ingebruik',
                                objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVerlichtingstoestelModelnaam/Z21'),
        'ampera': KeuzelijstWaarde(invulwaarde='ampera',
                                   label='Ampera',
                                   status='ingebruik',
                                   definitie='Ampera',
                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVerlichtingstoestelModelnaam/ampera'),
        'andere': KeuzelijstWaarde(invulwaarde='andere',
                                   label='andere',
                                   status='ingebruik',
                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVerlichtingstoestelModelnaam/andere'),
        'brugleuning': KeuzelijstWaarde(invulwaarde='brugleuning',
                                        label='brugleuning',
                                        status='ingebruik',
                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVerlichtingstoestelModelnaam/brugleuning'),
        'clear-field': KeuzelijstWaarde(invulwaarde='clear-field',
                                        label='ClearField',
                                        status='ingebruik',
                                        definitie='ClearField',
                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVerlichtingstoestelModelnaam/clear-field'),
        'digi-street': KeuzelijstWaarde(invulwaarde='digi-street',
                                        label='DigiStreet',
                                        status='ingebruik',
                                        definitie='DigiStreet',
                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVerlichtingstoestelModelnaam/digi-street'),
        'izylum': KeuzelijstWaarde(invulwaarde='izylum',
                                   label='Izylum',
                                   status='ingebruik',
                                   definitie='Izylum',
                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVerlichtingstoestelModelnaam/izylum'),
        'izylum-1': KeuzelijstWaarde(invulwaarde='izylum-1',
                                     label='Izylum-1',
                                     status='ingebruik',
                                     definitie='Izylum-1',
                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVerlichtingstoestelModelnaam/izylum-1'),
        'izylum-2': KeuzelijstWaarde(invulwaarde='izylum-2',
                                     label='Izylum-2',
                                     status='ingebruik',
                                     definitie='Izylum-2',
                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVerlichtingstoestelModelnaam/izylum-2'),
        'izylum-3': KeuzelijstWaarde(invulwaarde='izylum-3',
                                     label='Izylum-3',
                                     status='ingebruik',
                                     definitie='Izylum-3',
                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVerlichtingstoestelModelnaam/izylum-3'),
        'izylum-4': KeuzelijstWaarde(invulwaarde='izylum-4',
                                     label='Izylum-4',
                                     status='ingebruik',
                                     definitie='Izylum-4',
                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVerlichtingstoestelModelnaam/izylum-4'),
        'izylum-5': KeuzelijstWaarde(invulwaarde='izylum-5',
                                     label='Izylum-5',
                                     status='ingebruik',
                                     definitie='Izylum-5',
                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVerlichtingstoestelModelnaam/izylum-5'),
        'luma': KeuzelijstWaarde(invulwaarde='luma',
                                 label='Luma',
                                 status='ingebruik',
                                 definitie='Luma',
                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVerlichtingstoestelModelnaam/luma'),
        'lumi-street': KeuzelijstWaarde(invulwaarde='lumi-street',
                                        label='LumiStreet',
                                        status='ingebruik',
                                        definitie='LumiStreet',
                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVerlichtingstoestelModelnaam/lumi-street'),
        'lumistreet-gen2-large': KeuzelijstWaarde(invulwaarde='lumistreet-gen2-large',
                                                  label='LumiStreet Gen2 Large',
                                                  status='ingebruik',
                                                  definitie='LumiStreet Gen2 Large',
                                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVerlichtingstoestelModelnaam/lumistreet-gen2-large'),
        'lumistreet-gen2-medium': KeuzelijstWaarde(invulwaarde='lumistreet-gen2-medium',
                                                   label='LumiStreet Gen2 Medium',
                                                   status='ingebruik',
                                                   definitie='LumiStreet Gen2 Medium',
                                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVerlichtingstoestelModelnaam/lumistreet-gen2-medium'),
        'lumistreet-gen2-micro': KeuzelijstWaarde(invulwaarde='lumistreet-gen2-micro',
                                                  label='LumiStreet Gen2 Micro',
                                                  status='ingebruik',
                                                  definitie='LumiStreet Gen2 Micro',
                                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVerlichtingstoestelModelnaam/lumistreet-gen2-micro'),
        'lumistreet-gen2-mini': KeuzelijstWaarde(invulwaarde='lumistreet-gen2-mini',
                                                 label='LumiStreet Gen2 Mini',
                                                 status='ingebruik',
                                                 definitie='LumiStreet Gen2 Mini',
                                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVerlichtingstoestelModelnaam/lumistreet-gen2-mini'),
        'luxis': KeuzelijstWaarde(invulwaarde='luxis',
                                  label='Luxis',
                                  status='ingebruik',
                                  definitie='Luxis',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVerlichtingstoestelModelnaam/luxis'),
        'projector': KeuzelijstWaarde(invulwaarde='projector',
                                      label='projector',
                                      status='ingebruik',
                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVerlichtingstoestelModelnaam/projector'),
        'rombalux': KeuzelijstWaarde(invulwaarde='rombalux',
                                     label='Rombalux',
                                     status='ingebruik',
                                     definitie='Rombalux',
                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVerlichtingstoestelModelnaam/rombalux'),
        'teceo': KeuzelijstWaarde(invulwaarde='teceo',
                                  label='Teceo',
                                  status='ingebruik',
                                  definitie='Teceo',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVerlichtingstoestelModelnaam/teceo'),
        'tflex-line': KeuzelijstWaarde(invulwaarde='tflex-line',
                                       label='TFLEX LINE',
                                       status='ingebruik',
                                       definitie='TFLEX LINE',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVerlichtingstoestelModelnaam/tflex-line'),
        'tflex-module': KeuzelijstWaarde(invulwaarde='tflex-module',
                                         label='TFLEX Module',
                                         status='ingebruik',
                                         definitie='TFLEX Module',
                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVerlichtingstoestelModelnaam/tflex-module')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

