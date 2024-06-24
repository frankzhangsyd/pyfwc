import pytest
import pandas as pd
from pyfwc.fwc import FWCAPI

@pytest.fixture()
def fwc(API_KEY):
    print(API_KEY)
    print(len(API_KEY))
    fwc = FWCAPI(API_KEY)
    return fwc


def test_get_awards(fwc):
    result = fwc.get_awards(name="mining")

    assert result["name"].iloc[0] == "Black Coal Mining Industry Award 2020"
    assert result["name"].iloc[1] == "Mining Industry Award 2020"

def test_get_award(fwc):
    result = fwc.get_award(id_or_code='MA000001').head(3)

    assert result["name"].iloc[0] == "Black Coal Mining Industry Award 2020"


def test_get_classification(fwc):
    result = fwc.get_classification(id_or_code='MA000002',classification_fixed_id='98')

    assert result["classification_fixed_id"].iloc[0] == 98
    assert result["classification"].iloc[0] == "Level 1—Year 1"

def test_get_current_payrate(fwc):
    result = fwc.get_current_payrate(id_or_code='MA000012',classification_fixed_id='549')

    assert result["classification"].iloc[0] == "Pharmacy assistant level 1"

def test_get_expense_allowance(fwc):
    result = fwc.get_expense_allowance(id_or_code='MA000012',expense_allowance_fixed_id='49')

    assert result["allowance"].iloc[0] == "Meal allowance—overtime which exceeds 1.5 hours"

def test_get_penalties(fwc):
    result = fwc.get_penalties(id_or_code='MA000012').sort_values("penalty_fixed_id").head(3)

    assert result["penalty_fixed_id"].iloc[0] == 2126

def test_get_wage_allowances(fwc):
    result = fwc.get_wage_allowances(id_or_code='MA000012').head(3)

    assert result["wage_allowance_fixed_id"].iloc[0] == 191
