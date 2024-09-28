<?php

include_once __DIR__ . '/../Custom/Medoo/connect.php';
include_once __DIR__ . '/../Functions/utility.class.php';
include_once __DIR__ . '/../Functions/external.class.php';

@session_start();

$utilityClass = new UtilityClass();
$externalServerClass = new ExternalServerClass($utilityClass);

if(isset($_GET["getVideo"])) {
    $videoId = $_GET["getVideo"];
    
    $videoData = $database->get("rutube_videos", [
        "id",
        "videoTitle",
        "originalVideo",
        "video_json",
        "status",
        "created_at"
    ], [
        "id" => $videoId
    ]);

    if (!$videoData) {
        exit(json_encode(["status" => "error", "message" => "Video not found"]));
    }

    $response = [
        "id" => $videoData["id"],
        "videoTitle" => $videoData["videoTitle"],
        "originalVideo" => $videoData["originalVideo"],
        "status" => $videoData["status"],
        "created_at" => $videoData["created_at"],
        "fragments" => null
    ];

    if (!empty($videoData["video_json"])) {
        $fragments = json_decode($videoData["video_json"], true);
        if (json_last_error() !== JSON_ERROR_NONE) {
            exit(json_encode(["status" => "error", "message" => json_last_error_msg()]));
        }
        $response["fragments"] = $fragments;
    }

    header('Content-Type: application/json');
    echo json_encode($response);
}

if(isset($_GET["rerenderVideo"])) {
    $videoId = $_POST["id"];
    $fragmentUuid = $_POST["uuid"];
    $transcriptionRaw = $_POST["transcriptionRaw"];
    $transcriptionTimecodes = json_decode($_POST["transcriptionTimecodes"], true);

    $fragmentTitle = "";

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
            $fragment["transcriptionRaw"] = $transcriptionRaw;
            $fragment["transcriptionTimecodes"] = $transcriptionTimecodes;

            $fragmentTitle = $fragment["fragmentTitle"];
            break;
        }
    }

    $updateResult = $database->update("rutube_videos", [
        "video_json" => json_encode($fragments),
        "status" => "Processing"
    ], [
        "id" => $videoId
    ]);

    if ($updateResult->rowCount() > 0) {
        
        $requestData = [
            "identity" => $rowId,
            "uuid" => $uuid,
            "transcription_raw" => $transcriptionRaw,
            "transcription_timecodes" => json_encode($transcriptionTimecodes),
            "fragment_title" => $fragmentTitle,
        ];

        $externalServerClass->startVideoRerender($requestData);

        echo json_encode(["status" => "success", "message" => "Rerender started"]);
    } else {
        echo json_encode(["status" => "error", "message" => "Failed to update video data"]);
    }
}

if(isset($_GET["getAllVideos"])) {
    
    $videosData = $database->select("rutube_videos", [
        "id",
        "videoTitle",
        "status",
        "created_at"
    ], [
        "ORDER" => ["id" => "DESC"]
    ]);

    if (!$videosData) {
        exit(json_encode(["status" => "error", "message" => "Videos not found"]));
    }

    header('Content-Type: application/json');
    echo json_encode($videosData);
}

if(isset($_GET["deleteVideo"])) {
    $videoId = $_GET["deleteVideo"];
    
    $deleteResult = $database->delete("rutube_videos", [
        "id" => $videoId
    ]);

    if ($deleteResult->rowCount() > 0) {
        echo json_encode(["status" => "success", "message" => "Video deleted successfully"]);
    } else {
        echo json_encode(["status" => "error", "message" => "Failed to delete video or video not found"]);
    }
}

if(isset($_GET["uploadVideo"])) {
    $videoTitle = $_POST['videoTitle'] ?? '';
    $addSoapVideo = $_POST['addSoapVideo'] ?? '0';
    $file = $_FILES['file'] ?? null;

    if (!$file) {
        http_response_code(400);
        exit(json_encode(["status" => "error", "message" => "No file uploaded"]));
    }

    $allowedExtensions = ['mp4'];
    $maxFileSize = 400 * 1024 * 1024;

    $fileExtension = strtolower(pathinfo($file['name'], PATHINFO_EXTENSION));
    if (!in_array($fileExtension, $allowedExtensions)) {
        http_response_code(400);
        exit(json_encode(["status" => "error", "message" => "Invalid file format. Only MP4 is allowed."]));
    }

    if ($file['size'] > $maxFileSize) {
        http_response_code(400);
        exit(json_encode(["status" => "error", "message" => "File size exceeds the limit of 400MB"]));
    }

    $randomFileName = uniqid() . '.mp4';
    $uploadPath = __DIR__ . '/../../temp/' . $randomFileName;

    if (move_uploaded_file($file['tmp_name'], $uploadPath)) {
        $fileUrl = $utilityClass->getFullServerUrl() . "/temp/" . $randomFileName;
        
        $insertResult = $database->insert("rutube_videos", [
            "videoTitle" => $videoTitle,
            "originalVideo" => $fileUrl,
            "add_soap_video" => $addSoapVideo,
            "status" => "Processing",
            "created_at" => date("Y-m-d H:i:s")
        ]);

        $rowId = $database->id();

        if ($insertResult->rowCount() > 0) {
            
            $requestData = [
                "identity" => $rowId,
                "original_video" => $fileUrl
            ];
    
            $externalServerClass->startVideoProcessing($requestData);

            echo json_encode(["status" => "success", "message" => "Video uploaded successfully"]);
        } else {
            http_response_code(500);
            echo json_encode(["status" => "error", "message" => "Failed to save video information"]);
        }
    } else {
        http_response_code(500);
        echo json_encode(["status" => "error", "message" => "Failed to upload file"]);
    }
}

if(isset($_GET["getVideosForDashboard"])) {
    
    $videosData = $database->select("rutube_videos", [
    "id",
    "videoTitle",
    "video_json",
    "metric_score",
    "status",
    "created_at"
    ], [
        "AND" => [
            "video_json[!]" => null,
            "metric_score[!]" => null,
            "video_json[!]" => "",
            "metric_score[!]" => ""
        ],
        "ORDER" => ["id" => "DESC"]
    ]);

    if (!$videosData) {
        exit(json_encode(["status" => "error", "message" => "Videos not found"]));
    }

    $formattedVideos = [];

    foreach ($videosData as $video) {
        $videoJson = json_decode($video['video_json'], true);
        $metricScore = json_decode($video['metric_score'], true);

        $thumbnails = [];
        foreach ($videoJson as $fragment) {
            $thumbnails[] = $fragment['thumbnail'];
        }

        $formattedVideos[] = [
            'title' => $video['videoTitle'],
            'thumbnail' => $thumbnails,
            'metric_score' => $metricScore
        ];
    }

    header('Content-Type: application/json');
    echo json_encode($formattedVideos);
}