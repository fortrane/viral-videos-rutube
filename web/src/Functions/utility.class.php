<?php

class UtilityClass
{
    public function sanitizeParam($param) {
        $param = strip_tags(htmlspecialchars(trim($param)));
        return $param;
    }

    public function addNotification($title, $text, $type) {
        ?><script>addNotification("<?=$title;?>", "<?=$text;?>", "<?=$type;?>");</script><?
    }

    public function addJavaScript($param) {
        ?><script><?=$param;?></script><?
    }

    public function addCSS($param) {
        ?><style><?=$param;?></style><?
    }

    public function changeLocationViaHTML($time, $link) {
        ?>
        <script>
        setTimeout(function() {
          window.location.href = "<?=$link;?>";
        }, <?=$time;?>);
        </script>
        <meta http-equiv="refresh" content="<?=$time;?>;URL=<?=$link;?>" />
        <?
    }

    public function checkSessions($permissions, $database, $uuid = null) {

        if($permissions == "defaultAccess") {
            if(!empty($_SESSION['id'])) {
                exit($this->changeLocationViaHTML('0', './dashboard'));
            }
        }

    }

    public function id() {
        return $_SESSION['id'];
    }

    public function getUsersAccessType() {
        return $_SESSION["role"];
    }

    public function getCurrentDateTime() {
        return date('d.m.Y H:i:s');
    }

    public function getCurrentTimeStamp() {
        return time();
    }

    public function getFullServerUrl() {
        $connectionType = 'http';
        if (isset($_SERVER['HTTPS']) && $_SERVER['HTTPS'] === 'on') {
            $connectionType = 'https';
        }

        $serverName = $_SERVER['SERVER_NAME'];

        $port = $_SERVER['SERVER_PORT'];
        $portPart = '';
        if (($connectionType === 'http' && $port != 80) || ($connectionType === 'https' && $port != 443)) {
            $portPart = ':' . $port;
        }

        return $connectionType . '://' . $serverName . $portPart;
    }

    public function extractValueFromJson($jsonString, $key) {
        $data = json_decode($jsonString, true);
    
        if (isset($data[$key])) {
            return $data[$key];
        } else {
            return "N/A";
        }
    }

    public function sendDataToExternalServer($url, $data) {
        $url = $url . '?' . http_build_query($data);
    
        $ch = curl_init();
        curl_setopt($ch, CURLOPT_URL, $url);
        curl_setopt($ch, CURLOPT_POST, true);
        curl_setopt($ch, CURLOPT_POSTFIELDS, '');
        curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
        curl_setopt($ch, CURLOPT_HEADER, true);
        
        curl_setopt($ch, CURLOPT_HTTPHEADER, [
            'Accept: application/json',
            'Content-Type: application/json'
        ]);
    
        $response = curl_exec($ch);
        curl_close($ch);
    
        return $response;
    }

    public function fetchDataFromExternalServer($url) {
        $ch = curl_init();
        curl_setopt($ch, CURLOPT_URL, $url);
        curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
        curl_setopt($ch, CURLOPT_HEADER, false);
        $response = curl_exec($ch);
        curl_close($ch);

        return $response;
    }
    

}