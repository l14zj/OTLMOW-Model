# coding=utf-8
from otlmow_model.BaseClasses.OTLObject import OTLAttribuut
from otlmow_model.Classes.Onderdeel.BetonnenConstructieObject import BetonnenConstructieObject
from otlmow_model.Datatypes.KwantWrdInMeterTAW import KwantWrdInMeterTAW, KwantWrdInMeterTAWWaarden
from otlmow_model.GeometrieTypes.PuntGeometrie import PuntGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class BetonnenPredal(BetonnenConstructieObject, PuntGeometrie):
    """Betonnen plaat van 15 cm dik met een tralieligger, gebruikt voor de opbouw van een definitieve berlinerwand."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#BetonnenPredal'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        BetonnenConstructieObject.__init__(self)
        PuntGeometrie.__init__(self)

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#BekledingComponent')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Inloopbehuizing')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#KabelgeleidingEnLeidingBevestiging')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Kast')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Verlichtingstoestel')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Berlinerwand')

        self._aanzetpeil = OTLAttribuut(field=KwantWrdInMeterTAW,
                                        naam='aanzetpeil',
                                        label='aanzetpeil',
                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#BetonnenPredal.aanzetpeil',
                                        definition='Aanzetpeil van de predal in mTaw.',
                                        owner=self)

    @property
    def aanzetpeil(self) -> KwantWrdInMeterTAWWaarden:
        """Aanzetpeil van de predal in mTaw."""
        return self._aanzetpeil.get_waarde()

    @aanzetpeil.setter
    def aanzetpeil(self, value):
        self._aanzetpeil.set_waarde(value, owner=self)