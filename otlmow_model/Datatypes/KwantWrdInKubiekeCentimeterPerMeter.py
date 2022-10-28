# coding=utf-8
from otlmow_model.BaseClasses.OTLAttribuut import OTLAttribuut
from otlmow_model.BaseClasses.OTLField import OTLField
from otlmow_model.BaseClasses.WaardenObject import WaardenObject
from otlmow_model.BaseClasses.FloatOrDecimalField import FloatOrDecimalField
from otlmow_model.BaseClasses.StringField import StringField


# Generated with OTLPrimitiveDatatypeCreator. To modify: extend, do not edit
class KwantWrdInKubiekeCentimeterPerMeterWaarden(WaardenObject):
    def __init__(self):
        WaardenObject.__init__(self)
        self._standaardEenheid = OTLAttribuut(field=StringField,
                                              naam='standaardEenheid',
                                              label='standaard eenheid',
                                              objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#KwantWrdInKubiekeCentimeterPerMeter.standaardEenheid',
                                              usagenote='"cm3/m"^^cdt:ucumunit',
                                              readonly=True,
                                              constraints='"cm3/m"^^cdt:ucumunit',
                                              definition='De standaard eenheid bij dit datatype is uitgedrukt in kubieke centimeter per meter.',
                                              owner=self)

        self._waarde = OTLAttribuut(field=FloatOrDecimalField,
                                    naam='waarde',
                                    label='waarde',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#KwantWrdInKubiekeCentimeterPerMeter.waarde',
                                    definition='Bevat een getal die bij het datatype hoort.',
                                    owner=self)

    @property
    def standaardEenheid(self):
        """De standaard eenheid bij dit datatype is uitgedrukt in kubieke centimeter per meter."""
        return self._standaardEenheid.usagenote.split('"')[1]

    @property
    def waarde(self):
        """Bevat een getal die bij het datatype hoort."""
        return self._waarde.get_waarde()

    @waarde.setter
    def waarde(self, value):
        self._waarde.set_waarde(value, owner=self._parent)


# Generated with OTLPrimitiveDatatypeCreator. To modify: extend, do not edit
class KwantWrdInKubiekeCentimeterPerMeter(OTLField):
    """Een kwantitatieve waarde die een getal in kubieke centimeter per meter uitdrukt."""
    naam = 'KwantWrdInKubiekeCentimeterPerMeter'
    label = 'Kwantitatieve waarde in kubieke centimeter per meter'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#KwantWrdInKubiekeCentimeterPerMeter'
    definition = 'Een kwantitatieve waarde die een getal in kubieke centimeter per meter uitdrukt.'
    waarde_shortcut_applicable = True
    waardeObject = KwantWrdInKubiekeCentimeterPerMeterWaarden

    def __str__(self):
        return OTLField.__str__(self)

