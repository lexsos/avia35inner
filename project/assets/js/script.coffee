$ = jQuery
$(document).ready =>
    console.log 'ok'


    set_ajax_form = (form_id) ->
        $(form_id).ajaxForm
            success: (data) ->
                $(form_id).parent().html data
                set_ajax_form form_id

    set_ajax_form('#auth-form')

