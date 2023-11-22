# coding=utf-8
from ...Classes.ImplementatieElement.AIMObject import AIMObject
from ...GeometrieTypes.GeenGeometrie import GeenGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class Been(AIMObject, GeenGeometrie):
    """Een aaneengesloten reeks van links die samen een traject realiseren over het netwerk, gebruik makende van eenzelfde technologie (vb SDH, OTN...)."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Been'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Pad')
