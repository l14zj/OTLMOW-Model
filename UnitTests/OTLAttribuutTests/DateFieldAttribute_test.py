import datetime
import pytest

from UnitTests.TestClasses.Classes.Onderdeel.AllCasesTestClass import AllCasesTestClass
from otlmow_model.warnings.IncorrectTypeWarning import IncorrectTypeWarning


def test_datefield_with_correct_input(subtests):
    instance = AllCasesTestClass()
    with subtests.test(msg='empty instance'):
        assert instance.testDateField is None

    with subtests.test(msg='assign values to DateField with correct date'):
        instance.testDateField = '2020-01-01'
        assert instance.testDateField == datetime.date(2020, 1, 1)
        instance.testDateField = '2020-1-1'
        assert instance.testDateField == datetime.date(2020, 1, 1)
        instance.testDateField = '1/1/2020'
        assert instance.testDateField == datetime.date(2020, 1, 1)


def test_datefield_with_datetime_val(subtests,caplog):
    instance = AllCasesTestClass()
    with subtests.test(msg='empty instance'):
        assert instance.testDateField is None

    with pytest.warns(IncorrectTypeWarning):
        instance.testDateField = datetime.datetime(2020, 1, 1, 2, 2, 2)
