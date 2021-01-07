from nose.tools import assert_raises


def pos_only_params(one, two, /, three, four):
    print(one, two, three, four)


def kw_only_params(one, two, *, three, four):
    print(one, two, three, four)


def test_pos_only_params_ok():
    pos_only_params(1, 2, 3, 4)


def test_pos_only_params_error():
    with assert_raises(TypeError) as error:
        pos_only_params(one=1, two=2, three=3, four=4)
    assert error.exception.args[0] == "pos_only_params() got some positional-only " \
                                      "arguments passed as keyword arguments: 'one, two'"


def test_kw_only_params_ok():
    kw_only_params(1, 2, three=3, four=4)
    kw_only_params(1, two=2, three=3, four=4)
    kw_only_params(one=1, two=2, three=3, four=4)


def test_kw_only_params_error():
    with assert_raises(TypeError) as error:
        kw_only_params(1, 2, 3, 4)
    assert error.exception.args[0] == "kw_only_params() takes 2 positional arguments but 4 " \
                                      "were given"
