<?php
$templates = new Templates();

$templates->documentHead("Dashboard");
?>
<body class="bg-[#14191f]">
    <?php $templates->rutubeTopbar(); ?>
    <main class="container mx-auto px-4 py-8">
        <div class="bg-[#1c232b] rounded-[10px] md:p-8 p-6">
            <h2 class="md:text-2xl text-xl font-medium text-[#ffffff] mb-6 flex items-center justify-between">
                <span>Dashboard</span>
            </h2>
            <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4 gap-6 dashboard-container"> </div>
        </div>
    </main>
    <?php
    $templates->documentJavascript("Dashboard");
    ?>
</body>
</html>