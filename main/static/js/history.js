/**
 * Created by WU.YH on 2017/3/26.
 */
$(function () {
    FastClick.attach(document.body);

    function canceled(wo_id) {
        $.confirm("您确定要取消工单编号为" + wo_id + "的工单吗?", "确认取消?", function () {
            $.post(window.location.href, {wo_id: wo_id, wo_ishandle: 3}, function (res) {
                if (res == 'ok') {
                    window.location.href = window.location.href;
                    $.toast("工单已取消!");
                }
            });
        }, function () {
            //取消操作
        });
    }

    function confirmed(wo_id) {
        $.prompt("1-5分请您打分评价", "确认评价", function (text) {
            $.post(window.location.href, {wo_id: wo_id, wo_evaluation: text}, function (res) {
                if (res == 'ok') {
                    window.location.href = window.location.href;
                    $.toast("评价成功!");
                }
            });
        }, function () {
            //点击取消后的回调函数
        });
    }
});

