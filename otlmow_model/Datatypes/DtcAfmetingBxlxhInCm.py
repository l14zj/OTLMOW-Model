# coding=utf-8
from otlmow_model.BaseClasses.OTLAttribuut import OTLAttribuut
from otlmow_model.BaseClasses.WaardenObject import WaardenObject
from otlmow_model.BaseClasses.ComplexField import ComplexField
from otlmow_model.Datatypes.KwantWrdInCentimeter import KwantWrdInCentimeter


# Generated with OTLComplexDatatypeCreator. To modify: extend, do not edit
class DtcAfmetingBxlxhInCmWaarden(WaardenObject):
    def __init__(self):
        WaardenObject.__init__(self)
        self._breedte = OTLAttribuut(field=KwantWrdInCentimeter,
                                     naam='breedte',
                                     label='breedte',
                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcAfmetingBxlxhInCm.breedte',
                                     definition='De breedte in centimeter.',
                                     owner=self)

        self._hoogte = OTLAttribuut(field=KwantWrdInCentimeter,
                                    naam='hoogte',
                                    label='hoogte',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcAfmetingBxlxhInCm.hoogte',
                                    definition='De hoogte in centimeter.',
                                    owner=self)

        self._lengte = OTLAttribuut(field=KwantWrdInCentimeter,
                                    naam='lengte',
                                    label='lengte',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcAfmetingBxlxhInCm.lengte',
                                    definition='De lengte in centimeter.',
                                    owner=self)

    @property
    def breedte(self):
        """De breedte in centimeter."""
        return self._breedte.get_waarde()

    @breedte.setter
    def breedte(self, value):
        self._breedte.set_waarde(value, owner=self._parent)

    @property
    def hoogte(self):
        """De hoogte in centimeter."""
        return self._hoogte.get_waarde()

    @hoogte.setter
    def hoogte(self, value):
        self._hoogte.set_waarde(value, owner=self._parent)

    @property
    def lengte(self):
        """De lengte in centimeter."""
        return self._lengte.get_waarde()

    @lengte.setter
    def lengte(self, value):
        self._lengte.set_waarde(value, owner=self._parent)


# Generated with OTLComplexDatatypeCreator. To modify: extend, do not edit
class DtcAfmetingBxlxhInCm(ComplexField):
    """Complex datatype voor de afmeting van de breedte,de lengte en hoogte in centimeter."""
    naam = 'DtcAfmetingBxlxhInCm'
    label = 'Afmeting bxlxh in centimeter'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcAfmetingBxlxhInCm'
    definition = 'Complex datatype voor de afmeting van de breedte,de lengte en hoogte in centimeter.'
    waardeObject = DtcAfmetingBxlxhInCmWaarden

    def __str__(self):
        return ComplexField.__str__(self)

