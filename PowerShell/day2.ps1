$file = Get-Content Inputs\day2.txt

$horizontal = 0
$depth = 0

foreach ($line in $file) {
    $linesplit = $line.Split()

    if($linesplit[0] -eq 'forward'){
        $horizontal += [int]$linesplit[1]
    }
    elseif($linesplit[0] -eq 'down'){
        $depth += [int]$linesplit[1]
    }
    elseif($linesplit[0] -eq 'up'){
        $depth -= [int]$linesplit[1]
    }
}

Write-Output 'horizontal: '  $horizontal
Write-Output 'depth: '  $depth
Write-Output 'first answer: '  ($depth*$horizontal)

$horizontal = 0
$depth = 0
$aim = 0

foreach ($line in $file) {
    $linesplit = $line.Split()

    if($linesplit[0] -eq 'forward'){
        $horizontal += [int]$linesplit[1]
        $depth += [int]$linesplit[1] * $aim
    }
    elseif($linesplit[0] -eq 'down'){
        $aim += [int]$linesplit[1]
    }
    elseif($linesplit[0] -eq 'up'){
        $aim -= [int]$linesplit[1]
    }
}

Write-Output 'horizontal: '  $horizontal
Write-Output 'depth: '  $depth
Write-Output 'aim: '  $aim
Write-Output 'second answer: '  ($depth*$horizontal)
