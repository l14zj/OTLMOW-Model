# coding=utf-8
from otlmow_model.BaseClasses.OTLObject import OTLAttribuut
from otlmow_model.BaseClasses.OTLField import OTLField
from otlmow_model.BaseClasses.WaardenObject import WaardenObject
from otlmow_model.BaseClasses.FloatOrDecimalField import FloatOrDecimalField
from otlmow_model.BaseClasses.StringField import StringField


# Generated with OTLPrimitiveDatatypeCreator. To modify: extend, do not edit
class KwantWrdInGigabyteWaarden(WaardenObject):
    def __init__(self):
        WaardenObject.__init__(self)
        self._standaardEenheid = OTLAttribuut(field=StringField,
                                              naam='standaardEenheid',
                                              label='standaard eenheid',
                                              objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#KwantWrdInGigabyte.standaardEenheid',
                                              usagenote='"GBy"^^cdt:ucumunit',
                                              readonly=True,
                                              constraints='"GBy"^^cdt:ucumunit',
                                              definition='De standaard eenheid bij dit datatype is uitgedrukt in gigabyte.',
                                              owner=self)

        self._waarde = OTLAttribuut(field=FloatOrDecimalField,
                                    naam='waarde',
                                    label='waarde',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#KwantWrdInGigabyte.waarde',
                                    definition='Bevat een getal die bij het datatype hoort.',
                                    owner=self)

    @property
    def standaardEenheid(self) -> str:
        """De standaard eenheid bij dit datatype is uitgedrukt in gigabyte."""
        return self._standaardEenheid.usagenote.split('"')[1]

    @property
    def waarde(self) -> float:
        """Bevat een getal die bij het datatype hoort."""
        return self._waarde.get_waarde()

    @waarde.setter
    def waarde(self, value):
        self._waarde.set_waarde(value, owner=self._parent)


# Generated with OTLPrimitiveDatatypeCreator. To modify: extend, do not edit
class KwantWrdInGigabyte(OTLField):
    """Een kwantitatieve waarde die een getal in gigabyte uitdrukt."""
    naam = 'KwantWrdInGigabyte'
    label = 'Kwantitatieve waarde in gigabyte'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#KwantWrdInGigabyte'
    definition = 'Een kwantitatieve waarde die een getal in gigabyte uitdrukt.'
    waarde_shortcut_applicable = True
    waardeObject = KwantWrdInGigabyteWaarden

    def __str__(self):
        return OTLField.__str__(self)

