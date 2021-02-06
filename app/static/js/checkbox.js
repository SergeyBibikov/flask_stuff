$("#confirm_checkbox").prop("checked",false);
$("#confirm_delete_checkbox").prop("checked",false);
disable_input2();
disable_input();

function disable_input(){ 
    $('#confirm_checkbox').on('click',()=>{
        if($("#confirm_checkbox").prop("checked")){
        $('#edit_manuf').prop("disabled",false)
        }else{
        $('#edit_manuf').prop("disabled",true)
    }});

}
function disable_input2(){
    $('#confirm_delete_checkbox').on('click',()=>{
        if($("#confirm_delete_checkbox").prop("checked")){
        $('#delete_manuf').prop("disabled",false)
        }else{
        $('#delete_manuf').prop("disabled",true)
    }});
}
