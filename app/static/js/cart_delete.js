$(document).ready(
    do_stuff
)

function do_stuff(){
    $('input[name="delete_item"]').unbind('click').click(
            function(e){
                product = $(this).attr('product');
                if(confirm("Удалить выбранный продукт?")){
                    $(`#delete_item[product=${product}]`).submit();
                }else{
                    e.preventDefault();
                }
            }
        );
}
