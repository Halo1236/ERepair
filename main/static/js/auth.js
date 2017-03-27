/**
 * Created by WU.YH on 2017/3/8.
 */
$(function () {

    $('#log_in').click(function() {
        var userid = $('#userid').val().replace(/\s+/g,'');
        var username = $('#username').val().replace(/\s+/g,'');

        // 验证各项信息不为空
        if (!!userid && !!username ) {
            // 判断绑定类型
            $.showLoading();
            var data = {
                userid : userid,
                username : username
            };
            // 提交绑定信息
            $.post(window.location.href, data, function(res) {
                if (res.errmsg == 'ok') {
                    $.hideLoading();
                    setTimeout(function () {
                        window.location.href =window.location.href+'index';
                    }, 500);
                }else {
                    $.toptip(res.errmsg,'error');
                    $.hideLoading();
                }
            });
        } else {
            // 提示输入格式不正确
            $.toptip('学号或姓名格式错误','error');
        }
    });
});