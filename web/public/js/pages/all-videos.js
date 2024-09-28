document.addEventListener('DOMContentLoaded', function() {
    fetchAllVideos();
});

function fetchAllVideos() {
    fetch('./src/Api/v1.php?getAllVideos')
        .then(response => response.json())
        .then(data => {
            renderVideosTable(data);
            updateStatusIndicator('Completed');
        })
        .catch(error => {
            console.error('Error fetching videos:', error);
            updateStatusIndicator('Error');
            Swal.fire({
                title: 'Error!',
                text: 'Failed to fetch videos. Please try again later.',
                icon: 'error',
                confirmButtonText: 'OK'
            });
        });
}

function renderVideosTable(videos) {
    const tableBody = document.getElementById('videosTableBody');
    tableBody.innerHTML = '';

    videos.forEach(video => {
        const row = document.createElement('tr');
        row.innerHTML = `
            <td class="px-6 py-4 whitespace-nowrap text-sm text-gray-300">${video.videoTitle}</td>
            <td class="px-6 py-4 whitespace-nowrap">
                <span class="px-2 inline-flex text-xs leading-5 font-semibold rounded-full ${getStatusClass(video.status)}">
                    ${video.status}
                </span>
            </td>
            <td class="px-6 py-4 whitespace-nowrap text-sm text-gray-300">${video.created_at}</td>
            <td class="px-6 py-4 whitespace-nowrap flex items-center gap-x-2">
                <div class="border border-[#29333d] rounded-full p-[10px] text-[#e1e5ea] hover:text-[#ffffff] transition-all">
                    <a href="/video?${video.id}">
                        <svg class="w-5 h-5" xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M15 3h6v6"/><path d="M10 14 21 3"/><path d="M18 13v6a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V8a2 2 0 0 1 2-2h6"/></svg>
                    </a>
                </div>
                <div class="border border-[#29333d] rounded-full p-[10px] text-[#ff4343] hover:text-[#ff6565] transition-all h-[42px]">
                    <button type="button" onclick="deleteVideo('${video.id}')">
                        <svg class="w-5 h-5" xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M3 6h18"/><path d="M19 6v14c0 1-1 2-2 2H7c-1 0-2-1-2-2V6"/><path d="M8 6V4c0-1 1-2 2-2h4c1 0 2 1 2 2v2"/><line x1="10" x2="10" y1="11" y2="17"/><line x1="14" x2="14" y1="11" y2="17"/></svg>
                    </button>
                </div>
            </td>
        `;
        tableBody.appendChild(row);
    });
}

function getStatusClass(status) {
    switch(status) {
        case 'Processing':
            return 'bg-[#2a2b1c] text-[#f5e65b]';
        case 'Completed':
            return 'bg-[#353f26] text-[#b0ff6c]';
        case 'Error':
            return 'bg-[#2b1c1c] text-[#f55b5b]';
        default:
            return 'bg-gray-200 text-gray-800';
    }
}

function updateStatusIndicator(status) {
    const indicator = document.querySelector('.status-indicator');
    indicator.textContent = status;
    indicator.className = `status-indicator px-2 py-1 text-xs font-medium rounded-full ${getStatusClass(status)}`;
}

function deleteVideo(videoId) {
    Swal.fire({
        title: 'Are you sure?',
        text: "You won't be able to revert this!",
        icon: 'warning',
        showCancelButton: true,
        confirmButtonColor: '#3085d6',
        cancelButtonColor: '#d33',
        confirmButtonText: 'Yes, delete it!'
    }).then((result) => {
        if (result.isConfirmed) {
            Swal.fire({
                title: 'Deleting...',
                text: 'Please wait while we delete the video.',
                allowOutsideClick: false,
                showConfirmButton: false,
                willOpen: () => {
                    Swal.showLoading();
                }
            });

            fetch(`./src/Api/v1.php?deleteVideo=${videoId}`, { method: 'DELETE' })
                .then(response => response.json())
                .then(data => {
                    if (data.status === 'success') {
                        Swal.fire(
                            'Deleted!',
                            'The video has been deleted.',
                            'success'
                        ).then(() => {
                            fetchAllVideos();
                        });
                    } else {
                        Swal.fire(
                            'Error!',
                            'Failed to delete video: ' + data.message,
                            'error'
                        );
                    }
                })
                .catch(error => {
                    console.error('Error deleting video:', error);
                    Swal.fire(
                        'Error!',
                        'An error occurred while deleting the video',
                        'error'
                    );
                });
        }
    });
}