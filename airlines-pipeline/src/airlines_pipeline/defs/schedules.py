# src/dagster_essentials/defs/schedules.py
import dagster as dg
from airlines_pipeline.defs.jobs import aal_quote_job, ual_quote_job

aal_quote_schedule = dg.ScheduleDefinition(
    job=aal_quote_job,
    cron_schedule="*/2 * * * *", # every 2 minute
)

ual_quote_schedule = dg.ScheduleDefinition(
    job=ual_quote_job,
    cron_schedule="*/2 * * * *", # every 2 minute
)