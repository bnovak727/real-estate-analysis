
# Helper Functions
def gt_quantile_name(df_in, q_name, q_value):
    threshold = df_in[q_name].quantile(q_value)
    df_out = df_in.loc[df_in[q_name] > threshold]
    return df_out

def gt_quantile_loc(df_in, loc, q_value):
    threshold = df_in.iloc[loc].quantile(q_value)
    df_out = df_in.loc[df_in.iloc[:,loc] > threshold]
    return df_out

def lt_quantile_name(df_in, q_name, q_value):
    threshold = df_in[q_name].quantile(q_value)
    df_out = df_in.loc[df_in[q_name] < threshold]
    return df_out

def lt_quantile_loc(df_in, loc, q_value):
    threshold = df_in.iloc[loc].quantile(q_value)
    df_out = df_in.loc[df_in.iloc[:,loc] < threshold]
    return df_out

def get_df_col(df_in, col_name):
    df_out = df_in.loc[:, [col_name]]
    return df_out

