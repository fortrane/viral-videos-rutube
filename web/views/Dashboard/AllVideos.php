<?php
$templates = new Templates();

$templates->documentHead("All Videos");
?>
<body class="bg-[#14191f]">
    <?php $templates->rutubeTopbar(); ?>
    <main class="container mx-auto px-4 py-8">
        <div class="bg-[#1c232b] rounded-[10px] md:p-8 p-6">
            <h2 class="md:text-2xl text-xl font-medium text-[#ffffff] mb-4 flex items-center justify-between">
                <span>All Videos</span>
                <span class="status-indicator px-2 py-1 text-xs font-medium rounded-full bg-blue-200 text-blue-800">Loading...</span>
            </h2>
            <div class="overflow-x-auto">
                <table class="min-w-full divide-y divide-gray-700">
                    <thead class="bg-gray-800">
                        <tr>
                            <th scope="col" class="px-6 py-3 text-left text-xs font-medium text-gray-300 uppercase tracking-wider">Title</th>
                            <th scope="col" class="px-6 py-3 text-left text-xs font-medium text-gray-300 uppercase tracking-wider">Status</th>
                            <th scope="col" class="px-6 py-3 text-left text-xs font-medium text-gray-300 uppercase tracking-wider">Created At</th>
                            <th scope="col" class="px-6 py-3 text-left text-xs font-medium text-gray-300 uppercase tracking-wider">Actions</th>
                        </tr>
                    </thead>
                    <tbody class="bg-[#1c232b] divide-y divide-gray-700" id="videosTableBody"></tbody>
                </table>
            </div>
        </div>
    </main>
    <?php
    $templates->documentJavascript("All Videos");
    ?>
</body>
</html>