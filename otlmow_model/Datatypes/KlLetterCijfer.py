# coding=utf-8
import random
from otlmow_model.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlLetterCijfer(KeuzelijstField):
    """De mogelijke letters en cijfers voor een letter- of cijfermarkering."""
    naam = 'KlLetterCijfer'
    label = 'Letter-cijfer'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlLetterCijfer'
    definition = 'De mogelijke letters en cijfers voor een letter- of cijfermarkering.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlLetterCijfer'
    options = {
        '-': KeuzelijstWaarde(invulwaarde='-',
                              label='-',
                              status='ingebruik',
                              definitie='Koppelteken.',
                              objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLetterCijfer/-'),
        '0': KeuzelijstWaarde(invulwaarde='0',
                              label='0',
                              status='ingebruik',
                              definitie='Cijfer 0.',
                              objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLetterCijfer/0'),
        '1': KeuzelijstWaarde(invulwaarde='1',
                              label='1',
                              status='ingebruik',
                              definitie='Cijfer 1.',
                              objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLetterCijfer/1'),
        '2': KeuzelijstWaarde(invulwaarde='2',
                              label='2',
                              status='ingebruik',
                              definitie='Cijfer 2.',
                              objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLetterCijfer/2'),
        '3': KeuzelijstWaarde(invulwaarde='3',
                              label='3',
                              status='ingebruik',
                              definitie='Cijfer 3.',
                              objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLetterCijfer/3'),
        '4': KeuzelijstWaarde(invulwaarde='4',
                              label='4',
                              status='ingebruik',
                              definitie='Cijfer 4.',
                              objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLetterCijfer/4'),
        '5': KeuzelijstWaarde(invulwaarde='5',
                              label='5',
                              status='ingebruik',
                              definitie='Cijfer 5.',
                              objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLetterCijfer/5'),
        '6': KeuzelijstWaarde(invulwaarde='6',
                              label='6',
                              status='ingebruik',
                              definitie='Cijfer 6.',
                              objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLetterCijfer/6'),
        '7': KeuzelijstWaarde(invulwaarde='7',
                              label='7',
                              status='ingebruik',
                              definitie='Cijfer 7.',
                              objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLetterCijfer/7'),
        '8': KeuzelijstWaarde(invulwaarde='8',
                              label='8',
                              status='ingebruik',
                              definitie='Cijfer 8.',
                              objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLetterCijfer/8'),
        '9': KeuzelijstWaarde(invulwaarde='9',
                              label='9',
                              status='ingebruik',
                              definitie='Cijfer 9.',
                              objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLetterCijfer/9'),
        'a': KeuzelijstWaarde(invulwaarde='a',
                              label='a',
                              status='ingebruik',
                              definitie='Letter a.',
                              objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLetterCijfer/a'),
        'b': KeuzelijstWaarde(invulwaarde='b',
                              label='b',
                              status='ingebruik',
                              definitie='Letter b.',
                              objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLetterCijfer/b'),
        'c': KeuzelijstWaarde(invulwaarde='c',
                              label='c',
                              status='ingebruik',
                              definitie='Letter c.',
                              objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLetterCijfer/c'),
        'd': KeuzelijstWaarde(invulwaarde='d',
                              label='d',
                              status='ingebruik',
                              definitie='Letter d.',
                              objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLetterCijfer/d'),
        'e': KeuzelijstWaarde(invulwaarde='e',
                              label='e',
                              status='ingebruik',
                              definitie='Letter e.',
                              objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLetterCijfer/e'),
        'f': KeuzelijstWaarde(invulwaarde='f',
                              label='f',
                              status='ingebruik',
                              definitie='Letter f.',
                              objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLetterCijfer/f'),
        'g': KeuzelijstWaarde(invulwaarde='g',
                              label='g',
                              status='ingebruik',
                              definitie='Letter g.',
                              objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLetterCijfer/g'),
        'h': KeuzelijstWaarde(invulwaarde='h',
                              label='h',
                              status='ingebruik',
                              definitie='Letter h.',
                              objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLetterCijfer/h'),
        'i': KeuzelijstWaarde(invulwaarde='i',
                              label='i',
                              status='ingebruik',
                              definitie='Letter i.',
                              objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLetterCijfer/i'),
        'j': KeuzelijstWaarde(invulwaarde='j',
                              label='j',
                              status='ingebruik',
                              definitie='Letter j.',
                              objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLetterCijfer/j'),
        'k': KeuzelijstWaarde(invulwaarde='k',
                              label='k',
                              status='ingebruik',
                              definitie='Letter k.',
                              objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLetterCijfer/k'),
        'l': KeuzelijstWaarde(invulwaarde='l',
                              label='l',
                              status='ingebruik',
                              definitie='Letter l.',
                              objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLetterCijfer/l'),
        'm': KeuzelijstWaarde(invulwaarde='m',
                              label='m',
                              status='ingebruik',
                              definitie='Letter m.',
                              objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLetterCijfer/m'),
        'n': KeuzelijstWaarde(invulwaarde='n',
                              label='n',
                              status='ingebruik',
                              definitie='Letter n.',
                              objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLetterCijfer/n'),
        'o': KeuzelijstWaarde(invulwaarde='o',
                              label='o',
                              status='ingebruik',
                              definitie='Letter o.',
                              objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLetterCijfer/o'),
        'p': KeuzelijstWaarde(invulwaarde='p',
                              label='p',
                              status='ingebruik',
                              definitie='Letter p.',
                              objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLetterCijfer/p'),
        'q': KeuzelijstWaarde(invulwaarde='q',
                              label='q',
                              status='ingebruik',
                              definitie='Letter q.',
                              objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLetterCijfer/q'),
        'r': KeuzelijstWaarde(invulwaarde='r',
                              label='r',
                              status='ingebruik',
                              definitie='Letter r.',
                              objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLetterCijfer/r'),
        's': KeuzelijstWaarde(invulwaarde='s',
                              label='s',
                              status='ingebruik',
                              definitie='Letter s.',
                              objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLetterCijfer/s'),
        't': KeuzelijstWaarde(invulwaarde='t',
                              label='t',
                              status='ingebruik',
                              definitie='Letter t.',
                              objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLetterCijfer/t'),
        'u': KeuzelijstWaarde(invulwaarde='u',
                              label='u',
                              status='ingebruik',
                              definitie='Letter u.',
                              objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLetterCijfer/u'),
        'v': KeuzelijstWaarde(invulwaarde='v',
                              label='v',
                              status='ingebruik',
                              definitie='Letter v.',
                              objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLetterCijfer/v'),
        'w': KeuzelijstWaarde(invulwaarde='w',
                              label='w',
                              status='ingebruik',
                              definitie='Letter w.',
                              objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLetterCijfer/w'),
        'x': KeuzelijstWaarde(invulwaarde='x',
                              label='x',
                              status='ingebruik',
                              definitie='Letter x.',
                              objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLetterCijfer/x'),
        'y': KeuzelijstWaarde(invulwaarde='y',
                              label='y',
                              status='ingebruik',
                              definitie='Letter y.',
                              objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLetterCijfer/y'),
        'z': KeuzelijstWaarde(invulwaarde='z',
                              label='z',
                              status='ingebruik',
                              definitie='Letter z.',
                              objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLetterCijfer/z'),
        'â': KeuzelijstWaarde(invulwaarde='â',
                              label='â',
                              status='ingebruik',
                              definitie='Letter â.',
                              objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLetterCijfer/â'),
        'é': KeuzelijstWaarde(invulwaarde='é',
                              label='é',
                              status='ingebruik',
                              definitie='Letter é.',
                              objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLetterCijfer/é')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

