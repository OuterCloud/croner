$scriptPath = $MyInvocation.MyCommand.Path
$rootPath = Split-Path -Parent $MyInvocation.InvocationName
$driver = [io.path]::combine($rootPath,"lib","cron.py")
$interval = Read-Host "每隔多少秒执行一次测试"
$multi = Read-Host "设置并发进程数"
python $driver $interval $multi