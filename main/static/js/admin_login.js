/**
 * Created by WU.YH on 2017/3/22.
 */
$(function () {
    $('#admin_login').click(function () {
        var admin_name = $('#admin_name').val().trim();
        var admin_passwd = $('#admin_passwd').val().trim();
        if (admin_passwd && admin_name) {
            var data = {
                admin_name: admin_name,
                admin_passwd: admin_passwd
            };
            $.post(window.location.href, data, function (res) {
                if (res.errmsg == 'ok') {
                    $("#success").html("<p>登录成功</p>").show();
                    $("#sign_in").addClass("loading");
                    setTimeout(function () {
                        window.location.href = window.location.href+'/index';
                    }, 1000);
                } else {
                    $("#error").html("<p>登录失败</p>").show();
                }
            })
        }else {
            $("#error").html("<p>编号或姓名不能为空</p>").show();
        }
    });
});