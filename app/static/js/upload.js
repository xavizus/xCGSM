$(() => {
    'use strict';
    const selector = {
        CUSTOMFILE: 'input[type="file"].custom-file-input',
        CUSTOMFILELABEL: '.custom-file-label',
        NEEDS_VALIDATION: '.needs-validation',
        IS_INVALID: '.invalid-feedback',
        ID_OF_UPLOAD: 'uploadFile'
    }

    const validFiles = ['xlsx'];

    const events = {
        inputchange: 'change'
    }
    let defaultText = ''

    // Validator
    function checkFileType() {
        let FS = document.getElementById(selector.ID_OF_UPLOAD);
        let files = FS.files;
        let filenamesMissingFileType = [];
        let message = '';
        if (files.length > 0) {
            for (let file of files) {
                let fileType = file.name.split('.').pop();
                console.log(fileType)
                if (!(validFiles.includes(fileType))) {
                    let realFilename = file.name.split('\\');
                    filenamesMissingFileType.push(realFilename[realFilename.length - 1]);
                }
            }
        } else {
            message = 'You need to upload a file!';

        }

        if (filenamesMissingFileType.length > 0) {
            message = `Following files are not xslx-format: ${filenamesMissingFileType.join(', ')}`;
        }
        if (message != '') {
            FS.parentNode.querySelector(selector.IS_INVALID).textContent = message;
            FS.form.classList.add('was-validated');
        }

        FS.setCustomValidity(message);
    }

    // Change label based of filename
    function handleInputChange(event) {
        let input = event.target;
        let label = input.parentNode.querySelector(selector.CUSTOMFILELABEL);
        let filenames = getFileName(input);
        if (filenames) {
            label.textContent = filenames;
        } else {
            label.textContent = defaultText;
        }
    }

    // get filenames from input
    function getFileName(input) {
        if (input.hasAttribute('multiple')) {
            return input.files.map((file) => {
                return file.name
            }).join(', ');
        }

        if (input.value.indexOf('fakepath') !== -1) {
            let realFilename = input.value.split('\\');
            return realFilename[realFilename.length - 1];
        }

        return input.value;
    }

    // Get the default text (Kind of pointless, because I don't have a reset (yet))
    function getDefaultText(input) {

        let label = input.parentNode.querySelector(selector.CUSTOMFILELABEL);

        if (label) {
            defaultText = label.textContent;
        }

        return defaultText;
    }

    // Get all input fields with selector.
    let fileInputArray = document.querySelectorAll(selector.CUSTOMFILE);

    // loop all inputs
    for (let fileInput of fileInputArray) {
        // Kind of pointless atm, but planned to be used when there is an reset button
        defaultText = getDefaultText(fileInput);

        fileInput.addEventListener(events.inputchange, handleInputChange);
    }

    // Get all forms that needs validation
    let forms = $(selector.NEEDS_VALIDATION);

    for (let form of forms) {
        form.addEventListener('submit', event => {
            event.preventDefault();
            event.stopPropagation();
            checkFileType();
            form.classList.add('was-validated');

            if (form.checkValidity() === true) {
                let body = new FormData(form);
                postData(form.action, form.method, body);
            }
        }, false)
    }
    document.getElementById(selector.ID_OF_UPLOAD).addEventListener(events.inputchange, checkFileType);
});

async function postData(actionURL, method, body) {
    try {
        let response = await fetch(actionURL, {
            method: method,
            body: body
        });
        let results = await response.json();
        if(response.status != 200){
            throw new Error(results.error);
        }
        console.log(results);
    } catch (error) {
        console.log(error);
    }
}