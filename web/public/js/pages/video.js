let videoData = null;
let currentStatus = null;
let statusCheckInterval = null;

document.addEventListener('DOMContentLoaded', function() {
    const path = window.location.pathname;
    const query = window.location.search;

    if (path === '/video' && query.startsWith('?')) {
        const videoId = query.substring(1);
        if (videoId) {
            fetchVideoData(videoId);
            startStatusCheck(videoId);
        }
    }

    document.addEventListener('click', handleGlobalClick);

    const closeButton = document.getElementById('closeAlert');
    const alertBanner = document.getElementById('alertBanner');

    if (closeButton && alertBanner) {
        closeButton.addEventListener('click', function() {
        alertBanner.style.display = 'none';
        });
    }
});

function handleGlobalClick(e) {
    if (e.target.closest('.select-video')) {
        const videoUuid = e.target.closest('.select-video').dataset.videoUuid;
        selectVideoFragment(videoUuid);
    } else if (e.target.closest('.export-video-button')) {
        const button = e.target.closest('.export-video-button');
        exportVideo(button.dataset.videoId, button.dataset.videoUuid);
    } else if (e.target.closest('.rerender-fragment-button')) {
        const button = e.target.closest('.rerender-fragment-button');
        rerenderFragment(button.dataset.videoId, button.dataset.videoUuid);
    }
}

function fetchVideoData(videoId) {
    fetch(`./src/Api/v1.php?getVideo=${videoId}`)
        .then(response => response.json())
        .then(data => {
            if (data.status === "error") {
                console.error(data.message);
                return;
            }
            videoData = data;
            rerenderPage();
            updateVideoStatus(data.status);
        })
        .catch(error => console.error('Error:', error));
}

function renderVideoData(data) {
    const fragmentList = document.querySelector('.lg\\:col-span-4 .space-y-4');
    fragmentList.innerHTML = ''; 

    if (data.fragments === null) {
        fragmentList.innerHTML = '<p class="text-[#ffffff] opacity-80">No fragments available</p>';
        updateButtonState(false);
    } else {
        data.fragments.forEach((fragment, index) => {
            const fragmentHtml = `
                <div class="flex space-x-2 relative w-full cursor-pointer transition-all p-2 hover:bg-[#242c36] rounded-[10px] data-[selected=true]:bg-[#242c36] select-video" data-selected="${index === 0}" data-video-uuid="${fragment.uuid}">
                    <div class="relative w-20 h-20 flex-shrink-0">
                        <img src="${fragment.thumbnail}" class="w-20 h-20 object-cover rounded border border-[#ffffffb5] video-fragment-thumbnail">
                        <div class="absolute flex items-center gap-x-1 top-1 left-1 bg-[#000000] bg-opacity-50 rounded-full py-1 px-1.5">
                            <svg class="h-3 w-3 text-[#ffffff]" xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M9.937 15.5A2 2 0 0 0 8.5 14.063l-6.135-1.582a.5.5 0 0 1 0-.962L8.5 9.936A2 2 0 0 0 9.937 8.5l1.582-6.135a.5.5 0 0 1 .963 0L14.063 8.5A2 2 0 0 0 15.5 9.937l6.135 1.581a.5.5 0 0 1 0 .964L15.5 14.063a2 2 0 0 0-1.437 1.437l-1.582 6.135a.5.5 0 0 1-.963 0z"/><path d="M20 3v4"/><path d="M22 5h-4"/><path d="M4 17v2"/><path d="M5 18H3"/></svg>
                            <span class="text-[#ffffff] text-[12px]">${fragment.viralScore}</span>
                        </div>
                    </div>
                    <div class="flex flex-col justify-between py-0.5 pl-1">
                        <h3 class="text-sm text-[#ffffff] font-semibold leading-tight">${fragment.fragmentTitle}</h3>
                        <p class="text-xs text-[#ffffff] opacity-80">${fragment.duration}</p>
                    </div>
                </div>
            `;
            fragmentList.innerHTML += fragmentHtml;
        });
        updateButtonState(true);
    }

    document.querySelector('.video-full-title').textContent = data.videoTitle;
    
    const videoPlayer = document.querySelector('.video-fragment-file');
    videoPlayer.src = data.originalVideo;
    videoPlayer.load();

    const exportButtons = document.querySelectorAll('.export-video-button');
    const rerenderButtons = document.querySelectorAll('.rerender-fragment-button');
    exportButtons.forEach(button => {
        button.dataset.videoId = data.id;
        button.dataset.videoUuid = data.fragments && data.fragments.length > 0 ? data.fragments[0].uuid : '';
    });
    rerenderButtons.forEach(button => {
        button.dataset.videoId = data.id;
        button.dataset.videoUuid = data.fragments && data.fragments.length > 0 ? data.fragments[0].uuid : '';
    });

    if (data.fragments && data.fragments.length > 0) {
        updateFragmentInfo(data.fragments[0]);
    } else {
        clearFragmentInfo();
    }
}

function updateButtonState(enabled) {
    const buttons = document.querySelectorAll('.export-video-button, .rerender-fragment-button');
    buttons.forEach(button => {
        if (enabled) {
            button.disabled = false;
            button.classList.remove('opacity-50', 'cursor-not-allowed');
        } else {
            button.disabled = true;
            button.classList.add('opacity-50', 'cursor-not-allowed');
        }
    });
}

function clearFragmentInfo() {
    document.querySelectorAll('.video-fragment-title').forEach(el => el.textContent = 'N/A');
    document.querySelectorAll('.video-fragment-duration').forEach(el => el.textContent = 'N/A');
    document.querySelectorAll('.viral-score').forEach(el => el.textContent = '?');
    document.querySelector('.viral-description').textContent = 'No description available';
    document.querySelector('.video-fragment-tags').textContent = 'No tags available';
    
    const transcriptionArea = document.querySelector('.video-fragment-transcription');
    if (transcriptionArea) {
        transcriptionArea.value = '';
        const existingContainer = document.querySelector('.word-by-word-container');
        if (existingContainer) {
            existingContainer.remove();
        }
    }

}

function updateFragmentInfo(fragment) {
    document.querySelectorAll('.video-fragment-title').forEach(el => el.textContent = fragment.fragmentTitle);
    document.querySelectorAll('.video-fragment-duration').forEach(el => el.textContent = fragment.duration);
    document.querySelectorAll('.viral-score').forEach(el => el.textContent = fragment.viralScore);
    document.querySelector('.viral-description').textContent = fragment.viralDescription;
    document.querySelector('.video-fragment-tags').textContent = fragment.tags.join(', ');
    
    const transcriptionArea = document.querySelector('.video-fragment-transcription');
    if (transcriptionArea) {
        const existingContainer = document.querySelector('.word-by-word-container');
        if (existingContainer) {
            existingContainer.remove();
        }
        transcriptionArea.value = fragment.transcriptionRaw;
        initializeWordByWordEditing(transcriptionArea, fragment.uuid);
    }

    document.querySelectorAll('.export-video-button, .rerender-fragment-button').forEach(button => {
        button.dataset.videoUuid = fragment.uuid;
    });

    const videoPlayer = document.querySelector('.video-fragment-file');
    videoPlayer.src = fragment.videoLink;
    videoPlayer.load();
}

function initializeWordByWordEditing(textarea, fragmentUuid) {
    const text = textarea.value;
    const words = text.split(/\s+/);
    
    const container = document.createElement('div');
    container.className = 'word-by-word-container bg-gray-800 rounded px-3 py-3 text-[13px] text-[#ffffff] min-h-[8rem] overflow-y-auto';
    
    words.forEach((word, index) => {
        const span = document.createElement('span');
        span.textContent = word + ' ';
        span.className = 'cursor-pointer hover:bg-gray-700 px-1 rounded';
        span.dataset.index = index;
        span.addEventListener('click', () => editWord(span, index, textarea, fragmentUuid));
        container.appendChild(span);
    });
    
    textarea.style.display = 'none';
    textarea.parentNode.insertBefore(container, textarea.nextSibling);
}

function editWord(span, index, textarea, fragmentUuid) {
    const input = document.createElement('input');
    input.type = 'text';
    input.value = span.textContent.trim();
    input.className = 'bg-gray-700 text-white px-2 py-1 rounded outline-none text-[13px] w-auto';
    
    input.addEventListener('blur', () => {
        const newWord = input.value.trim();
        span.textContent = newWord + ' ';
        span.style.display = '';
        input.remove();
        updateTextarea(textarea, fragmentUuid);
    });
    
    input.addEventListener('keypress', (e) => {
        if (e.key === 'Enter') {
            input.blur();
        }
    });
    
    span.style.display = 'none';
    span.parentNode.insertBefore(input, span);
    input.focus();
}

function updateTextarea(textarea, fragmentUuid) {
    const container = document.querySelector('.word-by-word-container');
    const words = Array.from(container.children).map(span => span.textContent.trim());
    textarea.value = words.join(' ');
    
    const fragmentIndex = videoData.fragments.findIndex(f => f.uuid === fragmentUuid);
    if (fragmentIndex !== -1) {
        videoData.fragments[fragmentIndex].transcriptionRaw = textarea.value;
        
        if (!videoData.fragments[fragmentIndex].transcriptionTimecodes) {
            videoData.fragments[fragmentIndex].transcriptionTimecodes = [];
        }

        const updatedTranscriptionTimecodes = words.map((word, index) => {
            return {
                start: videoData.fragments[fragmentIndex].transcriptionTimecodes[index]?.start || "",
                end: videoData.fragments[fragmentIndex].transcriptionTimecodes[index]?.end || "",
                text: word
            };
        });
        videoData.fragments[fragmentIndex].transcriptionTimecodes = updatedTranscriptionTimecodes;
    }
}

function selectVideoFragment(uuid) {
    console.log('Selected fragment:', uuid);
    const fragments = document.querySelectorAll('.select-video');
    fragments.forEach(fragment => {
        if (fragment.dataset.videoUuid === uuid) {
            fragment.dataset.selected = "true";
            fragment.setAttribute('selected', '');
        } else {
            fragment.dataset.selected = "false";
            fragment.removeAttribute('selected');
        }
    });

    if (videoData.fragments) {
        const selectedFragment = videoData.fragments.find(f => f.uuid === uuid);
        if (selectedFragment) {
            updateFragmentInfo(selectedFragment);
        }
    }
}

function exportVideo(videoId, fragmentUuid) {
    console.log('Exporting video:', videoId, 'fragment:', fragmentUuid);
    
    const fragment = videoData.fragments.find(f => f.uuid === fragmentUuid);
    
    if (fragment && fragment.videoLink) {
        const link = document.createElement('a');
        link.href = fragment.videoLink;
        
        const fileName = `video_${videoId}_fragment_${fragmentUuid}.mp4`;
        link.download = fileName;
        
        document.body.appendChild(link);
        link.click();
        document.body.removeChild(link);
        
        console.log(`Downloading video: ${fileName}`);
    } else {
        console.error('Video fragment not found or video link is missing');
    }
}

function rerenderFragment(videoId, fragmentUuid) {
    console.log('Re-rendering fragment:', fragmentUuid, 'of video:', videoId);
    const fragment = videoData.fragments.find(f => f.uuid === fragmentUuid);
    if (fragment) {
        updateVideoStatus('Processing');
        
        const data = new URLSearchParams({
            transcriptionRaw: fragment.transcriptionRaw,
            transcriptionTimecodes: JSON.stringify(fragment.transcriptionTimecodes),
            uuid: fragmentUuid,
            id: videoId
        });

        fetch('./src/Api/v1.php?rerenderVideo', {
            method: 'POST',
            body: data
        })
        .then(response => response.json())
        .then(data => {
            if (data.status === 'success') {
                updateVideoStatus('Completed');
                window.location.reload();
            } else {
                updateVideoStatus('Error');
                console.error('Rerender failed:', data.message);
            }
        })
        .catch(error => {
            updateVideoStatus('Error');
            console.error('Rerender error:', error);
        });
    }
}

function updateVideoStatus(status) {
    if (status !== currentStatus) {
        currentStatus = status;
        const statusIndicator = document.querySelector('.status-indicator');
        statusIndicator.textContent = status;
        statusIndicator.className = 'status-indicator px-2 py-1 text-xs font-medium rounded-full';
        
        switch(status) {
            case 'Processing':
                statusIndicator.classList.add('bg-[#2a2b1c]', 'text-[#f5e65b]');
                updateButtonState(false);
                break;
            case 'Error':
                statusIndicator.classList.add('bg-[#2b1c1c]', 'text-[#f55b5b]');
                updateButtonState(true);  
                break;
            case 'Completed':
                statusIndicator.classList.add('bg-[#252b1c]', 'text-[#a2e26a]');
                updateButtonState(true); 
                rerenderPage();
                break;
        }
    }
}

function rerenderPage() {
    if (videoData) {
        renderVideoData(videoData);
        
        if (videoData.fragments && videoData.fragments.length > 0) {
            const firstFragmentUuid = videoData.fragments[0].uuid;
            selectVideoFragment(firstFragmentUuid);
        }
        
        updateButtonState(videoData.status !== 'Processing');
    }
}

function startStatusCheck(videoId) {
    if (statusCheckInterval) {
        clearInterval(statusCheckInterval);
    }

    statusCheckInterval = setInterval(() => {
        fetch(`./src/Api/v1.php?getVideo=${videoId}`)
            .then(response => response.json())
            .then(data => {
                if (data.status !== currentStatus) {
                    updateVideoStatus(data.status);
                    if (data.status === 'Completed') {
                        videoData = data;
                        rerenderPage();
                    }
                }
            })
            .catch(error => console.error('Error checking video status:', error));
    }, 10000); 
}