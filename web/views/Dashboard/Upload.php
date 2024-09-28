<?php
$templates = new Templates();

$templates->documentHead("Upload");
?>
<body class="bg-[#14191f]">
    <?php $templates->rutubeTopbar(); ?>
    <main class="container mx-auto px-4 py-8">
        <div class="bg-[#1c232b] rounded-[10px] md:p-8 p-6">
            <h2 class="md:text-2xl text-xl font-medium text-[#ffffff] mb-4 flex items-center justify-between">
                <span>Upload Video</span>
            </h2>
            <div class="space-y-6">
                <div>
                    <label for="videoTitle" class="block text-sm font-medium text-gray-300 mb-2">Video Title</label>
                    <input type="text" name="videoTitle" class="video-title-input bg-[#242c36] text-white w-full px-4 py-2 rounded-md focus:outline-none focus:ring-2 focus:ring-[#00a1e7]" placeholder="Enter video title">
                </div>
                <div class="flex items-center mt-4">
                    <div class="relative inline-block w-12 mr-2 align-middle select-none transition duration-200 ease-in">
                        <input type="checkbox" id="addVideoSoap" name="addVideoSoap" class="toggle-checkbox absolute block w-6 h-6 rounded-full bg-white border-4 border-gray-700 appearance-none cursor-pointer transition-transform duration-200 ease-in-out transform translate-x-0 checked:translate-x-full checked:border-[#00a1e7]"/>
                        <label for="addVideoSoap" class="toggle-label block overflow-hidden h-6 rounded-full bg-gray-700 cursor-pointer transition-colors duration-200 ease-in-out"></label>
                    </div>
                    <label for="addVideoSoap" class="text-sm font-medium text-gray-300 cursor-pointer select-none">Add Video Soap</label>
                    <div class="soap-tooltip ml-1 mb-[4px] cursor-pointer hover:opacity-80 transition-all">
                        <svg class="w-5 h-5 text-[#e1e5ea]" xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"/><path d="M9.09 9a3 3 0 0 1 5.83 1c0 2-3 3-3 3"/><path d="M12 17h.01"/></svg>
                    </div>
                </div>
                <div class="video-dropzone bg-[#242c36] border-2 border-dashed border-gray-500 rounded-lg p-6 flex flex-col items-center justify-center cursor-pointer">
                    <svg class="w-12 h-12 text-gray-400 mb-4" fill="none" stroke="currentColor" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">
                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M7 16a4 4 0 01-.88-7.903A5 5 0 1115.9 6L16 6a5 5 0 011 9.9M15 13l-3-3m0 0l-3 3m3-3v12"></path>
                    </svg>
                    <p class="text-gray-400 text-center">Drag and drop your video here, or click to select</p>
                    <p class="text-gray-500 text-sm mt-2">Max file size: 400MB, Format: .mp4</p>
                </div>
                <div class="upload-progress hidden">
                    <div class="bg-[#242c36] rounded-full h-4 overflow-hidden">
                        <div class="progress-bar bg-[#00a1e7] h-full w-0 transition-all duration-300"></div>
                    </div>
                    <p class="text-gray-400 text-md mt-2 text-center progress-text">0%</p>
                </div>
                <button type="button" class="upload-button bg-[#00a1e7] text-white px-4 py-2 rounded-md hover:bg-[#1eabe9] transition-colors w-full">Upload Video</button>
            </div>
        </div>
    </main>
    <?php
    $templates->documentJavascript("Upload");
    ?>
</body>
</html>