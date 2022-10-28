# coding=utf-8
from otlmow_model.BaseClasses.OTLAttribuut import OTLAttribuut
from otlmow_model.BaseClasses.WaardenObject import WaardenObject
from otlmow_model.BaseClasses.ComplexField import ComplexField
from otlmow_model.Datatypes.KwantWrdInMeter import KwantWrdInMeter


# Generated with OTLComplexDatatypeCreator. To modify: extend, do not edit
class DtcAfmetingBxhInMWaarden(WaardenObject):
    def __init__(self):
        WaardenObject.__init__(self)
        self._breedte = OTLAttribuut(field=KwantWrdInMeter,
                                     naam='breedte',
                                     label='breedte',
                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcAfmetingBxhInM.breedte',
                                     definition='De breedte in meter.',
                                     owner=self)

        self._hoogte = OTLAttribuut(field=KwantWrdInMeter,
                                    naam='hoogte',
                                    label='hoogte',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcAfmetingBxhInM.hoogte',
                                    definition='De hoogte in meter.',
                                    owner=self)

    @property
    def breedte(self):
        """De breedte in meter."""
        return self._breedte.get_waarde()

    @breedte.setter
    def breedte(self, value):
        self._breedte.set_waarde(value, owner=self._parent)

    @property
    def hoogte(self):
        """De hoogte in meter."""
        return self._hoogte.get_waarde()

    @hoogte.setter
    def hoogte(self, value):
        self._hoogte.set_waarde(value, owner=self._parent)


# Generated with OTLComplexDatatypeCreator. To modify: extend, do not edit
class DtcAfmetingBxhInM(ComplexField):
    """Complex datatype voor de afmeting van de breedte en hoogte in meter."""
    naam = 'DtcAfmetingBxhInM'
    label = 'Afmeting bxh in meter'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcAfmetingBxhInM'
    definition = 'Complex datatype voor de afmeting van de breedte en hoogte in meter.'
    waardeObject = DtcAfmetingBxhInMWaarden

    def __str__(self):
        return ComplexField.__str__(self)

