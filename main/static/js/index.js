/**
 * Created by WU.YH on 2017/2/28.
 */
$(function() {

    $('#submit').click(function() {
        var tel_number = $('#tel_number').val().replace(/\s+/g,'');
        var brand = $('#brand').val().replace(/\s+/g,'');
        var problem = $('#problem').val().replace(/\s+/g,'');
        var remark = $('#remark').val().replace(/\s+/g,'');
        var scheduled = $('#time').val().replace(/\s+/g,'');

        // 验证各项信息不为空
        if (!!tel_number && !!brand && !!problem && scheduled) {
            // 判断绑定类型
            $.showLoading();
            var data = {
                tel_number : tel_number,
                brand : brand,
                problem : problem,
                remark : remark,
                scheduled : scheduled
            };
            // 提交绑定信息
            $.post(window.location.href +'/result', data, function(res) {
                if (res.errmsg == 'ok') {
                    $.toptip('提交成功','success');
                    $.hideLoading();
                    setTimeout(function () {
                        window.location.href = window.location.href+'/succeed';
                    }, 500);
                }else {
                    $.toptip(res.errmsg,'error');
                    $.hideLoading();
                }
            });
        } else {
            // 提示输入格式不正确
            $.toptip('信息填写错误，不要留空','error');
        }
    });


    $('#warnning').click(function () {
        $.alert("1.请确保你的学号和姓名正确,个人信息会加密存储\n" +
                "2.请在前来维修前备份你的重要数据,如在维修过程中发生数据丢失,我们概不负责\n" +
                "3.如要硬件更换，需要你自己购买\n"+
                "4.本条款最终解释权归E修哥志愿服务队所有\n" , "条款", function() {
            $('#submit').removeClass('weui-btn_disabled');
        });
    });
});
