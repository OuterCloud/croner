$interval = Read-Host "每隔多少秒执行一次测试"
$scriptPath = $MyInvocation.MyCommand.Path
$rootPath = Split-Path -Parent $MyInvocation.InvocationName
$driver = [io.path]::combine($rootPath,"lib","cron.py")
python $driver $interval 