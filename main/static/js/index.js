/**
 * Created by WU.YH on 2017/2/28.
 */
$(function() {

    function get_wo_result(stu_id) {
        var intervalId = setInterval(function() {
            $.get(window.location.href + stu_id +'/result', function(res) {
                clearInterval(intervalId);
                $.hideLoading();
                if (res.errmsg == 'ok') {
                    $('.page.msg').show();
                    // 绑定成功3秒后关闭窗口
                    setTimeout(function() {
                        wx.closeWindow();
                    }, 3000);
                } else {
                    // 绑定失败，显示后端信息
                    $('#err_msg').text(res.errmsg);
                    $('.weui_dialog_alert').show();
                }
            });
        }, 1000);
    }

    $('#submit').click(function() {
        var stu_id = $('#stu_id').val().replace(/\s+/g, '');
        var stu_name = $('#stu_name').val().replace(/\s+/g, '');
        var tel_number = $('#tel_number').val().replace(/\s+/g,'');
        var brand = $('#brand').val().replace(/\s+/g,'');
        var problem = $('#problem').val().replace(/\s+/g,'');
        var remark = $('#remark').val().replace(/\s+/g,'');

        // 验证各项信息不为空
        if (!!stu_id && !!stu_name && !!tel_number && !!brand && !!problem) {
            // 判断绑定类型
            $.showLoading();
            var data = {
                stu_id: stu_id,
                stu_name: stu_name,
                tel_number : tel_number,
                brand : brand,
                problem : problem,
                remark : remark
            };
            // 提交绑定信息
            $.post(window.location.href, data, function(res) {
                if (res.errmsg == 'ok') {
                    $.post()
                }
            });
        } else {
            // 提示输入格式不正确
            $('.js_tooltips').show();
            setTimeout(function() {
                $('.js_tooltips').hide();
            }, 3000);
        }
    });

    // 关闭错误弹框
    $('.weui_btn_dialog.primary').click(function() {
        $('.weui_dialog_alert').hide();
    });
});
