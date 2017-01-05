(function() {
    function setup() {
        var selector = '.django-mediumeditor-editable';
        var editor = new MediumEditor(selector, MediumEditorOptions);
        // update the text box
        editor.subscribe('blur', function (event, editable) {
            // Get the HTML from the editor
            var html = editable.innerHTML.trim();
            // Grab the selector for the associated text area
            var textareaSelector = '#' + editable.attributes['data-mediumeditor-textarea'].value;
            // Update the value of the textarea to the HTML
            document.querySelectorAll(textareaSelector)[0].value = html;
        });
        // load the data in
        var editableElements = document.querySelectorAll(selector);
        Array.prototype.forEach.call(editableElements, function(el, i){
            // Grab the selector for the associated text area
            var textareaSelector = '#' + el.attributes['data-mediumeditor-textarea'].value;
            // Get the stored HTML
            var html = document.querySelectorAll(textareaSelector)[0].value;
            // Set the value
            editor.setContent(html, i);
        });
    };

    // Wait for the DOM to be loaded before configuring the editor
    if (document.readyState != 'loading'){
        setup();
    } else {
        document.addEventListener('DOMContentLoaded', setup);
    }

})();
