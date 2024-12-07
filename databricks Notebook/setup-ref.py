val AwProjectSecret = dbutils.secrets.get("intechprojectScope", "secrectkeys")  ## app01 secrets value "secrectkeys"
val client_id = dbutils.secrets.get("intechprojectScope", "clientidkey") ## app01 client id  value "clientidkey"
val tenant_id = dbutils.secrets.get("intechprojectScope", "tenantidkey") app01 tenant id  value "tenantidkey"

val configs = Map(
  "fs.azure.account.auth.type" -> "OAuth",
  "fs.azure.account.oauth.provider.type" -> "org.apache.hadoop.fs.azurebfs.oauth2.ClientCredsTokenProvider",
  "fs.azure.account.oauth2.client.id" -> client_id,
  "fs.azure.account.oauth2.client.secret" -> AwProjectSecret,
  "fs.azure.account.oauth2.client.endpoint" -> s"https://login.microsoftonline.com/$tenant_id/oauth2/token"
)


dbutils.fs.mount(
  source = "abfss://bronze@storagedatalakechetan.dfs.core.windows.net/",
  mountPoint = "/mnt/bronze",
  extraConfigs = configs
)



dbutils.fs.mount(
  source = "abfss://silver@storagedatalakechetan.dfs.core.windows.net/",
  mountPoint = "/mnt/silver",
  extraConfigs = configs
)

dbutils.fs.mount(
  source = "abfss://gold@storagedatalakechetan.dfs.core.windows.net/",
  mountPoint = "/mnt/gold",
  extraConfigs = configs
)
