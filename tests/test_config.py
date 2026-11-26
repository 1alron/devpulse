from devpulse.core.config import Settings


def test_settings_use_defaults() -> None:
    settings = Settings(_env_file=None)

    assert settings.app_name == "DevPulse"
    assert settings.app_env == "development"


def test_settings_read_environment_variables(monkeypatch) -> None:
    monkeypatch.setenv("APP_NAME", "DevPulse Test")
    monkeypatch.setenv("APP_ENV", "test")

    settings = Settings(_env_file=None)

    assert settings.app_name == "DevPulse Test"
    assert settings.app_env == "test"
