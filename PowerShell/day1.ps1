$file = Get-Content Inputs\day1.txt
$last = 99999
$count = 0
foreach ($line in $file) {
    if($last -lt $line) {
        $count++
    }
    $last = $line
}
Write-Output "first answer:" $count

$count = 0
$num = 0
foreach ($line in $file) {
    $a = [int]$file[$num] + [int]$file[$num+1] + [int]$file[$num+2]
    $b = [int]$file[$num+1] + [int]$file[$num+2] + [int]$file[$num+3]
    if($a -lt $b) {
        $count++
    }
    $num++
}

Write-Output "second answer:" $count
