$ = jQuery
$(document).ready =>

    set_ajax_form = (
        form_id,
        after = ->
        before = ->
            true
    ) ->
        $(form_id).ajaxForm
            success: (data) ->
                after(data)
                $(form_id).parent().html data
                set_ajax_form form_id, after, before
            beforeSubmit: ->
                before()

    set_ajax_form('#auth-form')


    load_support_comments = ->
        url = $('.ticket-comments').attr('url')
        $('.ticket-comments').load url

    load_support_comments()
    setInterval(
        ->
            load_support_comments()
        60000
    )


    form_url = $('.tiket-comment-add').attr('form-url')
    $('.tiket-comment-add').load form_url, ->
        set_ajax_form '#add-comment-form',
            (data) ->
                load_support_comments()
            ->
                $('.new-tiket .submit .progress').css('display', 'block')
                true


