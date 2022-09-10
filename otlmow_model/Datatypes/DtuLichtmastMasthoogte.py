# coding=utf-8
from otlmow_model.BaseClasses.AttributeInfo import AttributeInfo
from otlmow_model.BaseClasses.OTLAttribuut import OTLAttribuut
from otlmow_model.Datatypes.KlLichtmastMasthoogte import KlLichtmastMasthoogte
from otlmow_model.Datatypes.KwantWrdInMeter import KwantWrdInMeter
from otlmow_model.BaseClasses.UnionTypeField import UnionTypeField
from otlmow_model.BaseClasses.UnionWaarden import UnionWaarden


# Generated with OTLUnionDatatypeCreator. To modify: extend, do not edit
class DtuLichtmastMasthoogteWaarden(AttributeInfo, UnionWaarden):
    def __init__(self, parent=None):
        AttributeInfo.__init__(self, parent)
        UnionWaarden.__init__(self)
        self._afwijkendeHoogte = OTLAttribuut(field=KwantWrdInMeter,
                                              naam='afwijkendeHoogte',
                                              label='afwijkende hoogte',
                                              objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DtuLichtmastMasthoogte.afwijkendeHoogte',
                                              kardinaliteit_min='0',
                                              definition='De afwijkende hoogte van de mast in meter.',
                                              owner=self)

        self._standaardHoogte = OTLAttribuut(field=KlLichtmastMasthoogte,
                                             naam='standaardHoogte',
                                             label='standaard hoogte',
                                             objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DtuLichtmastMasthoogte.standaardHoogte',
                                             kardinaliteit_min='0',
                                             definition='Bepaling van de standaard hoogte van een mast.',
                                             owner=self)

    @property
    def afwijkendeHoogte(self):
        """De afwijkende hoogte van de mast in meter."""
        return self._afwijkendeHoogte.get_waarde()

    @afwijkendeHoogte.setter
    def afwijkendeHoogte(self, value):
        self._afwijkendeHoogte.set_waarde(value, owner=self._parent)
        if value is not None:
            self.clear_other_props('_afwijkendeHoogte')

    @property
    def standaardHoogte(self):
        """Bepaling van de standaard hoogte van een mast."""
        return self._standaardHoogte.get_waarde()

    @standaardHoogte.setter
    def standaardHoogte(self, value):
        self._standaardHoogte.set_waarde(value, owner=self._parent)
        if value is not None:
            self.clear_other_props('_standaardHoogte')


# Generated with OTLUnionDatatypeCreator. To modify: extend, do not edit
class DtuLichtmastMasthoogte(UnionTypeField, AttributeInfo):
    """Union datatype om een standaard of afwijkende masthoogte te bepalen."""
    naam = 'DtuLichtmastMasthoogte'
    label = 'Masthoogte'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DtuLichtmastMasthoogte'
    definition = 'Union datatype om een standaard of afwijkende masthoogte te bepalen.'
    waardeObject = DtuLichtmastMasthoogteWaarden

    def __str__(self):
        return UnionTypeField.__str__(self)

