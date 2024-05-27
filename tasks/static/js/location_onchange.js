document.addEventListener('DOMContentLoaded', function() {
    $('#id_location').change(function() {
        var selectedLocation = $(this).val();
        fetchLocationBackground(selectedLocation)
    });
 });