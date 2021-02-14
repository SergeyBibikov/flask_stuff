$(document).ready(
    do_stuff
)

function do_stuff(){
    $('input[name="delete_item"]').unbind('click').click(
            function(e){
                product = $(this).attr('product');
                //e.preventDefault();
                if(confirm("Удалить выбранный продукт?")){
                    //$(this).unbind('click');
                    $(`#delete_item[product=${product}]`).submit();
                }else{
                    console.log("No I won't");
                    e.preventDefault();
                }
            }
        )
}
