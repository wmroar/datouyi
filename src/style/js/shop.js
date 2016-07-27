// JavaScript Document
// Do.ready(function(){
//     $('#addshop').click(function(event) {
//         if($('#num_sel').val().length > 0){
//             $.ajax({
//                 'url' : '/ajax/vcode?num_sel=' + $('#num_sel').val() + '&rt='+ Math.floor((Math.random()*100)+1),
//                 'type' : 'GET',
//                 'cache' : false,
//                 'dataType' : 'json',
//                 'success' : function(result) {
//                     if(result.status)
//                     {
//                         alert('成功');
//                     } else {
//                         alert('失败');
//                     }
//                 }
//              });
//         }else{
//             alert('请填写数量');
//             $('#num_sel').focus();
//         }
//     return false;
//     });
// });