# _*_ coding:utf-8 _*_

from twisted.internet import reactor
from twisted.web.resource import Resource
from twisted.web.server import Site
import json
import logging
import re
from weixin.rundata import RunData

class Root(Resource):

    def __init__(self):
        Resource.__init__(self)
        self.putChild("", Index())
        self.putChild("rundata",RunData())

text = """
<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <meta name="viewport"
          content="width=device-width, user-scalable=no, initial-scale=1.0, maximum-scale=1.0, minimum-scale=1.0">
    <title>微信运动数据Demo_V4 最简示例</title>
    <script src="http://cdn.bootcss.com/jquery/3.2.1/jquery.min.js"></script>
    <script src="http://cdn.bootcss.com/radialIndicator/1.3.1/radialIndicator.min.js"></script>
    <link rel="stylesheet" href="http://cdn.bootcss.com/spectre.css/0.5.0/spectre.min.css">
    <link rel="stylesheet" href="http://cdn.bootcss.com/spectre.css/0.5.0/spectre-exp.min.css">
    <link rel="stylesheet" href="http://cdn.bootcss.com/spectre.css/0.5.0/spectre-icons.min.css">
    <script src="http://cdn.bootcss.com/moment.js/2.20.1/moment.min.js"></script>
    <script src="http://cdn.bootcss.com/moment.js/2.20.1/locale/zh-cn.js"></script>
    <script src="http://cdn.bootcss.com/vue/2.5.13/vue.min.js"></script>
    <script src="http://cdn.bootcss.com/lodash.js/4.17.4/lodash.min.js"></script>
</head>
<body>
<div id="app">
    <div class="container">
        <div class="columns">
            <div class="column col-12">
                <blockquote>
                    微信运动数据Demo_V4 最简示例
                </blockquote>
                <p style="font-size: 0.5em">本Demo采用了纯粹的前端H5直接调用本API的接口，直接实现了无服务器的展示微信运动数据的功能。<br><br>
                    主要使用了Vue.js(非编译模式)、jQuery和一个简单的css框架spectre。
                    <br><br>
                    调用了几个API：getDataByDate_v4、getSingleData_v4。
                </p>
                <!--<p style="font-size: 0.5em; color: blue;">-->
                    <!---->
                <!--</p>-->
                <p style="font-size: 0.5em">
                    talk is cheap, show me the code. 具体请看代码。
                </p>
            </div>
        </div>
    </div>
    <div class="container">
        <div class="columns">
            <div class="column col-12">
                <blockquote>
                    我的信息<br>
                    <span style="font-size: 0.5em; color: orangered;">(示例使用的用户fakeName为：{{fakeName}})</span>
                </blockquote>
                <table class="table table-striped table-hover" style="font-size: 0.5em;">
                    <thead>
                    <tr>
                        <th></th>
                        <th>昵称</th>
                        <th>步数</th>
                        <th>点赞</th>
                    </tr>
                    </thead>
                    <tbody>
                    <tr>
                        <td>
                            <figure class="avatar">
                                <img :src="userObj.head">
                            </figure>
                        </td>
                        <td style="word-break: break-all; word-wrap: break-word;">
                            {{ userObj.nickName }}
                        </td>
                        <td>{{userObj.scoreNow}}</td>
                        <td>{{userObj.starNow}}</td>
                    </tr>
                    <tr>
                        <td colspan="4">
                            <span style="color: darkgrey;">最后更新时间：{{userObj.tsString}}</span>
                        </td>
                    </tr>
                    </tbody>
                </table>
            </div>
        </div>
    </div>
    <div class="container">
        <div class="columns">
            <div class="column col-12">
                <blockquote>
                    今日实时排行榜
                </blockquote>
                <table class="table table-striped table-hover" style="font-size: 0.5em;">
                    <thead>
                    <tr>
                        <th>排名</th>
                        <th></th>
                        <th>昵称</th>
                        <th>步数</th>
                        <th>点赞</th>
                    </tr>
                    </thead>
                    <tbody>
                    <tr>
                        <td>{{userRankObj.index + 1}}</td>
                        <td>
                            <figure class="avatar">
                                <img :src="userRankObj.head">
                            </figure>
                        </td>
                        <td style="word-break: break-all; word-wrap: break-word;">
                            {{ userRankObj.nickName }}
                        </td>
                        <td>{{userRankObj.scoreNow}}</td>
                        <td>{{userRankObj.starNow}}</td>
                    </tr>
                    <tr>
                        <td colspan="5">
                            <hr/>
                        </td>
                    </tr>
                    <tr v-for="(item, index) in orderedRank" :key="item.fakeName">
                        <td>{{index + 1}}</td>
                        <td>
                            <figure class="avatar">
                                <img :src="item.head">
                            </figure>
                        </td>
                        <td style="word-break: break-all; word-wrap: break-word;">
                            {{ item.nickName }}
                        </td>
                        <td>{{item.scoreNow}}</td>
                        <td>{{item.starNow}}</td>
                    </tr>
                    </tbody>
                </table>
            </div>
        </div>
    </div>
</div>
</body>

<script>
    var app = new Vue({
        el: '#app',
        data: {
            todayRank: [],
            userObjRaw: {},
            fakeName: 'BZXQ.q9Zj',
            serverConfig: {
                baseUrl: 'http://wxs.grplpl.com/',
                // baseUrl: 'http://wxs.testhost.com:3000/',
                projectID: '0001',
                salt: 'ayme4jf59ibcgqr3',
            },
        },
        computed: {
            orderedRank: function () {
                var self = this;
                if (!self.todayRank || self.todayRank.length === 0) {
                    return [];
                }

                var _list = self.todayRank;

                //增加头像
                for (let _item of _list) {
                    _item.head = self.serverConfig.baseUrl
                        + 'getSingleHeadImage_v4?projectID=' + self.serverConfig.projectID
                        + '&salt=' + self.serverConfig.salt
                        + '&fakeName=' + _item.fakeName;
                }

                //本地排序
                _list = _.orderBy(_list, ['scoreNow'], ['desc']);
                return _list;
            },
            userObj: function () {
                var self = this;
                if (!self.userObjRaw || !self.userObjRaw.fakeName || self.userObjRaw.fakeName.length === 0) {
                    return {
                        head: '',
                        nickName: '',
                        scoreNow: 0,
                        starNow: 0,
                        tsString: '',
                    };
                }

                var _head = self.serverConfig.baseUrl
                    + 'getSingleHeadImage_v4?projectID=' + self.serverConfig.projectID
                    + '&salt=' + self.serverConfig.salt
                    + '&fakeName=' + self.userObjRaw.fakeName;

                var _list = self.userObjRaw.list;
                var _score = 0;
                var _star = 0;
                var _tsString = '(暂无数据)';
                if (_list && _list.length > 0) {
                    _list = JSON.parse(self.userObjRaw.list);
                    _list = _.orderBy(_list, ['dateString'], ['desc']);
                    _score = _list[0].scoreNow;
                    _star = _list[0].starNow;
                    _tsString = moment.unix(_list[0].timeStamp / 1000).format('YYYY-MM-DD HH:mm:ss');
                }

                return {
                    head: _head,
                    nickName: self.userObjRaw.nickName,
                    scoreNow: _score,
                    starNow: _star,
                    tsString: _tsString,
                };
            },
            userRankObj: function () {
                var self = this;
                if (!self.orderedRank || self.orderedRank.length === 0) {
                    return {};
                }

                var _index = _.findIndex(self.orderedRank, function (_obj) {
                    return _obj.fakeName === self.fakeName;
                });
                if (_index === -1) {
                    return {};
                }
                else {
                    return {
                        index: _index,
                        head: self.orderedRank[_index].head,
                        nickName: self.orderedRank[_index].nickName,
                        scoreNow: self.orderedRank[_index].scoreNow,
                        starNow: self.orderedRank[_index].starNow,
                    }
                }
            },
        },
        methods: {
            getTodayRank: function () {
                var self = this;
                // var _date = moment().format('YYYYMMDD'); //今天的日期字符串
                var _date = '20171217';

                $.ajax({
                    type: "post",
                    url: self.serverConfig.baseUrl + 'getDataByDate_v4/',
                    timeOut: 100000,
                    data: {
                        projectID: self.serverConfig.projectID,
                        salt: self.serverConfig.salt,
                        date: _date
                    },
                    before: function () {
                    },
                    success: function (_data) {
                        var msg = _data.msg;
                        if (msg.indexOf('success') > -1) {
                            self.todayRank = JSON.parse(_data.list);
                        }
                        else {
                            alert(msg);
                        }
                    },
                    error: function () {
                        alert('fail_2');
                    }
                });
            },
            getParameterByName: function (name, url) {
                if (!url) url = window.location.href;
                name = name.replace(/[\[\]]/g, "\\$&");
                var regex = new RegExp("[?&]" + name + "(=([^&#]*)|&|#|$)"),
                    results = regex.exec(url);
                if (!results) return null;
                if (!results[2]) return '';
                return decodeURIComponent(results[2].replace(/\+/g, " "));
            },
            getSingleData: function (_fakeName) {
                var self = this;

                $.ajax({
                    type: "post",
                    url: self.serverConfig.baseUrl + 'getSingleData_v4/',
                    timeOut: 100000,
                    data: {
                        projectID: self.serverConfig.projectID,
                        salt: self.serverConfig.salt,
                        fakeName: _fakeName,
                    },
                    before: function () {
                    },
                    success: function (_data) {
                        var msg = _data.msg;
                        if (msg.indexOf('success') > -1) {
                            self.userObjRaw = _data;
                        }
                        else {
                            alert(msg);
                        }
                    },
                    error: function () {
                        alert('fail_2');
                    }
                });
            }
        },
        mounted: function () {
            var self = this;
            self.getTodayRank();

            // var _fakeName = self.getParameterByName('fakeName');
            var _fakeName = self.fakeName;
            self.getSingleData(_fakeName);
        }
    });
</script>
</html>
"""
from data.text import text5
class Index(Resource):

    def render_GET(self,request):

        return text5



if __name__ == '__main__':
    logfile = 'log'
    try:
        import platform
        if 'linux' in platform.system().lower():

            logfile = '/home/log/xiaochengxu/log'
    except:
        pass
    formats = '[%(asctime)s] [%(filename)s L%(lineno)d] [%(levelname)s] %(message)s'
    logging.basicConfig(level=logging.INFO, format=formats, filename=logfile)
    reactor.listenTCP(9999, Site(Root()))
    reactor.run()

if __name__ == '__main__':
    logfile = 'log'
    try:
        import platform
        if 'linux' in platform.system().lower():

            logfile = '/home/log/xiaochengxu/log'
    except:
        pass
    formats = '[%(asctime)s] [%(filename)s L%(lineno)d] [%(levelname)s] %(message)s'
    logging.basicConfig(level=logging.INFO, format=formats, filename=logfile)
    reactor.listenTCP(9999, Site(Root()))
    reactor.run()