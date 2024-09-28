<?php

include_once __DIR__ . '/../Custom/Medoo/connect.php';
include_once __DIR__ . '/../Functions/utility.class.php';

class ExternalServerClass 
{
    const SERVER_LINK = "http://127.0.0.1:8001/";
    const SECRET_TOKEN = "SECRET_KEY";
    private $utilityClass;

    public function __construct(UtilityClass $utilityClass) {
        $this->utilityClass = $utilityClass;
    }

    public function startVideoProcessing($data) {
        $data['secret_token'] = self::SECRET_TOKEN;
        $startTask = $this->utilityClass->sendDataToExternalServer(self::SERVER_LINK . "video-processing/", $data);
        return $startTask;
    }

    public function startVideoRerender($data) {
        $data['secret_token'] = self::SECRET_TOKEN;
        $startTask = $this->utilityClass->sendDataToExternalServer(self::SERVER_LINK . "video-rerender/", $data);
        return $startTask;
    }

}