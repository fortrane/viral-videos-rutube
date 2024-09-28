<?php
$templates = new Templates();

$templates->documentHead("Video");
?>
<body class="bg-[#14191f]">
    <?php $templates->rutubeTopbar(); ?>
    <main class="container mx-auto px-4 py-8">
        <div id="alertBanner" class="bg-gray-800 text-white p-6 rounded-lg shadow-lg mb-4">
            <div class="relative">
                <button id="closeAlert" class="absolute top-0 right-0 text-white hover:text-gray-300">
                <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" viewBox="0 0 20 20" fill="currentColor">
                    <path fill-rule="evenodd" d="M4.293 4.293a1 1 0 011.414 0L10 8.586l4.293-4.293a1 1 0 111.414 1.414L11.414 10l4.293 4.293a1 1 0 01-1.414 1.414L10 11.414l-4.293 4.293a1 1 0 01-1.414-1.414L8.586 10 4.293 5.707a1 1 0 010-1.414z" clip-rule="evenodd" />
                </svg>
                </button>
                <p class="text-sm w-[97%]">
                После загрузки видео на Frontend сервер начнется его загрузка на ML сервер, потом обработка ML-скриптом. Время обработки отсчитывается с момента завершения полной загрузки. По окончании вы получите набор виральных видеофрагментов. Для редактирования фрагмента кликните на слово в транскрипции, измените его и нажмите кнопку "Re-render Fragment". Процесс запустится заново. Следите за статусом выполнения.
                </p>
            </div>
        </div>
        <div class="grid grid-cols-1 lg:grid-cols-12 gap-8">
            <aside class="lg:col-span-4 space-y-4 bg-[#1c232b] rounded-[10px] px-5 py-4">
                <h2 class="text-xl font-medium text-[#ffffff] mb-4 flex items-center gap-x-2">Video Fragments <span class="status-indicator px-2 py-1 text-xs font-medium rounded-full"></span></h2>
                <div class="space-y-4 max-h-[250px] md:max-h-[500px] overflow-y-auto"></div>
            </aside>

            <div class="lg:col-span-4 flex flex-col items-center">
                <h2 class="text-xl font-bold mb-4 text-[#ffffff] video-full-title">Loading...</h2>
                <div class="w-full max-w-[450px] mb-4">
                    <div class="relative flex items-center justify-center">
                        <video class="rounded-lg video-fragment-file" controls>
                            <source src="#" type="video/mp4">
                        </video>
                    </div>
                </div>
                <div class="flex justify-center w-full space-x-4 mb-4">
                    <button class="bg-[#00a1e7] text-[#ffffff] text-[14px] py-[11px] px-[16px] rounded-[6px] font-medium hover:bg-[#1eabe9] transition-all export-video-button" data-video-id="" data-video-uuid="">
                        Export
                    </button>
                    <button class="bg-[#00e7a3] text-[#ffffff] text-[14px] py-[11px] px-[16px] rounded-[6px] font-medium hover:bg-[#02ffb5] transition-all rerender-fragment-button" data-video-id="" data-video-uuid="">
                        Re-render Fragment
                    </button>
                </div>
            </div>

            <aside class="lg:col-span-4 space-y-4 rounded-[10px] px-5 py-4 bg-[#1c232b]">
                <h3 class="text-xl font-medium text-[#ffffff] video-fragment-title">Loading...</h3>
                <div class="p-4 bg-[#00a1e73d] rounded-[10px]">
                    <div class="flex items-center justify-between mb-2">
                        <div class="flex items-center gap-x-2">
                            <div>
                                <svg class="h-4 w-4 text-[#ffffff]" xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M9.937 15.5A2 2 0 0 0 8.5 14.063l-6.135-1.582a.5.5 0 0 1 0-.962L8.5 9.936A2 2 0 0 0 9.937 8.5l1.582-6.135a.5.5 0 0 1 .963 0L14.063 8.5A2 2 0 0 0 15.5 9.937l6.135 1.581a.5.5 0 0 1 0 .964L15.5 14.063a2 2 0 0 0-1.437 1.437l-1.582 6.135a.5.5 0 0 1-.963 0z"></path><path d="M20 3v4"></path><path d="M22 5h-4"></path><path d="M4 17v2"></path><path d="M5 18H3"></path></svg>
                            </div>
                            <div>
                                <h2 class="text-[17px] font-medium text-[#ffffff]">Viral Score</h2>
                            </div>
                        </div>
                        <div>
                            <h2 class="text-[16px] font-medium text-[#ffffff]"><span class="text-[20px] viral-score">0</span>/10</h2>
                        </div>
                    </div>
                    <div>
                        <p class="text-[14px] font-normal opacity-80 text-[#ffffff] viral-description"></p>
                    </div>
                </div>

                <div>
                    <h3 class="text-lg font-medium text-[#ffffff]">Video Tags</h3>
                    <p class="text-[14px] font-normal opacity-80 text-[#ffffff] video-fragment-tags"></p>
                </div>

                <div>
                    <h3 class="text-lg font-medium text-[#ffffff] mb-2">Transcription</h3>
                    <textarea class="w-full h-32 bg-gray-800 rounded px-3 py-3 text-[13px] outline-none text-[#ffffff] video-fragment-transcription" placeholder="Transcript goes here..."></textarea>
                </div>
            </aside>
        </div>
    </main>
    <?php
    $templates->documentJavascript("Video");
    ?>
</body>
</html>