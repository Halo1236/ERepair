/**
 * Created by WU.YH on 2017/2/28.
 */
$(function () {
    $("#brand").select({
        title: "选择品牌",
        items: [
            {
                title: "联想 lenovo",
                value: "001"
            },
            {
                title: "华硕 asus",
                value: "002"
            },
            {
                title: "戴尔 dell",
                value: "003"
            },
            {
                title: "苹果 mac",
                value: "004"
            },
            {
                title: "惠普 HP",
                value: "005"
            },
            {
                title: "神舟 hasee",
                value: "006"
            },
            {
                title: "宏碁 acer",
                value: "007"
            },
            {
                title: "其他品牌",
                value: "008"
            }
        ]
      });
    $("#problem").select({
        title: "选择问题",
        items: [
            {
                title: "重装系统",
                value: "001"
            },
            {
                title: "电脑清灰",
                value: "002"
            },
            {
                title: "驱动安装",
                value: "003"
            },
            {
                title: "硬件更换",
                value: "004"
            }
        ]
      });
});