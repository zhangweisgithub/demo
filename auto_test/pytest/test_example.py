# content of test.py
import pytest
import os

from pre.common_func import get_config_with_sep_env, log_config
from interface.SEP.common.user import User

config = get_config_with_sep_env("dev")
log = log_config(out_path='.', filename='test_example', fix=True)[0]


class TestClass(object):
    def test_one(self):
        '''new_etests'''
        x = "this"
        assert 'h' in x

    @pytest.mark.slow
    def test_two(self):
        '''new_sssetests'''
        x = "hello"
        assert hasattr(x, 'check')

    @pytest.mark.parametrize("input_value", [1, 2, 3, 4, 5, 6, 7])
    def test_a(self, input_value):
        """abcttttt"""
        assert input_value > 2

    def test_b(self):
        """test_BBBBBBBB"""
        assert 1==3

    def test_c(self):
        assert 1 == 2


def testabc():
    "This is the 2 example"
    import os
    os.environ.setdefault("a", "1")
    assert 1 == int(os.environ.get("a"))


def test_login():
    host = config.get("host")
    user = config.get("user")
    passwd = config.get("password")
    print(config)
    ret = User.user_login(host=host, log=log, user=user, password=passwd)
    print(ret)


def test_configtst_compute(param_no):
    print(param_no)
    assert param_no < 4

