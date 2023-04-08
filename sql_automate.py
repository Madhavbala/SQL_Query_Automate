import pandas as pd

query = "INSERT INTO schema_name.table_name(drug, category, Preferred_Name, requiredmed_pt, action_dts, act_uid) VALUES ('%s','%s','%s','',datetime(now() at time zone 'utc'), current_user);"
df = pd.read_csv(data_location)
queries = []
for row in range(len(df)):
    params = []
    df_record = df.iloc[[row]]
    params.extend([df_record['drug'].values[0], df_record['category'].values[0], df_record['name'].values[0]])
    queries.append(query % tuple(params) + "\n")
sql_file = open("queries.sql", "w")
sql_file.writelines(queries)