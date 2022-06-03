from typing import List
from abbreviator import path_join, main
import pytest
@pytest.mark.parametrize("path, expect",
    [
        ([""], "/"), 
        (["hello"], "/hello"), 
        (["hello world", "my name is weird", "so_please_concat"], "/hello world/my name is weird/so_please_concat")
    ])
def test_path_join(path:List[str], expect:str):
    assert(path_join(path) == expect)

