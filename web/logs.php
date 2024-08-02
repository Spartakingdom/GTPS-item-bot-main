<?php
session_start();

$log_file = 'logs.txt';

if (!isset($_SESSION['authenticated'])) {
    header('Location: index.php');
    exit;
}

$logs = '';
if (file_exists($log_file)) {
    $logs = file_get_contents($log_file);
}
?>

<!DOCTYPE html>
<html>
<head>
    <title>Bot Logs</title>
    <link rel="stylesheet" type="text/css" href="static/logs.css">
</head>
<body>
    <div class="container">
        <h1>Bot Logs</h1>
        <div class="logs-container">
            <pre><?= $logs ?></pre>
        </div>
        <a href="index.php"><button class="back-button">Back to Admin Panel</button></a>
    </div>
</body>
</html>
