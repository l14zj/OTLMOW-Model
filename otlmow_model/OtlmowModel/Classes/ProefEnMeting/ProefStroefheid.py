# coding=utf-8
from ...BaseClasses.OTLObject import OTLAttribuut
from ...Classes.Abstracten.Proef import Proef
from ...Datatypes.DtcDocument import DtcDocument, DtcDocumentWaarden
from ...GeometrieTypes.PuntGeometrie import PuntGeometrie
from ...GeometrieTypes.LijnGeometrie import LijnGeometrie
from ...GeometrieTypes.VlakGeometrie import VlakGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class ProefStroefheid(Proef, PuntGeometrie, LijnGeometrie, VlakGeometrie):
    """Het vermogen van een wegdek om door voertuigbanden tangentieel uitgeoefende krachten (bij het nemen van bochten, afremmen of optrekken) te compenseren door even grote wrijvingskrachten."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/proefenmeting#ProefStroefheid'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#IsInspectieVan', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Markering')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#IsInspectieVan', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bestrijking')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#IsInspectieVan', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Cementbetonverharding')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#IsInspectieVan', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DunneOverlaging')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#IsInspectieVan', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Slemlaag')

        self._stroefheid = OTLAttribuut(field=DtcDocument,
                                        naam='stroefheid',
                                        label='stroefheid',
                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/proefenmeting#ProefStroefheid.stroefheid',
                                        definition='Proefresultaten van de stroefheid.',
                                        owner=self)

    @property
    def stroefheid(self) -> DtcDocumentWaarden:
        """Proefresultaten van de stroefheid."""
        return self._stroefheid.get_waarde()

    @stroefheid.setter
    def stroefheid(self, value):
        self._stroefheid.set_waarde(value, owner=self)
