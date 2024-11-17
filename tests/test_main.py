from unittest.mock import patch

from main import (views_option, services_option, reports_option)


@patch("main.input")
def test_views_option(mock_input) -> None:
    mock_input.return_value = "2024-11-21 12:12:00"
    assert views_option() is None


@patch("main.input")
def test_services_option(mock_input) -> None:
    mock_input.side_effect = ["2024-11", '10']
    assert services_option() is None

@patch("main.input")
def test_reports_option(mock_input) -> None:
    mock_input.side_effect = ["Каршеринг", '']
    assert reports_option() is None