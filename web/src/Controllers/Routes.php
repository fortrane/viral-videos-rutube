<?php

class Routes {

    public $database;

    public function __construct($database) {
        $request = parse_url($_SERVER['REQUEST_URI'], PHP_URL_PATH);

        $this->database = $database;
        $this->routeUserTo($request);

    }

    public function routeUserTo($request) {

        $viewDir = __DIR__ . '/../../views/';

        $utilityClass = new UtilityClass();

        switch ($request) {
            case '':
            case '/':
                $utilityClass->checkSessions("defaultAccess", $this->database);
                require $viewDir . 'Dashboard/Upload.php';
                break;
            
            case '/video':
                $utilityClass->checkSessions("defaultAccess", $this->database);
                require $viewDir . 'Dashboard/Video.php';
                break;

            case '/all-videos':
                $utilityClass->checkSessions("defaultAccess", $this->database);
                require $viewDir . 'Dashboard/AllVideos.php';
                break;

            case '/dashboard':
                $utilityClass->checkSessions("defaultAccess", $this->database);
                require $viewDir . 'Dashboard/Dashboard.php';
                break;

        
            default:
                http_response_code(404);
                break;
        }
    }

}




