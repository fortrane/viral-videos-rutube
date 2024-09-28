$(document).ready(function() {
    const container = $('.dashboard-container');
    
    function loadVideos() {
        $.getJSON('./src/Api/v1.php?getVideosForDashboard', function(data) {
            const cardsHtml = data.map(createVideoCard).join('');
            container.html(cardsHtml);
            initializeLazyLoading();
        }).fail(function(jqXHR, textStatus, errorThrown) {
            console.error("Ошибка загрузки данных:", textStatus, errorThrown);
        });
    }

    function createVideoCard(video) {
        const sortedMetrics = Object.entries(video.metric_score)
            .sort((a, b) => b[1] - a[1]);

        const thumbnailHtml = `
            <img data-src="${video.thumbnail[0]}" alt="Video Thumbnail" class="lazy absolute inset-0 w-full h-full object-cover current-thumbnail">
        `;

        const metricsHtml = sortedMetrics.map(([key, value]) => `
            <div class="flex justify-between items-center bg-gray-700 rounded-lg p-2">
                <span class="md:text-xs text-[11px] text-gray-400">${formatMetricName(key)}</span>
                <span class="text-lg font-semibold text-[#00a1e7] pl-[3px]">${Math.round(value)}</span>
            </div>
        `).join('');

        return `
            <div class="video-card bg-[#242c36] rounded-lg overflow-hidden shadow-lg" data-thumbnails='${JSON.stringify(video.thumbnail)}'>
                <div class="p-4">
                    <h3 class="text-lg font-semibold text-white mb-2">${video.title}</h3>
                    <div class="relative w-full h-64 mb-4 rounded-lg overflow-hidden thumbnail-container">
                        ${thumbnailHtml}
                        <div class="absolute bottom-2 right-2 bg-black bg-opacity-50 text-white px-2 py-1 rounded text-sm thumbnail-counter">1/${video.thumbnail.length}</div>
                        ${video.thumbnail.length > 1 ? `
                            <div class="absolute top-2 right-2 space-x-2">
                                <button class="bg-black bg-opacity-50 text-white px-2 py-1 rounded text-sm prev-thumbnail">&lt;</button>
                                <button class="bg-black bg-opacity-50 text-white px-2 py-1 rounded text-sm next-thumbnail">&gt;</button>
                            </div>
                        ` : ''}
                    </div>
                    <div class="grid grid-cols-2 gap-2">
                        ${metricsHtml}
                    </div>
                </div>
            </div>
        `;
    }

    function formatMetricName(name) {
        return name.split('_').map(word => word.charAt(0).toUpperCase() + word.slice(1)).join(' ');
    }

    function initializeLazyLoading() {
        $('.lazy').each(function() {
            const img = this;
            const observer = new IntersectionObserver((entries) => {
                entries.forEach(entry => {
                    if (entry.isIntersecting) {
                        img.src = img.dataset.src;
                        img.classList.remove('lazy');
                        observer.unobserve(img);
                    }
                });
            });
            observer.observe(img);
        });
    }

    container.on('click', '.prev-thumbnail, .next-thumbnail', function() {
        const $card = $(this).closest('.video-card');
        const thumbnails = JSON.parse($card.attr('data-thumbnails'));
        const $img = $card.find('img');
        const $counter = $card.find('.thumbnail-counter');
        let currentIndex = thumbnails.indexOf($img.attr('src'));

        if ($(this).hasClass('prev-thumbnail')) {
            currentIndex = (currentIndex - 1 + thumbnails.length) % thumbnails.length;
        } else {
            currentIndex = (currentIndex + 1) % thumbnails.length;
        }

        $img.attr('src', thumbnails[currentIndex]);
        $counter.text(`${currentIndex + 1}/${thumbnails.length}`);
    });

    loadVideos();
});
