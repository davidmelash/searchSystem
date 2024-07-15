$(document).ready(function () {
    $("#searchbar-date-input").click(function () {
        jQuery("#datePicker-block").attr("id", "datePicker");
        var date = new Date();
        var today = new Date(date.getFullYear(), date.getMonth(), date.getDate());


        var optComponent = {
            format: 'yyyy-mm-dd',
            container: '#datePicker',
            orientation: 'auto bottom',
            todayHighlight: true,
            autoclose: true
        };


// COMPONENT
        $('#datePicker').datepicker(optComponent);

// ===================================


        $('#datePicker').datepicker('setDate', today);
    });


});