import pytest

import pandas as pd

from titanic.features.fill import *

'''

@pytest.mark.parametrize("test_input,expected", [((1,2,4,None,4,4,4,5), (1,2,4,4,4,4,4,5) )])
def test_fill_age(test_input, expected):
    df = pd.DataFrame(
        data={"SibSp": [test_input[0]], "Parch": [test_input[1]]},
    )
    assert expected == family_size(df).iloc[0]


'''
