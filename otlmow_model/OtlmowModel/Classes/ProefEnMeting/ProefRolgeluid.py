# coding=utf-8
from ...BaseClasses.OTLObject import OTLAttribuut
from ...Classes.Abstracten.Proef import Proef
from ...Datatypes.DtcDocument import DtcDocument, DtcDocumentWaarden
from ...GeometrieTypes.PuntGeometrie import PuntGeometrie
from ...GeometrieTypes.LijnGeometrie import LijnGeometrie
from ...GeometrieTypes.VlakGeometrie import VlakGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class ProefRolgeluid(Proef, PuntGeometrie, LijnGeometrie, VlakGeometrie):
    """Het rolgeluid wordt gemeten met de CPX-methode volgens ISO/CEN 11819-2."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/proefenmeting#ProefRolgeluid'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#IsInspectieVan', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#BitumineuzeLaag')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#IsInspectieVan', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Cementbetonverharding')

        self._rolgeluid = OTLAttribuut(field=DtcDocument,
                                       naam='rolgeluid',
                                       label='rolgeluid',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/proefenmeting#ProefRolgeluid.rolgeluid',
                                       definition='Proefresultaten van het rolgeluid van de toplaag.',
                                       owner=self)

    @property
    def rolgeluid(self) -> DtcDocumentWaarden:
        """Proefresultaten van het rolgeluid van de toplaag."""
        return self._rolgeluid.get_waarde()

    @rolgeluid.setter
    def rolgeluid(self, value):
        self._rolgeluid.set_waarde(value, owner=self)
