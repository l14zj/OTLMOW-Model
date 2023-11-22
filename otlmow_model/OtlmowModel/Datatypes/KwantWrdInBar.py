# coding=utf-8
from ..BaseClasses.OTLObject import OTLAttribuut
from ..BaseClasses.OTLField import OTLField
from ..BaseClasses.WaardenObject import WaardenObject
from ..BaseClasses.FloatOrDecimalField import FloatOrDecimalField
from ..BaseClasses.StringField import StringField


# Generated with OTLPrimitiveDatatypeCreator. To modify: extend, do not edit
class KwantWrdInBarWaarden(WaardenObject):
    def __init__(self):
        WaardenObject.__init__(self)
        self._standaardEenheid = OTLAttribuut(field=StringField,
                                              naam='standaardEenheid',
                                              label='standaard eenheid',
                                              objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#KwantWrdInBar.standaardEenheid',
                                              usagenote='"bar"^^cdt:ucumunit',
                                              readonly=True,
                                              constraints='"bar"^^cdt:ucumunit',
                                              definition='De standaard eenheid bij dit datatype is uitgedrukt in bar.',
                                              owner=self)

        self._waarde = OTLAttribuut(field=FloatOrDecimalField,
                                    naam='waarde',
                                    label='waarde',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#KwantWrdInBar.waarde',
                                    definition='Bevat een getal die bij het datatype hoort.',
                                    owner=self)

    @property
    def standaardEenheid(self) -> str:
        """De standaard eenheid bij dit datatype is uitgedrukt in bar."""
        return self._standaardEenheid.usagenote.split('"')[1]

    @property
    def waarde(self) -> float:
        """Bevat een getal die bij het datatype hoort."""
        return self._waarde.get_waarde()

    @waarde.setter
    def waarde(self, value):
        self._waarde.set_waarde(value, owner=self._parent)


# Generated with OTLPrimitiveDatatypeCreator. To modify: extend, do not edit
class KwantWrdInBar(OTLField):
    """Een kwantitatieve waarde die een getal in bar uitdrukt."""
    naam = 'KwantWrdInBar'
    label = 'Kwantitatieve waarde in bar'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#KwantWrdInBar'
    definition = 'Een kwantitatieve waarde die een getal in bar uitdrukt.'
    waarde_shortcut_applicable = True
    waardeObject = KwantWrdInBarWaarden

    def __str__(self):
        return OTLField.__str__(self)
