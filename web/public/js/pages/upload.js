document.addEventListener('DOMContentLoaded', function() {

    Dropzone.autoDiscover = false;

    const myDropzone = new Dropzone(".video-dropzone", {
        url: "./src/Api/v1.php?uploadVideo",
        maxFilesize: 400,
        acceptedFiles: ".mp4",
        autoProcessQueue: false,
        addRemoveLinks: true,
        maxFiles: 1,
        createImageThumbnails: false
    });

    const uploadButton = document.querySelector('.upload-button');
    const titleInput = document.querySelector('.video-title-input');
    const addVideoSoapCheckbox = document.getElementById('addVideoSoap');
    const progressBar = document.querySelector('.progress-bar');
    const progressText = document.querySelector('.progress-text');
    const uploadProgress = document.querySelector('.upload-progress');

    tippy('.soap-tooltip', {
        content: 'Данный переключатель отвечает за добавление на видео залипательного фона с нарезкой мыла для повышения виральности',
    });

    addVideoSoapCheckbox.addEventListener('change', function() {
        const toggleLabel = this.nextElementSibling;
        if (this.checked) {
            toggleLabel.classList.remove('bg-gray-700');
            toggleLabel.classList.add('bg-[#00a1e7]');
        } else {
            toggleLabel.classList.remove('bg-[#00a1e7]');
            toggleLabel.classList.add('bg-gray-700');
        }
    });

    function setUploadButtonState(enabled) {
        if (enabled) {
            uploadButton.disabled = false;
            uploadButton.classList.remove('opacity-50', 'cursor-not-allowed');
        } else {
            uploadButton.disabled = true;
            uploadButton.classList.add('opacity-50', 'cursor-not-allowed');
        }
    }

    uploadButton.addEventListener('click', function() {
        const videoTitle = titleInput.value.trim();
        if (!videoTitle) {
            Swal.fire('Error', 'Please enter a video title', 'error');
            return;
        }

        if (myDropzone.files.length === 0) {
            Swal.fire('Error', 'Please select a video file', 'error');
            return;
        }

        setUploadButtonState(false);
        myDropzone.processQueue();
    });

    myDropzone.on("sending", function(file, xhr, formData) {
        formData.append("videoTitle", titleInput.value);
        formData.append("addSoapVideo", addVideoSoapCheckbox.checked ? "1" : "0");
        uploadProgress.classList.remove('hidden');
        setUploadButtonState(false);
    });

    myDropzone.on("uploadprogress", function(file, progress) {
        progressBar.style.width = progress + "%";
        progressText.textContent = Math.round(progress) + "%";
    });

    myDropzone.on("success", function(file, response) {
        Swal.fire('Success', 'Video uploaded successfully', 'success')
        .then(() => {
            window.location.href = '/all-videos';
        });
    });

    myDropzone.on("error", function(file, errorMessage) {
        Swal.fire('Error', errorMessage, 'error');
        uploadProgress.classList.add('hidden');
        setUploadButtonState(true);
    });

    myDropzone.on("addedfile", function() {
        setUploadButtonState(true);
    });

    myDropzone.on("removedfile", function() {
        if (myDropzone.files.length === 0) {
            setUploadButtonState(false);
        }
    });
});