/**
 * Sets the initial background based on the initial location value.
 */
function initialLocationBackground() {
    var initialLocation = $('#id_location').val();
    if (initialLocation) {
        fetchLocationBackground(initialLocation);
    }
}

// Execute initialLocationBackground() when the DOM content is loaded
document.addEventListener('DOMContentLoaded', function() {
    // Set initial background based on initial location
    initialLocationBackground();

    // Change event handler for the location dropdown
    $('#id_location').change(function() {
        var selectedLocation = $(this).val();
        fetchLocationBackground(selectedLocation)
    });
 });