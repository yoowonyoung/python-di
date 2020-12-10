from di.utils.config.settings import config


def test_load_config_default():
    assert len(config) == 4
