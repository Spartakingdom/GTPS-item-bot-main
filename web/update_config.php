<?php
session_start();

$config_file = 'config.json';
$config = json_decode(file_get_contents($config_file), true);

$secret = $config['SECRET'];
$base_url = 'http://localhost:5000';

if (!isset($_SESSION['authenticated'])) {
    header('Location: index.php');
    exit;
}

if (isset($_POST['update_config'])) {
    $update_url = "$base_url/update_config";
    $data = [
        'secret' => $secret,
        'bot_token' => $_POST['bot_token'],
        'items_url' => $_POST['items_url'],
        'developer_id' => $_POST['developer_id']
    ];
    $options = [
        'http' => [
            'header' => "Content-Type: application/x-www-form-urlencoded\r\n",
            'method' => 'POST',
            'content' => http_build_query($data)
        ]
    ];
    $context = stream_context_create($options);
    $result = file_get_contents($update_url, false, $context);
    $status_message = $result;
}
?>

<!DOCTYPE html>
<html>
<head>
    <title>Update Configuration</title>
    <link rel="stylesheet" type="text/css" href="static/update_config.css">
</head>
<body>
    <div class="container">
        <h1>Update Configuration</h1>
        <?php if (isset($status_message)): ?>
            <p class="status-message"><?= $status_message ?></p>
        <?php endif; ?>
        <form method="post">
            <label for="bot_token">BOT_TOKEN</label>
            <input type="text" id="bot_token" name="bot_token" placeholder="BOT_TOKEN" value="<?= $config['BOT_TOKEN'] ?>" required>
            <label for="items_url">ITEMS_URL</label>
            <input type="text" id="items_url" name="items_url" placeholder="ITEMS_URL" value="<?= $config['ITEMS_URL'] ?>" required>
            <label for="developer_id">DEVELOPER_ID</label>
            <input type="text" id="developer_id" name="developer_id" placeholder="DEVELOPER_ID" value="<?= $config['DEVELOPER_ID'] ?>" required>
            <button type="submit" name="update_config">Update Config</button>
        </form>
        <a href="index.php"><button class="back-button">Back to Admin Panel</button></a>
    </div>
</body>
</html>
