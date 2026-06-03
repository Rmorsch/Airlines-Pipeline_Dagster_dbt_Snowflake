# airlines-pipeline\src\airlines_pipeline\defs\resources.py
from dagster_snowflake import SnowflakeResource
import dagster as dg

snowflake_resource = SnowflakeResource(
    account=dg.EnvVar("SNOWFLAKE_ACCOUNT"),
    user=dg.EnvVar("SNOWFLAKE_USER"),
    password=dg.EnvVar("SNOWFLAKE_PASSWORD"),
    database=dg.EnvVar("SNOWFLAKE_DATABASE"),
    warehouse=dg.EnvVar("SNOWFLAKE_WAREHOUSE"),
)

@dg.definitions
def resources() -> dg.Definitions:
    return dg.Definitions(resources={"snowflake": snowflake_resource})