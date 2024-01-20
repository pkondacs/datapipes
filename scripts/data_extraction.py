# codes to be added
class extract_full_dataset:
    def __init__(self, valid_from, valid_to, filter_cond=""):
        self.valid_from = valid_from
        self.valid_to = valid_to
        self.filter_cond = filter_cond

    def extract_full_dataset(self, valid_from, valid_to, filter_cond=""):
        valid_from = clean_string_to_datetime(valid_from, get_str=True)
        valid_to = clean_string_to_datetime(valid_to, get_str=True)
        if valid_from != "9999-12-31":
            df = (self.spark.read.format(self.data_format)
                  .option("mergeSchema", "true")
                  .load(self.location)
                  .withColumn('valid_from', F.to_date(F.lit(valid_from)))
                  .withColumn('valid_to', F.to_date(F.lit(valid_to)))
                  .where('snapshot_date >= valid_from AND snapshot_date <= valid_to'))
            df = df.drop('valid_from', 'valid_to')
        else:
            df = (self.spark.read.format(self.data_format)
                  .option("mergeSchema", "true")
                  .load(self.location))

        if filter_cond:
            df = df.where(filter_cond)
        return df

    def select_used_fields(self, dataframe, used_fields):
        return dataframe.select([c.lower() for c in used_fields])  # check CRC custom...

    def reduce_to_unique_set(self, dataframe, business_keys):
        """This method captures the unique changes in the incoming data set over all snapshots.
        codes to be added
        """