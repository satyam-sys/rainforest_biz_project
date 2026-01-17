from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from enrich_accounts.config.ConfigStore import *
from enrich_accounts.functions import *

def SelectFields(spark: SparkSession, salesforce_Opportunity: DataFrame) -> DataFrame:
    return salesforce_Opportunity.select(
        col("AccountId"), 
        col("Amount"), 
        col("ExpectedRevenue"), 
        concat(year(col("CloseDate")), lit("-Q"), quarter(col("CloseDate"))).alias("CloseQtr")
    )
