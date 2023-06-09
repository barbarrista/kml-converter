function proccessForm(event) {
    event.preventDefault()

    formatSelect = document.getElementById("format-select")
    fileInput = document.getElementById("file-input")
    let file = fileInput.files[0]
    fileName = file.name.toLocaleLowerCase()

    convertToFormat = formatSelect.value

    formData = new FormData(form)
    formData.append("file", file)

    if (fileName.endsWith(".kml")) {
        convertKMLFile(formData = formData, fileFormat = convertToFormat)
    }

    if (fileName.endsWith(".gpx")) {
        convertGPXFile(formData = formData, fileFormat = convertToFormat)
    }
}

function convertGPXFile(formData, fileFormat) {
    axios.post("/api/v1/converter/gpx/build", formData, {
        headers: {
            "Content-Type": "multipart/form-data",
        },
        params: {
            "report_type": fileFormat,
        },
    }).then(processReponse).catch(processError)
}

function convertKMLFile(formData, fileFormat) {
    axios(
        {
            method: "post",
            url: "/api/v1/converter/kml/build",
            responseType: "stream",
            data: formData,
            headers: {
                "Content-Type": "multipart/form-data",
            },
            params: {
                "report_type": fileFormat,
            },

        }).then(processReponse).catch(processError)
}

function processReponse(response) {
    console.log(response)
    const href = URL.createObjectURL(new Blob([response.data]))
    downloadButton = document.getElementById("download-btn")
    downloadButton.href = href;
    contenDisposition = response.headers["content-disposition"]
    fileName = getFileName(contenDisposition)
    downloadButton.setAttribute('download', fileName)
    downloadButton.click()
}

function processError(error) {
    console.log(error)
}

function getFileName(contenDisposition) {
    return contenDisposition.split("filename=")[1]
}