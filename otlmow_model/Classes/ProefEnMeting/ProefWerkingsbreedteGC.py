# coding=utf-8
from otlmow_model.Classes.Abstracten.Proef import Proef
from otlmow_model.GeometrieArtefact.PuntGeometrie import PuntGeometrie
from otlmow_model.GeometrieArtefact.LijnGeometrie import LijnGeometrie
from otlmow_model.GeometrieArtefact.VlakGeometrie import VlakGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class ProefWerkingsbreedteGC(Proef, PuntGeometrie, LijnGeometrie, VlakGeometrie):
    """Proef om de afstand te bepalen tussen de voorkant van de geleideconstructie in normale positie en de plaats van het verst uitwijkend onderdeel aan de achterzijde van de geleideconstructie bij aanrijding. (gemeten op het voorvlak van een geleideconstructie en loodrecht op de as van de weg)"""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/proefenmeting#ProefWerkingsbreedteGC'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    deprecated_version = '2.0.0'

    def __init__(self):
        Proef.__init__(self)
        LijnGeometrie.__init__(self)
        PuntGeometrie.__init__(self)
        VlakGeometrie.__init__(self)

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#IsInspectieVan', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Geleideconstructie', deprecated='2.0.0')
