$(document).ready(
    do_stuff
)

function do_stuff(){
    
    $('.add-to-cart').unbind('click').click(
       function(event) {
           clicked_prod_id = $(this).attr('product_id');
           input_selector=`input[product_id=${clicked_prod_id}]`;
           obj_body = {"product":clicked_prod_id,"qty":$(input_selector).val()};
           settings = form_body_and_settings(obj_body);
           $(input_selector).val(null);
           $.ajax(settings);
        }
    )
}
function read_response(resp){
    $('.cart-size').html(function(i, val) { return +val+1 });
    alert(jQuery.parseJSON(resp)["success"]);
}
function handle_error(first,_unimportant,_ignore){
    alert(jQuery.parseJSON(first.responseText)["error"]);
}

function form_body_and_settings(obj_body) {
    body=JSON.stringify(obj_body);
    settings={"url":"/addtocart","method":"POST",
            "contentType":"application/json",
            "data":body,
            "success":read_response,
            "error":handle_error};
    return settings;
}