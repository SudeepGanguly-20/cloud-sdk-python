"""Shared fixtures for agent_memory unit tests."""

from unittest.mock import patch

import pytest

_NO_CREDENTIALS = "sap_cloud_sdk.agent_memory.config._load_config_from_env"


@pytest.fixture(autouse=True)
def no_credentials(request):
    """Default: simulate no Agent Memory credentials so tests use in-memory path.

    Tests that need the credentials path must opt out via the
    'no_autouse_credentials' marker.
    """
    if request.node.get_closest_marker("no_autouse_credentials"):
        yield
        return
    with patch(_NO_CREDENTIALS, return_value=None):
        yield
