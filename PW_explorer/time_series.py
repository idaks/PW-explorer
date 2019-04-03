from .meta_data_parser import META_DATA_TEMPORAL_DEC_KEYWORD


class PWETimeSeriesModule:

    CONSTANT_STATE_KEYWORD = 'constant'

    @staticmethod
    def group_by_time(dfs, rels):
        time_to_state_mapper = {}
        temporal_rels = [rel for rel in rels
                         if ((META_DATA_TEMPORAL_DEC_KEYWORD in rel.meta_data) and (len(rel.meta_data[META_DATA_TEMPORAL_DEC_KEYWORD]) > 0))]
        # i.e. it has atleast one temporal column
        # In fact at this point we only use the first temporal column
        temporal_rel_names = {rel.relation_name for rel in temporal_rels}
        non_temporal_rel_names = set(dfs.keys()) - temporal_rel_names
        time_to_state_mapper[PWETimeSeriesModule.CONSTANT_STATE_KEYWORD] = {}
        for rl_name in non_temporal_rel_names:
            time_to_state_mapper[PWETimeSeriesModule.CONSTANT_STATE_KEYWORD][rl_name] = dfs[rl_name]
        for rl in temporal_rels:
            rl_name = rl.relation_name
            temporal_index = rl.meta_data[META_DATA_TEMPORAL_DEC_KEYWORD][0]
            df = dfs[rl_name]
            temporal_col_name = df.columns[temporal_index + 1]  # +1 to a/c for the 'pw' column
            df_grouped_by_time_step = df.groupby(temporal_col_name)
            for t, df_at_t in df_grouped_by_time_step:
                if t not in time_to_state_mapper:
                    time_to_state_mapper[t] = {}
                time_to_state_mapper[t][rl_name] = df_at_t[
                    [i for i in list(df_at_t.columns) if i not in [temporal_col_name]]]
        return time_to_state_mapper


    @staticmethod
    def simple_timeseries_text_visualization(time_state_mapper: dict, jupyter=False):
        """
        :param time_state_mapper: dict containing the keys 'constant' and timesteps: ints or other keys that
               can be sorted.
               Each value must be a dictionary (relation_name --> pandas dataframe of relation atoms at that time_step)
               Generated by group_by_time function in the PWETimeSeriesModule.
        :param jupyter: Set to true if displaying in a jupyter notebook. Will display the dataframes
               in a cleaner fashion.
        """

        def print_rl_name_and_df(rl_name, rl_df, jupyter=False):
            print("")
            print("{}:".format(rl_name))
            if jupyter:
                display(rl_df)
            else:
                print(rl_df.to_string())
            print("")

        def print_time_step(t):
            print("{}\nTimestep {}:\n{}".format("-" * 15, t, "-" * 15))

        print("Constants:")
        for rl_name, rl_df in time_state_mapper[PWETimeSeriesModule.CONSTANT_STATE_KEYWORD].items():
            print_rl_name_and_df(rl_name, rl_df, jupyter)

        for t in sorted(set(time_state_mapper.keys()) - set([PWETimeSeriesModule.CONSTANT_STATE_KEYWORD])):
            if t == PWETimeSeriesModule.CONSTANT_STATE_KEYWORD:
                continue
            print("\n")
            print_time_step(t)
            for rl_name, rl_df in time_state_mapper[t].items():
                print_rl_name_and_df(rl_name, rl_df, jupyter)

        print("END")