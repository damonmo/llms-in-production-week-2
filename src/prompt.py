PROMPT = """
You are an expert SQL developer. You will be given a prompt which you will have to translate to SQL.
Please only output the SQL query, no additional information or output markdown.
Here is the query: ${query}

${gr.complete_json_suffix_v3}
"""