<?php
session_start();

$config_file = 'config.json';
$config = json_decode(file_get_contents($config_file), true);

$secret = $config['SECRET'];
$base_url = 'http://localhost:5000';

if (isset($_POST['login'])) {
    $entered_secret = $_POST['secret'];
    if ($entered_secret === $secret) {
        $_SESSION['authenticated'] = true;
        header('Location: ' . $_SERVER['PHP_SELF']);
        exit;
    } else {
        $error = "Invalid secret!";
    }
}

if (isset($_POST['action']) && $_SESSION['authenticated']) {
    $action = $_POST['action'];
    $url = "$base_url/$action?secret=$secret";
    $response = file_get_contents($url);
    $status_message = $response;
}

if (isset($_GET['logout'])) {
    session_destroy();
    header('Location: ' . $_SERVER['PHP_SELF']);
    exit;
}

if (!isset($_SESSION['authenticated'])):
?>

<!DOCTYPE html>
<html>
<head>
    <title>GTKY Item Panel Login</title>
    <link rel="stylesheet" type="text/css" href="static/index.css">
</head>
<body>
    <div class="container">
        <h1>GTKY Item Panel Login</h1>
        <?php if (isset($error)): ?>
            <p class="error"><?= $error ?></p>
        <?php endif; ?>
        <form method="post">
            <input type="password" name="secret" placeholder="Enter secret" required>
            <button type="submit" name="login">Login</button>
        </form>
    </div>
</body>
</html>

<?php else: ?>

<!DOCTYPE html>
<html>
<head>
    <title>GTKY Item Panel</title>
    <link rel="stylesheet" type="text/css" href="static/index.css">
</head>
<body>
    <div class="container">
        <h1>GTKY Item Panel</h1>
        <form method="post">
            <button name="action" value="start_bot">Start Bot</button>
            <button name="action" value="stop_bot">Stop Bot</button>
            <button name="action" value="status">Check Status</button>
        </form>
        <?php if (isset($status_message)): ?>
            <p class="status-message"><?= $status_message ?></p>
        <?php endif; ?>
        <form method="post" action="logs.php">
            <button class="logs-button" type="submit">View Logs</button>
        </form>
        <form method="post" action="update_config.php">
            <button class="config-button" type="submit">Update Configuration</button>
        </form>
        <form method="get">
            <button class="logout-button" name="logout">Logout</button>
        </form>
    </div>
</body>
</html>

<?php endif; ?>
