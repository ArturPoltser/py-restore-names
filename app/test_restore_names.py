import pytest
from app.restore_names import restore_names


@pytest.mark.parametrize(
    "users_list,expected_result",
    [
        ([
            {
                "first_name": None,
                "last_name": "Holy",
                "full_name": "Jack Holy",
            },
            {
                "last_name": "Adams",
                "full_name": "Mike Adams",
            },
        ], [
            {
                "first_name": "Jack",
                "last_name": "Holy",
                "full_name": "Jack Holy",
            },
            {
                "first_name": "Mike",
                "last_name": "Adams",
                "full_name": "Mike Adams",
            },
        ])
    ]
)
def test_should_return_correct_user_list(
        users_list: list[dict],
        expected_result: list[dict]
) -> None:
    restore_names(users_list)
    assert users_list == expected_result
