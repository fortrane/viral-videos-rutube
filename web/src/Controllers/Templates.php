<?php

class Templates
{
    public function documentHead($pageName) {
        ?>
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Генерация виральных клипов | <?=$pageName;?></title>
            <link rel="icon" sizes="16x16" type="image/x-icon" href="./public/img/favicon.ico">
            <script src="https://cdn.tailwindcss.com"></script>
            <link rel="preconnect" href="https://fonts.googleapis.com">
            <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
            <link href="https://fonts.googleapis.com/css2?family=Open+Sans:ital,wght@0,300..800;1,300..800&display=swap" rel="stylesheet">
            <link rel="stylesheet" href="./public/css/rutube.bundle.css">
            <?php
            switch ($pageName) {
                case 'Upload':
                    ?>
                    <link href="./public/css/plugins/dark.min.css" rel="stylesheet">
                    <link href="./public/css/plugins/dropzone.min.css" rel="stylesheet">
                    <?
                    break;

                case 'All Videos':
                    ?>
                    <link href="./public/css/plugins/dark.min.css" rel="stylesheet">
                    <?
                    break;

                default:
                    ?> <?
                    break;
            }
            ?>
        </head>
        <?
    }

    public function documentJavascript($pageName) {
        ?>
        <script src="./public/js/plugins/jquery-3.7.1.min.js"></script>
        <script src="./public/js/main.js"></script>
        <?php

        switch ($pageName) {
            case 'Upload':
                ?>
                <script src="https://unpkg.com/@popperjs/core@2"></script>
                <script src="https://unpkg.com/tippy.js@6"></script>
                <script src="./public/js/plugins/dropzone.min.js"></script>
                <script src="./public/js/plugins/sweetalert.js"></script>
                <script src="./public/js/pages/upload.js"></script>
                <?
                break;

            case 'Video':
                ?>
                <script src="./public/js/pages/video.js"></script>
                <?
                break;

            case 'All Videos':
                ?>
                <script src="./public/js/plugins/sweetalert.js"></script>
                <script src="./public/js/pages/all-videos.js"></script>
                <?
                break;

            case 'Dashboard':
                ?>
                <script src="./public/js/pages/dashboard.js"></script>
                <?
                break;

            default:
                ?> <?
                break;
        }
    }

    public function rutubeTopbar() {
        ?>
<header class="bg-[#1c232b] mb-8">
        <div class="flex items-center justify-between lg:px-20 sm:px-8 px-4 py-3">
            <div>
                <a href="/">
                    <svg class="w-[148px] h-[40px] fill-[#ffffff] cursor-pointer" viewBox="0 0 125 25" fill="none" xmlns="http://www.w3.org/2000/svg"><path d="M13.9025 6H0V21H3.86952V16.1199H11.2841L14.6671 21H19L15.2695 16.0975C16.4281 15.9176 17.2622 15.4903 17.772 14.8156C18.2817 14.141 18.5366 13.0615 18.5366 11.6222V10.4978C18.5366 9.64318 18.444 8.96855 18.2817 8.45125C18.1195 7.93403 17.8415 7.48425 17.4476 7.07946C17.0305 6.69715 16.5671 6.42729 16.011 6.24737C15.4549 6.08995 14.7597 6 13.9025 6ZM13.2769 12.8141H3.86952V9.30582H13.2769C13.8098 9.30582 14.1805 9.3958 14.3659 9.55321C14.5512 9.71062 14.6671 10.003 14.6671 10.4303V11.6897C14.6671 12.1395 14.5512 12.4318 14.3659 12.5892C14.1805 12.7466 13.8098 12.8141 13.2769 12.8141Z"></path><path d="M24.7575 16.5697V6H21V16.4798C21 17.3343 21.0675 18.0315 21.225 18.5487C21.3825 19.0885 21.6525 19.5382 22.0575 19.9206C22.44 20.3254 22.89 20.5952 23.43 20.7526C23.97 20.9326 24.645 21 25.5 21H34.5C35.3325 21 36.0075 20.9326 36.5475 20.7526C37.0875 20.5952 37.5375 20.3254 37.9425 19.9206C38.325 19.5382 38.595 19.0885 38.7525 18.5487C38.9101 18.0315 39 17.3343 39 16.4798V6H35.2425V16.5697C35.2425 17.0195 35.13 17.3119 34.95 17.4693C34.77 17.6267 34.41 17.6941 33.8925 17.6941H26.1075C25.5675 17.6941 25.2075 17.6267 25.0275 17.4693C24.8475 17.3119 24.7575 17.0195 24.7575 16.5697Z"></path><path d="M51.8487 21V9.30582H59V6H41V9.30582H48.1512V21H51.8487Z"></path><path d="M64.7575 16.5697V6H61V16.4798C61 17.3343 61.0676 18.0315 61.225 18.5487C61.3825 19.0885 61.6525 19.5382 62.0575 19.9206C62.44 20.3254 62.89 20.5952 63.43 20.7526C63.97 20.9326 64.645 21 65.5 21H74.5C75.3325 21 76.0075 20.9326 76.5475 20.7526C77.0875 20.5952 77.5375 20.3254 77.9425 19.9206C78.325 19.5382 78.595 19.0885 78.7525 18.5487C78.91 18.0315 79 17.3343 79 16.4798V6H75.2425V16.5697C75.2425 17.0195 75.13 17.3119 74.95 17.4693C74.7699 17.6267 74.41 17.6941 73.8925 17.6941H66.1075C65.5675 17.6941 65.2075 17.6267 65.0275 17.4693C64.8475 17.3119 64.7575 17.0195 64.7575 16.5697Z"></path><path d="M98.2567 10.3628V10.0705C98.2567 8.67618 97.8964 7.64168 97.1749 6.98951C96.4541 6.33733 95.3054 6 93.7737 6H81V21H94.5169C96.0486 21 97.1974 20.6852 97.9189 20.033C98.6397 19.3808 99 18.3463 99 16.9521V16.6372C99 15.2429 98.6397 14.2534 97.9189 13.6687C97.7835 13.5787 97.6481 13.5112 97.5134 13.4438C97.378 13.3763 97.1749 13.2864 96.9274 13.1964C97.4231 12.9265 97.7609 12.5667 97.9633 12.1619C98.1439 11.7571 98.2567 11.1499 98.2567 10.3628ZM84.7624 12.0045V9.30582H93.165C93.7059 9.30582 94.0663 9.3958 94.2469 9.55321C94.4266 9.71062 94.5169 10.003 94.5169 10.4303V10.8801C94.5169 11.3299 94.4266 11.6222 94.2469 11.7796C94.0663 11.9371 93.7059 12.0045 93.165 12.0045H84.7624ZM84.7624 17.6941V14.9955H93.9309C94.4492 14.9955 94.8096 15.0854 94.9901 15.2429C95.1699 15.4003 95.2828 15.6927 95.2828 16.1199V16.5697C95.2828 17.0195 95.1699 17.3119 94.9901 17.4693C94.8096 17.6267 94.4492 17.6941 93.9309 17.6941H84.7624Z"></path><path d="M104.837 9.30582H117.38V6H101V21H118V17.6941H104.837V15.153H117.081L117.38 11.8471H104.837V9.30582Z"></path><path d="M121.682 5.25234C123.128 5.25234 124.301 4.07656 124.301 2.62617C124.301 1.17578 123.128 0 121.682 0C120.235 0 119.062 1.17578 119.062 2.62617C119.062 4.07656 120.235 5.25234 121.682 5.25234Z" fill="#F41240"></path></svg>
                </a>
            </div>
            <div class="flex items-center gap-x-3">
                <div>
                    <a href="/" class="flex items-center justify-center bg-[#00a1e7] text-[#ffffff] text-[12px] sm:py-[11px] sm:px-[16px] p-2 rounded-[6px] font-medium hover:bg-[#1eabe9] transition-all">
                        <span class="sm:block hidden">Upload</span>
                        <svg class="sm:hidden block w-4 h-4" xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"/><polyline points="17 8 12 3 7 8"/><line x1="12" x2="12" y1="3" y2="15"/></svg>
                    </a>
                </div>
                <div>
                    <a href="/all-videos" class="flex items-center justify-center bg-[#00a1e7] text-[#ffffff] text-[12px] sm:py-[11px] sm:px-[16px] p-2 rounded-[6px] font-medium hover:bg-[#1eabe9] transition-all">
                        <span class="sm:block hidden">All Videos</span>
                        <svg class="sm:hidden block w-4 h-4" xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 12H3"/><path d="M16 6H3"/><path d="M12 18H3"/><path d="m16 12 5 3-5 3v-6Z"/></svg>
                    </a>
                </div>
                <div>
                    <a href="/dashboard" class="flex items-center justify-center bg-[#00a1e7] text-[#ffffff] text-[12px] sm:py-[11px] sm:px-[16px] p-2 rounded-[6px] font-medium hover:bg-[#1eabe9] transition-all">
                        <span class="sm:block hidden">Dashboard</span>
                        <svg class="sm:hidden block w-4 h-4" xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect width="7" height="9" x="3" y="3" rx="1"/><rect width="7" height="5" x="14" y="3" rx="1"/><rect width="7" height="9" x="14" y="12" rx="1"/><rect width="7" height="5" x="3" y="16" rx="1"/></svg>
                    </a>
                </div>
            </div>
        </div>
    </header>
        <?
    }

}

