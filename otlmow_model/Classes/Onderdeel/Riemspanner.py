# coding=utf-8
from otlmow_model.Classes.ImplementatieElement.AIMNaamObject import AIMNaamObject
from otlmow_model.GeometrieTypes.PuntGeometrie import PuntGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class Riemspanner(AIMNaamObject, PuntGeometrie):
    """Een riemspanner bestaat meestal uit een rol en veermechanisme en zorgt er voor dat een riem op de gewenste spanning blijft. Een riemspanner  is samen met een riemschijf en riem onderdeel van een riemoverbrenging."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Riemspanner'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        AIMNaamObject.__init__(self)
        PuntGeometrie.__init__(self)

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Onderstel')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Overbrenging')
