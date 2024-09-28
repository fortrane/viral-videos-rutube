<?php

include_once __DIR__ . '/../Custom/Medoo/connect.php';
include_once __DIR__ . '/../Functions/utility.class.php';
include_once __DIR__ . '/../Functions/external.class.php';

@session_start();

$utilityClass = new UtilityClass();
$externalServerClass = new ExternalServerClass($utilityClass);

$secretKey = "SECRET_KEY";

if(isset($_GET["updateVideoData"])) {
    if($_POST["secret-key"] == $secretKey) {
        $videoId = $_POST["id"];
        $videoJson = $_POST["video_json"];
        $metricScore = $_POST["metric_score"];
        $status = $_POST["status"];

        $updateResult = $database->update("rutube_videos", [
            "video_json" => $videoJson,
            "metric_score" => $metricScore,
            "status" => $status
        ], [
            "id" => $videoId
        ]);

        if ($updateResult->rowCount() > 0) {
            echo json_encode(["status" => "success", "message" => "Data updated successfully"]);
        } else {
            echo json_encode(["status" => "error", "message" => "Failed to update video data"]);
        }
    } else {
        echo json_encode(['response' => 'error', 'message' => 'Not allowed']);
    }
}

if(isset($_GET["updateVideoFragment"])) {
    if($_POST["secret-key"] == $secretKey) {
        $videoId = $_POST["id"];
        $fragmentUuid = $_POST["uuid"];
        $videoLink = $_POST["video_link"];
        $status = $_POST["status"];

        $videoData = $database->get("rutube_videos", [
            "id",
            "video_json",
            "status"
        ], [
            "id" => $videoId
        ]);

        if (!$videoData) {
            exit(json_encode(["status" => "error", "message" => "Video not found"]));
        }

        $fragments = json_decode($videoData["video_json"], true);
    
        foreach ($fragments as &$fragment) {
            if ($fragment["uuid"] === $fragmentUuid) {
                $fragment["videoLink"] = $videoLink;
                break;
            }
        }

        $updateResult = $database->update("rutube_videos", [
            "video_json" => json_encode($fragments),
            "status" => $status
        ], [
            "id" => $videoId
        ]);

        if ($updateResult->rowCount() > 0) {
            echo json_encode(["status" => "success", "message" => "Fragment updated successfully"]);
        } else {
            echo json_encode(["status" => "error", "message" => "Failed to update fragment data"]);
        }
    } else {
        echo json_encode(['response' => 'error', 'message' => 'Not allowed']);
    }
}