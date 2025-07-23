def ask_agent(nl_question):
    prompt = f"""You are an AI assistant.
Use the following SQLite tables to answer the question:

Tables:
1. product_ad_sales(date, item_id, ad_sales, impressions, ad_spend, clicks, units_sold)
2. product_eligibility(date, item_id, total_sales, total_units_ordered)
3. product_total_sales(eligibility_datetime_utc, item_id, eligibility, message)

Convert the question into a valid SQLite SQL query and answer it by querying these tables.

Question: "{nl_question}"
"""
    return query_engine.query(prompt)
