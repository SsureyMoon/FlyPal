/* Project specific Javascript goes here. */
(function() {
    setTimeout(function(){
        $('#datetimepicker1').datepicker({ dateFormat: 'yy-mm-dd' });

        var data = [
            'SFO',
            'LAX',
            'LGA',
            'DXB',
            'PAR',
            'ICN'
        ];
        $('#incsearch').autocomplete({
            lookup: data,
            autoFocus: true,
            delay: 500,
            minLength: 1
        });

    }, 500);

    $('.disconnect-form').on('click', 'a.btn', function (event) {
      event.preventDefault();
      $(event.target).closest('form').submit();
    });
}());