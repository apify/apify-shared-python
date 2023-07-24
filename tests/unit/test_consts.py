import itertools

from apify_shared.consts import BOOL_ENV_VARS, DATETIME_ENV_VARS, FLOAT_ENV_VARS, INTEGER_ENV_VARS, STRING_ENV_VARS, ApifyEnvVars


class TestConsts:  # noqa: D101

    def test_env_vars_types_unique(self) -> None:
        """Test that env var types don't contain any item twice."""
        for env_var_type in [BOOL_ENV_VARS, DATETIME_ENV_VARS, FLOAT_ENV_VARS, INTEGER_ENV_VARS, STRING_ENV_VARS]:
            assert isinstance(env_var_type, list)
            assert len(env_var_type) == len(set(env_var_type))

    def test_env_vars_types_do_not_overlap(self) -> None:
        """Test that there is no overlap between env var types."""
        for first, second in itertools.combinations([BOOL_ENV_VARS, DATETIME_ENV_VARS, FLOAT_ENV_VARS, INTEGER_ENV_VARS, STRING_ENV_VARS], 2):
            assert isinstance(first, list)
            assert isinstance(second, list)
            assert not set(first) & set(second)

    def test_env_vars_types_defined_for_all_env_vars(self) -> None:
        """Test that all env vars from `ApifyEnvVars` have a defined type."""
        env_vars_from_types = set(
            list(BOOL_ENV_VARS) + list(DATETIME_ENV_VARS) + list(FLOAT_ENV_VARS) + list(INTEGER_ENV_VARS) + list(STRING_ENV_VARS),
        )
        env_vars_from_enum = set(ApifyEnvVars)
        assert env_vars_from_types == env_vars_from_enum
