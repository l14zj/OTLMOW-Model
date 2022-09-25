# coding=utf-8
from otlmow_model.BaseClasses.OTLAttribuut import OTLAttribuut
from otlmow_model.Classes.Abstracten.AxiaalDraagvermogen import AxiaalDraagvermogen
from otlmow_model.Classes.Abstracten.Fundering import Fundering
from otlmow_model.Datatypes.DtuDwarsafmetingen import DtuDwarsafmetingen
from otlmow_model.Datatypes.DtuHellingsSchoorhoek import DtuHellingsSchoorhoek
from otlmow_model.Datatypes.KwantWrdInMeter import KwantWrdInMeter
from otlmow_model.Datatypes.KwantWrdInMeterTAW import KwantWrdInMeterTAW
from otlmow_model.GeometrieTypes.PuntGeometrie import PuntGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class Funderingspaal(AxiaalDraagvermogen, Fundering, PuntGeometrie):
    """Diepfundering waarbij d.m.v. palen de belasting wordt afgedragen naar de diepe ondergrond. Enkel te gebruiken wanneer het type paal nog niet is vastgelegd bij ontwerp."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Funderingspaal'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        AxiaalDraagvermogen.__init__(self)
        Fundering.__init__(self)
        PuntGeometrie.__init__(self)

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Behuizing')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Hoppinzuil')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Inloopbehuizing')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#KabelgeleidingEnLeidingBevestiging')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Kast')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#SteunStandaard')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Verlichtingstoestel')

        self._afkappeil = OTLAttribuut(field=KwantWrdInMeterTAW,
                                       naam='afkappeil',
                                       label='afkappeil',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Funderingspaal.afkappeil',
                                       definition='De hoogte van het bovenvlak van de paal, na verwijderen van eventuele overlengte, exclusief uitstekende wapening. Berekend ten opzichte van gemiddeld laagwaterpeil te Oostende (TAWpeil).',
                                       owner=self)

        self._dwarsafmetingen = OTLAttribuut(field=DtuDwarsafmetingen,
                                             naam='dwarsafmetingen',
                                             label='dwarsafmetingen',
                                             objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Funderingspaal.dwarsafmetingen',
                                             definition='Dwarsdoorsnede van het element bv. lengte, breedte, diameter,...',
                                             owner=self)

        self._hellingsSchoorhoek = OTLAttribuut(field=DtuHellingsSchoorhoek,
                                                naam='hellingsSchoorhoek',
                                                label='hellings- of schoorhoek',
                                                objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Funderingspaal.hellingsSchoorhoek',
                                                definition='De hoek die de paal maakt ten opzichte van de verticale, uitgedrukt in decimale graden of in 1 op x.',
                                                owner=self)

        self._paallengte = OTLAttribuut(field=KwantWrdInMeter,
                                        naam='paallengte',
                                        label='paallengte',
                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Funderingspaal.paallengte',
                                        definition='Afstand gemeten, in meter, volgens de as van de paal tussen het afkappeil en het aanzetpeil.',
                                        owner=self)

    @property
    def afkappeil(self):
        """De hoogte van het bovenvlak van de paal, na verwijderen van eventuele overlengte, exclusief uitstekende wapening. Berekend ten opzichte van gemiddeld laagwaterpeil te Oostende (TAWpeil)."""
        return self._afkappeil.get_waarde()

    @afkappeil.setter
    def afkappeil(self, value):
        self._afkappeil.set_waarde(value, owner=self)

    @property
    def dwarsafmetingen(self):
        """Dwarsdoorsnede van het element bv. lengte, breedte, diameter,..."""
        return self._dwarsafmetingen.get_waarde()

    @dwarsafmetingen.setter
    def dwarsafmetingen(self, value):
        self._dwarsafmetingen.set_waarde(value, owner=self)

    @property
    def hellingsSchoorhoek(self):
        """De hoek die de paal maakt ten opzichte van de verticale, uitgedrukt in decimale graden of in 1 op x."""
        return self._hellingsSchoorhoek.get_waarde()

    @hellingsSchoorhoek.setter
    def hellingsSchoorhoek(self, value):
        self._hellingsSchoorhoek.set_waarde(value, owner=self)

    @property
    def paallengte(self):
        """Afstand gemeten, in meter, volgens de as van de paal tussen het afkappeil en het aanzetpeil."""
        return self._paallengte.get_waarde()

    @paallengte.setter
    def paallengte(self, value):
        self._paallengte.set_waarde(value, owner=self)