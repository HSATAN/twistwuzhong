# _*_ coding:utf-8 _*_


# _*_ coding:utf-8 _*_

default_html = """
<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <meta name="viewport"
          content="width=device-width, user-scalable=no, initial-scale=1.0, maximum-scale=1.0, minimum-scale=1.0">
    <title>茅坝中学健康运动</title>
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
    <style>
        .text-left {
            text-align: left;
        }

        .text-center {
            text-align: center;
        }

        .text-black-hint {
            color: #9a9a9a;
        }

        .step-available .info {
            position: relative;
        }

        .step-available .info .now-step-wrap .now-step-content-f {
            position: absolute;
            vertical-align: middle;
            text-align: center;
            width: 100%;
            top: 33%;
            font-size: 0.5em;
            line-height: 1rem;
        }

        .step-available .info .now-step-wrap .now-step-content-s {
            position: absolute;
            vertical-align: middle;
            text-align: center;
            width: 100%;
            bottom: 34%;
            font-size: 0.5em;
            line-height: 1rem;
        }

        /*修改stepper的颜色*/
        .stepper.active .stepper-step:before, .stepper.done .stepper-step:before {
            background-color: #4caf50;
        }

        .now-step-radius {
            margin-bottom: -0.5em;
        }
    </style>
</head>
<body>
<div id="app">
    <div class="container">
        <div class="columns">
            <div class="column col-12">
                <blockquote>
                    教师运动情况统计
                </blockquote>

            </div>
            <div class="column col-12">
                <blockquote>
                    数据一小时更新一次
                </blockquote>

            </div>
        </div>
    </div>
    <div class="container">
        <div class="columns">
            <div class="column col-12">
                <blockquote>
                    排行榜
                </blockquote>
                <ul class="tab tab-block">
                    <li class="tab-item" :class="tabSelected==='today'?'active':''">
                        <a href="javascript:void(0);" @click="tabChange('today')">今日</a>
                    </li>
                    <li class="tab-item" :class="tabSelected==='week'?'active':''">
                        <a href="javascript:void(0);" @click="tabChange('week')">本周</a>
                    </li>
                </ul>
                <table class="table table-striped table-hover" style="font-size: 0.5em;" v-show="tabSelected==='today'">
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
                        <td colspan="5">
                            <hr/>
                        </td>
                    </tr>
                    <tr v-for="(item, index) in orderedTodayRank" :key="item.fakeName">
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
                <table class="table table-striped table-hover" style="font-size: 0.5em;" v-show="tabSelected==='week'">
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
                        <td colspan="5">
                            <hr/>
                        </td>
                    </tr>
                    <tr v-for="(item, index) in orderedWeekRank" :key="item.fakeName">
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
    "use strict";
    var app = new Vue({
        el: '#app',
        data: {
            todayRank: [],
            allData: [],
            userObjRaw: {},
            //TODO 改动
            fakeName: '1Xh8.PTww',

            //TODO 改动


            serverConfig: {
                baseUrl: 'http://wxs.grplpl.com/',
                // baseUrl: 'http://wxs.testhost.com:3000/',
                projectID: 'hrmbzx',
                salt: 'ayf59mgqre4jibc3',
            },
            tabSelected: 'today',
            db: null,
        },
        computed: {
            orderedTodayRank: function () {
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
                        date: '',
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
                var _date = '(暂无数据)';
                if (_list && _list.length > 0) {
                    _list = JSON.parse(self.userObjRaw.list);
                    _list = _.orderBy(_list, ['dateString'], ['desc']);
                    _score = _list[0].scoreNow;
                    _star = _list[0].starNow;
                    _tsString = moment.unix(_list[0].timeStamp / 1000).format('YYYY-MM-DD HH:mm:ss');
                    _date = moment.unix(_list[0].timeStamp / 1000).format('YYYY-MM-DD');
                }

                self.showBigIndicator(_score);

                return {
                    head: _head,
                    nickName: self.userObjRaw.nickName,
                    scoreNow: _score,
                    starNow: _star,
                    tsString: _tsString,
                    date: _date,
                };
            },
            userTodayRankObj: function () {
                var self = this;
                if (!self.orderedTodayRank || self.orderedTodayRank.length === 0) {
                    return {};
                }

                var _index = _.findIndex(self.orderedTodayRank, function (_obj) {
                    return _obj.fakeName === self.fakeName;
                });
                if (_index === -1) {
                    return {};
                }
                else {
                    return {
                        index: _index,
                        head: self.orderedTodayRank[_index].head,
                        nickName: self.orderedTodayRank[_index].nickName,
                        scoreNow: self.orderedTodayRank[_index].scoreNow,
                        starNow: self.orderedTodayRank[_index].starNow,
                    }
                }
            },
            orderedWeekRank: function () {
                var self = this;
                if (!self.allData || self.allData.length === 0) {
                    return [];
                }

                var _startDateString = moment().startOf('week').format('YYYYMMDD');
                var _endDateString = moment().endOf('week').format('YYYYMMDD');
                //TODO 改动
                // var _startDateString = moment(1514221200000).startOf('week').format('YYYYMMDD'); //2017-12-26 那周，开始25 结束31
                // var _endDateString = moment(1514221200000).endOf('week').format('YYYYMMDD');
                var _len = self.allData.length;
                var _mainList = [];
                for (var i = 0; i < _len; i++) {
                    var _obj = self.allData[i];
                    var _list = _obj.list;
                    var _len2 = _list.length;
                    var _total = 0;
                    var _totalStar = 0;
                    for (var j = 0; j < _len2; j++) {
                        var _dateString = _list[j].dateString;
                        if (_startDateString <= _dateString && _dateString <= _endDateString) {
                            _total = _total + _list[j].scoreNow;
                            _totalStar = _list[j].starNow ? _totalStar + _list[j].starNow : 0;
                        }
                    }

                    _mainList.push({
                        fakeName: _obj.fakeName,
                        nickName: _obj.nickName,
                        head: self.serverConfig.baseUrl
                        + 'getSingleHeadImage_v4?projectID=' + self.serverConfig.projectID
                        + '&salt=' + self.serverConfig.salt
                        + '&fakeName=' + _obj.fakeName,
                        scoreNow: _total,
                        starNow: _totalStar
                    });
                }
                return _.orderBy(_mainList, ['scoreNow'], ['desc']);
            },
            userWeekRankObj: function () {
                var self = this;
                if (!self.orderedWeekRank || self.orderedWeekRank.length === 0) {
                    return {};
                }

                var _index = _.findIndex(self.orderedWeekRank, function (_obj) {
                    return _obj.fakeName === self.fakeName;
                });
                if (_index === -1) {
                    return {};
                }
                else {
                    return {
                        index: _index,
                        head: self.orderedWeekRank[_index].head,
                        nickName: self.orderedWeekRank[_index].nickName,
                        scoreNow: self.orderedWeekRank[_index].scoreNow,
                        starNow: self.orderedWeekRank[_index].starNow,
                    }
                }
            },
        },
        methods: {
            getTodayRank: function () {
                var self = this;
                var _date = moment().format('YYYYMMDD'); //今天的日期字符串
                // var _date = '20171217';

                $.ajax({
                    type: "post",
                    url: self.serverConfig.baseUrl + 'getDataByDate_v4/',
                    timeOut: 100000,
                    data: {
                        projectID: self.serverConfig.projectID,
                        salt: self.serverConfig.salt,
                        date: _date,
                        isZipped: 1, //打开压缩开关
                    },
                    before: function () {
                    },
                    success: function (_data) {
                        var msg = _data.msg;
                        if (msg.indexOf('success') > -1) {
                            //解压并转换JSON
                            self.todayRank = JSON.parse(pako.ungzip(_data.list, {to: 'string'}));
                            self.saveTodayRank(_date, _data.list);
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
                        isZipped: 1, //打开压缩开关
                    },
                    before: function () {
                    },
                    success: function (_data) {
                        var msg = _data.msg;
                        if (msg.indexOf('success') > -1) {
                            self.userObjRaw = _data;
                            var _zippedList = _data.list;
                            self.userObjRaw.list = pako.ungzip(_data.list, {to: 'string'});
                            self.saveSingleData(_data.fakeName, _data.nickName, _zippedList);
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
            showBigIndicator: function (_stepCount) {
                $("#nowStep").empty();

                _stepCount = _stepCount ? _stepCount : 0;
                var bigOption = {
                    radius: 80, //内环半径宽度
                    barWidth: 34, //外环宽度
                    fontColor: '#4caf50',//字体颜色
                    fontSize: 35,
                    minValue: 0,
                    maxValue: 10000,
                    roundCorner: true,
                    displayNumber: true,
                    barColor: {
                        0: '#F5FDCA',
                        2500: '#FFE767',
                        5000: '#FEC43E',
                        7500: '#8DCD9B',
                        10000: '#4caf50'
                    },
                    format: function () {
                        return _stepCount;
                    }
                };
                var bigRadius = radialIndicator('#nowStep', bigOption);
                bigRadius.animate(_stepCount);
            },
            getDataAll: function () {
                var self = this;
                $.ajax({
                    type: "post",
                    url: self.serverConfig.baseUrl + 'getDataAll_v4/',
                    timeOut: 100000,
                    data: {
                        projectID: self.serverConfig.projectID,
                        salt: self.serverConfig.salt,
                        isZipped: 1, //打开压缩开关
                    },
                    before: function () {
                    },
                    success: function (_data) {
                        var msg = _data.msg;
                        if (msg.indexOf('success') > -1) {
                            self.allData = JSON.parse(pako.ungzip(_data.list, {to: 'string'}));
                            self.saveAllData(_data.list);
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
            tabChange: function (_tab) {
                var self = this;
                self.tabSelected = _tab;
            },
            saveFakeName: function (_fakeName) {
                var self = this;
                self.db.fakeName
                    .put({id: 1, fakeName: _fakeName})
                    .then(function () {
                        self.db.updateTS.update(1, {fakeName: _.now()});
                    });
            },
            loadFakeName: function () {
                var self = this;
                self.db.fakeName.toArray(function (_arr) {
                    if (_arr && _arr.length > 0) {
                        self.fakeName = _arr[0].fakeName;
                    }
                });
            },
            saveTodayRank: function (_dateString, _dataZipped) {
                var self = this;
                self.db.todayRank
                    .put({id: 1, dateString: _dateString, dataZipped: _dataZipped})
                    .then(function () {
                        self.db.updateTS.update(1, {toadyRank: _.now()});
                    });
            },
            loadTodayRank: function () {
                var self = this;
                self.db.todayRank.toArray(function (_arr) {
                    if (_arr && _arr.length > 0) {
                        self.todayRank = JSON.parse(pako.ungzip(_arr[0].dataZipped, {to: 'string'}));
                    }
                });
            },
            saveSingleData: function (_fakeName, _nickName, _dataZipped) {
                var self = this;
                self.db.singleData
                    .put({id: 1, fakeName: _fakeName, nickName: _nickName, dataZipped: _dataZipped})
                    .then(function () {
                        self.db.updateTS.update(1, {singleData: _.now()});
                    });
            },
            loadSingleData: function () {
                var self = this;
                self.db.singleData.toArray(function (_arr) {
                    if (_arr && _arr.length > 0) {
                        self.userObjRaw = {
                            fakeName: _arr[0].fakeName,
                            nickName: _arr[0].nickName,
                            list: pako.ungzip(_arr[0].dataZipped, {to: 'string'})
                        };
                    }
                });
            },
            saveAllData: function (_dataZipped) {
                var self = this;
                self.db.allData
                    .put({id: 1, dataZipped: _dataZipped})
                    .then(function () {
                        self.db.updateTS.update(1, {allData: _.now()});
                    });
            },
            loadAllData: function () {
                var self = this;
                self.db.allData.toArray(function (_arr) {
                    if (_arr && _arr.length > 0) {
                        self.allData = JSON.parse(pako.ungzip(_arr[0].dataZipped, {to: 'string'}));
                    }
                });
            },
            initUpdateTS: function () {
                var self = this;
                self.db.updateTS.where('id').equals(1).toArray(function (_arr) {
                    if (!_arr || _arr.length === 0) {
                        self.db.updateTS.put({
                            id: 1,
                            fakeName: -1,
                            ToadyRank: -1,
                            singleData: -1,
                            allData: -1,
                        });
                    }
                });
            }
        },
        mounted: function () {
            var self = this;

            /* 实操上是先从Url获取是否存在fakeName字段，
                若没有则查找本地数据库是否有保存fakeName数据
                若还是没有则弹出计步器Bot的二维码，提示关注计步器并回复任意内容，
            以触发计步器回复一个带fakeName的Url过来，此Url即为用户的个人Url。  */

            // 从Url获取fakeName的代码
            // var _fakeName = self.getParameterByName('fakeName');

            //初始化数据库和建表，具体请去GitHub搜索Dexie以了解Dexie的详细用法。
            self.db = new Dexie('testdb5');
            self.db.version(1).stores({
                updateTS: 'id,fakeName,toadyRank,singleData,allData', //保存几个离线数据表的上次更新时间
                fakeName: 'id,fakeName',
                todayRank: 'id,dateString,dataZipped',
                singleData: 'id,fakeName,nickName,dataZipped',
                allData: 'id,dataZipped',
            });

            // 从本地数据库获取fakeName的代码。
            // self.loadFakeName();

            var _fakeName = self.fakeName; //演示用
            self.initUpdateTS();

            // 保存fakeName
            self.saveFakeName(_fakeName);

            //加载本地数据库，稍微延迟一点时间
            setTimeout(function () {
                self.loadTodayRank();
                self.loadSingleData();
                self.loadAllData();
            }, 100);

            //延迟5秒后从服务器获取，演示优先载入本地历史数据，秒开的效果。
            setTimeout(function () {
                self.getTodayRank();
                self.getSingleData(_fakeName);
                self.getDataAll();
            }, 5000);
        }
    });
</script>
</html>
"""