# _*_ coding:utf-8 _*_

all_rank_html_text = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport"
          content="width=device-width, user-scalable=no, initial-scale=1.0, maximum-scale=1.0, minimum-scale=1.0">
    <title>茅坝中学运动排名</title>
    <script src="http://cdn.bootcss.com/jquery/3.2.1/jquery.min.js"></script>
    <script src="http://cdn.bootcss.com/radialIndicator/1.3.1/radialIndicator.min.js"></script>
    <link rel="stylesheet" href="http://cdn.bootcss.com/spectre.css/0.5.0/spectre.min.css">
    <link rel="stylesheet" href="http://cdn.bootcss.com/spectre.css/0.5.0/spectre-exp.min.css">
    <link rel="stylesheet" href="http://cdn.bootcss.com/spectre.css/0.5.0/spectre-icons.min.css">
    <script src="http://cdn.bootcss.com/moment.js/2.20.1/moment.min.js"></script>
    <script src="http://cdn.bootcss.com/moment.js/2.20.1/locale/zh-cn.js"></script>
    <script src="http://cdn.bootcss.com/vue/2.5.13/vue.min.js"></script>
    <script src="http://cdn.bootcss.com/lodash.js/4.17.4/lodash.min.js"></script>
    <script src="http://cdn.bootcss.com/pako/1.0.6/pako.min.js"></script>
    <script src="http://cdn.bootcss.com/dexie/2.0.1/dexie.min.js"></script>
    <script>
        var mydate = new Date();
        function handle_time() {
            var year = mydate.getFullYear();
            var month = mydate.getMonth()+1;
            var day = mydate.getDate();
            return year+'-'+month+'-'+day;
        }
        function handle_data(data) {
            data = JSON.parse(data);
            data.forEach(function(curent,index, item) {
                $("#main_tboby").append( "<tr><th>" + (index+1).toString()+ "</th><th>" + curent["nickName"]+"</th><th>"+curent["scoreNow"]+ "</th></tr>");
            });
        }
        $(document).ready(function () {
            $("#select_query").bind("change", function () {
               alert($(this).val());
            });
            $.post("today",
                {"day": 123,
                "date": handle_time()
                },
                function (data, status) {
                    if (status == "success")
                    {
                        handle_data(data);

                    }

                }

            );
        });

    </script>
</head>
<body>
<div id="select_div" style="padding-top: 10px">
    <label>查询：</label>
    <select id="select_query">
        <option value="today">今日数据</option>
        <option value="my_home">我的个人主页</option>
        <option value="current_week">查看本周</option>
        <option value="last_week">查看上周</option>
        <option value="month">查看本月</option>
    </select></div>
<br>
<ul class="tab tab-block">
                    <li class="tab-item" :class="tabSelected==='today'?'active':''">
                        <a href="javascript:void(0);">今日</a>
                    </li>
                </ul>
                <table class="table table-striped table-hover" style="font-size: 0.5em;">
                    <thead>
                    <tr>
                        <th>排名</th>
                        <th>昵称</th>

                        <th>步数</th>
                    </tr>
                    </thead>
                    <tbody id="main_tboby">

                    </tbody>
                </table>
</body>
</html>
"""