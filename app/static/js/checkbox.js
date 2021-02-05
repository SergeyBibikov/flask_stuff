$("#confirm_checkbox").prop("checked",false);
disable_input()

function disable_input(){ 
    $('#confirm_checkbox').on('click',()=>{
        if($("#confirm_checkbox").prop("checked")){
        $('#edit_manuf').prop("disabled",false)
        }else{
        $('#edit_manuf').prop("disabled",true)
    }})
}
