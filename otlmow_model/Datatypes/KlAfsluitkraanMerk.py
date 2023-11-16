# coding=utf-8
import random
from otlmow_model.BaseClasses.KeuzelijstField import KeuzelijstField


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlAfsluitkraanMerk(KeuzelijstField):
    """Lijst met merknamen van afsluitkranen volgens de fabrikant"""
    naam = 'KlAfsluitkraanMerk'
    label = 'Merk aflsuitkraan'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlAfsluitkraanMerk'
    definition = 'Lijst met merknamen van afsluitkranen volgens de fabrikant'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlAfsluitkraanMerk'
    options = {
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

