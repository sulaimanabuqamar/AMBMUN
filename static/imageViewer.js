var album = {};
fetch(location.href.replace("Album", "AlbumJson")) // api for the get request
    .then(response => response.json())
    .then(data => { album = data; console.log(album); });
function getMediaTypeFromExtension(extension) {
    extension = extension.replace(".", "");
    if (extension == "mp4" || extension == "mov" || extension == "hevc") {
        return "video";
    }
    else {
        return "image";
    }
}
var id = 0;
var mediaViewInterval;
function viewMedia(photo, video, mediaType) {
    console.log(mediaType);
    var mediaitem = "";
    if (mediaType == "video") {
        mediaitem = video;
    }
    else {
        mediaitem = photo;
    }
    if (mediaType == "image") {
        for (var i = 0; i < album.media_items.length; i++) {
            if (mediaitem == album.media_items[i].photo) {
                id = i;
                break;
            }
        }
    }
    else if (mediaType == "video") {
        for (var i = 0; i < album.media_items.length; i++) {
            if (mediaitem == album.media_items[i].video) {
                id = i;
                break;
            }
        }
    }
    // var media = "test.mskdfl.mp4";
    var mediaDesc = album.media_items[id].description;
    // var mediaType = getMediaTypeFromExtension(media.substring(media.lastIndexOf(".")));
    var backdrop = document.createElement("div");
    backdrop.className = "backdrop";
    var window = document.createElement("div");
    window.className = "imageViewerWindow";
    var toolbar = document.createElement("div");
    toolbar.className = "imageViewerToolbar";
    var toolbarleft = document.createElement("div");
    toolbarleft.classList.add("imageViewerToolbarContent");
    toolbarleft.classList.add("left");
    var toolbarright = document.createElement("div");
    toolbarright.classList.add("imageViewerToolbarContent");
    toolbarright.classList.add("right");
    var closebutton = document.createElement("button");
    closebutton.innerHTML = "X";
    closebutton.style = "border: none;background: none;color: red;width: 30px;display: flex;align-items: center;justify-content: center;";
    closebutton.onclick = function () {
        document.getElementsByClassName("backdrop")[0].remove();
    }
    var downloadbutton = document.createElement("button");
    downloadbutton.innerHTML = "<img src='/media/images/download_24dp_FILL0_wght400_GRAD0_opsz24.svg'>";
    downloadbutton.style = "border: none;background: none;width: 30px;display: flex;align-items: center;justify-content: center;"
    downloadbutton.onclick = function () {
        var a = document.createElement("a");
        a.href = photo;
        a.download = true;
        a.click();
    }
    var sharebutton = document.createElement("button");
    sharebutton.innerHTML = "<img src='/media/images/share_24dp_FILL0_wght400_GRAD0_opsz24.svg'>";
    sharebutton.style = "border: none;background: none;width: 30px;display: flex;align-items: center;justify-content: center;"
    sharebutton.reslink = mediaitem;
    sharebutton.onclick = function () {
        navigator.share({
            title: mediaDesc,
            url: reslink
        });
    }

    var previousbutton = document.createElement("button");
    previousbutton.innerHTML = "<img src='/media/images/arrow_back_ios_24dp_FILL0_wght400_GRAD0_opsz24.svg'>";
    previousbutton.style = "border: none;background: none;width: 30px;display: flex;align-items: center;justify-content: center;"
    previousbutton.onclick = function () {
        if (id > 0) {
            id--;
        }
        else {
            id = 0;
        }
        mediaDesc = album.media_items[id].description;
        // mediaType = getMediaTypeFromExtension(media.substring(media.lastIndexOf(".")));
        mediaView.remove();
        var tempitem = albumdata[id];
        if (tempitem.media_type == "image") {
            mediaView = document.createElement("img");
            mediaView.src = tempitem.photo;
            mediaView.style = "object-fit: contain; width: 100%; height: calc(100% - 40px); margin-top: 10px;";
            window.appendChild(mediaView);
        }
        else if (tempitem.media_type == "video") {
            mediaView = document.createElement("div");
            mediaView.innerHTML = `<iframe src="` + tempitem.video + `" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen style="width: 100%;"></iframe>`;
            clearInterval(mediaViewInterval);
            mediaViewInterval = setInterval(function () {
                mediaView.children[0].style.height = window.clientHeight.toString() + "px";
            }, 1000);
        }
        else {
            alert("Unknown Media Type");
        }
        window.appendChild(mediaView);
        medialabel.innerHTML = mediaDesc;
    }
    var nextbutton = document.createElement("button");
    nextbutton.innerHTML = "<img src='/media/images/arrow_forward_ios_24dp_FILL0_wght400_GRAD0_opsz24.svg'>";
    nextbutton.style = "border: none;background: none;width: 30px;display: flex;align-items: center;justify-content: center;"
    nextbutton.onclick = function () {
        if (id < album.media_items.length) {
            id++;
        }
        else {
            id = album.media_items.length - 1;
        }
        mediaDesc = album.media_items[id].description;
        mediaView.remove();
        var tempitem = albumdata[id];
        if (tempitem.media_type == "image") {
            mediaView = document.createElement("img");
            mediaView.src = tempitem.photo;
            mediaView.style = "object-fit: contain; width: 100%; height: calc(100% - 40px); margin-top: 10px;";
            window.appendChild(mediaView);
        }
        else if (tempitem.media_type == "video") {
            mediaView = document.createElement("div");
            mediaView.innerHTML = `<iframe src="` + tempitem.video + `" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen style="width: 100%;"></iframe>`;
            clearInterval(mediaViewInterval);
            mediaViewInterval = setInterval(function () {
                mediaView.children[0].style.height = window.clientHeight.toString() + "px";
            }, 1000);
        }
        else {
            alert("Unknown Media Type");
        }
        window.appendChild(mediaView);
        medialabel.innerHTML = mediaDesc;
    }
    var medialabel = document.createElement("p");
    medialabel.innerHTML = mediaDesc;
    medialabel.style = "margin: 0; margin-left: 5px;"

    var mediaView = null;
    if (mediaType == "image") {
        mediaView = document.createElement("img");
        mediaView.src = album.media_items[id].photo;
        mediaView.style = "object-fit: contain; width: 100%; height: calc(100% - 40px); margin-top: 10px;";
        window.appendChild(mediaView);
    }
    else if (mediaType == "video") {
        mediaView = document.createElement("div");
        mediaView.innerHTML = `<iframe src="` + album.media_items[id].video + `" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen style="width: 100%;"></iframe>`;
        clearInterval(mediaViewInterval);
        mediaViewInterval = setInterval(function () {
            mediaView.children[0].style.height = window.clientHeight.toString() + "px";
        }, 1000);
    }
    else {
        alert("Unknown Media Type");
    }

    // toolbarright.appendChild(sharebutton);
    // toolbarright.appendChild(downloadbutton);
    toolbarright.appendChild(closebutton);

    toolbarleft.appendChild(previousbutton);
    toolbarleft.appendChild(nextbutton);
    toolbarleft.appendChild(medialabel);

    toolbar.appendChild(toolbarleft);
    toolbar.appendChild(toolbarright);
    window.appendChild(toolbar);
    window.appendChild(mediaView);
    backdrop.appendChild(window);
    document.body.appendChild(backdrop);
}
// setTimeout(function() {
var elements = document.getElementsByClassName("cardrow flexcontainer")[0].children;
for (var i = 0; i < elements.length; i++) {
    var img = elements[i].children[0].children[0];
    // var result = getMediaTypeFromExtension(img.src.substring(img.src.lastIndexOf("."))) ;
    var result = img.dataset.type;
    console.log(result);
    if (result == "video") {
        img.src = "/media/images/movie_24dp_FILL0_wght400_GRAD0_opsz24.svg";
    }
    else {

    }
}
// },3000);