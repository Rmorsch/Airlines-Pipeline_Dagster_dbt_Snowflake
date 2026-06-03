import dagster as dg

aal_stock_price = dg.AssetSelection.assets("aal_stock_price")
ual_stock_price = dg.AssetSelection.assets("ual_stock_price")

aal_quote_job = dg.define_asset_job(
    name="aal_quote_job",
    selection=aal_stock_price,
)

ual_quote_job = dg.define_asset_job(
    name="ual_quote_job",
    selection=ual_stock_price,
)
