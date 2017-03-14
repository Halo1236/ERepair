/**
 * Created by WU.YH on 2017/3/8.
 */
$(function () {
    function get_user_result() {
        var intervalId = setInterval(function() {
            clearInterval(intervalId);
            $.hideLoading();
            $.get(window.location.href +'/result');
        }, 2000);
        window.location.href =window.location.href+'/result';
    }

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
                    get_user_result();
                }
            });
        } else {
            // 提示输入格式不正确
            $.toptip('学号或姓名格式错误','error');
        }
    });
});