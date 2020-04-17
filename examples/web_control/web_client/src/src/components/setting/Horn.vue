<template>
    <div>
        <div>
            <div class="switch-bar">
                <div class="switch-text">
                    喇叭测试开关
                </div>
                <div class="wheel-img">
                    <!-- <img class="img-ok" src="../../assets/img/OK.png" alt=""> -->
                </div>
            </div>
            <div class="area">
                <div class="wrapper">
                    <div class="content">
                        <ul class="list border-right">
                            <li @click="handleItemClick($event,index)" class="item" v-for="(item, index) of musicList"
                                :key="item.id">
                                <div class="item-img">
                                    <img class="item-img-content" :src="item.imgUrl" alt="">
                                </div>
                                <p class="item-desc">{{item.text}}</p>
                                <div style="display:none"  ref="musicHandler">
                                    <div @click="handleRecClick(index)" class="item positionDivAu">
                                        <div class="item-img">
                                            <img class="item-img-content" src="../../assets/img/audio.png"
                                                alt="">
                                        </div>
                                        <p class="item-desc">录音</p>
                                    </div>
                                    <div @click="handlePlayClick(index)" class="item positionDivPy">
                                        <div class="item-img">
                                            <img ref="imgContent" class="item-img-content" src="../../assets/img/Soundeffects.png"
                                                alt="">
                                        </div>
                                        <p class="item-desc">播放</p>
                                    </div>
                                </div>
                            </li>
                        </ul>
                        <div class="volumn border-topright">
                            <div class="volumn-icon">
                                <img class="volumn-icon-img" src="../../assets/img/volumn-icon.png" alt="">
                            </div>
                            <vue-slider v-model="value">
                                <template v-slot:dot>
                                    <img src="../../assets/img/volumn-controll-icon.png" class="custom-dot" />
                                </template>
                            </vue-slider>
                        </div>
                    </div>
                    <div class="menu">
                        <div class="menu-arrow-up menu-height">
                        </div>
                        <div class="menu-icon">
                            <img class="menu-img" src="../../assets/img/menu-luying.png" alt="">
                        </div>
                        <div class="menu-arrow-down menu-height">
                        </div>
                    </div>
                </div>
            </div>
        </div>
        <Confirm v-model="isConfirmShow" :data="confirm" @ok="ok" @cancel="cancel" />
    </div>
</template>

<script>
    import VueSlider from 'vue-slider-component'
    import 'vue-slider-component/theme/default.css'
    import Recorder from 'recorder-core/recorder.mp3.min'
    import axios from 'axios'
    // import { mapState, mapGetters, mapActions } from 'vuex'
    import {
        mapState,
        mapGetters,
        mapActions
    } from 'vuex'
    export default {
        name: 'SettingHorn',
        components: {
            VueSlider,
        },
        data() {
            return {
                audioImg0: require('../../assets/img/audio.png'),
                audioImg1: require('../../assets/img/audio.png'),
                audioImg2: require('../../assets/img/audio.png'),
                audioImg3: require('../../assets/img/audio.png'),
                audioImg4: require('../../assets/img/audio.png'),
                isConfirmShow: false,
                confirm: {
                    title: 'tip',
                    content: `正在录音...最长10秒`,
                    confirmBtn: '确定',
                    cancelBtn: "取消"
                },
                timer: null,
                value: 30,
                rec: null,
                musicList: [{
                    id: '0001',
                    imgUrl: require('../../assets/img/audio.png'),
                    text: 'music1'
                }, {
                    id: '0002',
                    imgUrl: require('../../assets/img/audio.png'),
                    text: 'music2'
                }, {
                    id: '0003',
                    imgUrl: require('../../assets/img/audio.png'),
                    text: 'music3'
                }, {
                    id: '0004',
                    imgUrl: require('../../assets/img/audio.png'),
                    text: 'music4'
                }, {
                    id: '0005',
                    imgUrl: require('../../assets/img/audio.png'),
                    text: 'music5'
                }],
                fileIndex: 0,
                "SL": {"SL": ['on', 0, 0]},
                date: 10
            }
        },
        computed: {
            ...mapGetters(['msgObj']),
            fileAdress() {
                if (this.msgObj) {
                    return this.msgObj['FD']
                }
            },
        },
        methods: {
            ...mapActions(['send']),
            recopen(success) {
                this.rec = Recorder({
                    type: "mp3",
                    sampleRate: 44100,
                    bitRate: 128 //mp3格式，指定采样率hz、比特率kbps，其他参数使用默认配置；注意：是数字的参数必须提供数字，不要用字符串；需要使用的type类型，需提前把格式支持文件加载进来，比如使用wav格式需要提前加载wav.js编码引擎
                        ,
                    onProcess: function (buffers, powerLevel, bufferDuration, bufferSampleRate, newBufferIdx,
                        asyncEnd) {
                        //录音实时回调，大约1秒调用12次本回调
                        //可利用extensions/waveview.js扩展实时绘制波形
                        //可利用extensions/sonic.js扩展实时变速变调，此扩展计算量巨大，onProcess需要返回true开启异步模式
                    },
                });

                this.rec.open(() => { //打开麦克风授权获得相关资源
                    // dialog&&dialog.Cancel(); 如果开启了弹框，此处需要取消
                    //rec.start() 此处可以立即开始录音，但不建议这样编写，因为open是一个延迟漫长的操作，通过两次用户操作来分别调用open和start是推荐的最佳流程

                    success && success();
                }, function (msg, isUserNotAllow) { //用户拒绝未授权或不支持
                    //dialog&&dialog.Cancel(); 如果开启了弹框，此处需要取消
                    console.log((isUserNotAllow ? "UserNotAllow，" : "") + "无法录音:" + msg);
                });
            },
            recStart() {
                this.isConfirmShow = true;
                this.rec.start();
            },
            recStop(index) {
                this.rec.stop((blob, duration) => {
                    console.log(blob, "时长:" + duration + "ms");
                    let form = new FormData();
                    console.log(this.fileIndex)
                    form.append("upfile", blob, `${this.fileIndex}.mp3`);
                    axios.post(this.fileAdress, form).then((data) => {
                        // console.log(this.$refs.imgContent[this.fileIndex - 1].src)
                        this.$set(this.musicList[this.fileIndex - 1], 'imgUrl', require('../../assets/img/menu-luying.png'))
                        // this.musicList[this.fileIndex - 1] = require('../../assets/img/menu-luying.png')
                        console.log(data);
                        this.rec.close();
                        this.rec = null;
                        this.isConfirmShow = false;
                    }).catch((e) => {
                        this.$set(this.musicList[this.fileIndex - 1], 'imgUrl', require('../../assets/img/menu-luying.png'))
                        // this.audioImg[this.fileIndex - 1] = require('../../assets/img/audio.png')                        
                        console.log(e);
                        this.rec.close();
                        this.rec = null;
                        this.isConfirmShow = false
                    })
                }, (msg) => {
                    console.log("录音失败:" + msg);
                    this.rec.close(); //可以通过stop方法的第3个参数来自动调用close
                    this.rec = null;
                });
            },
            recBreak() {
                this.rec.stop((blob, duration) => {
                    // console.log(blob, "时长:" + duration + "ms");
                    this.rec.close(); //释放录音资源，当然可以不释放，后面可以连续调用start；但不释放时系统或浏览器会一直提示在录音，最佳操作是录完就close掉
                    this.rec = null;
                }, (msg) => {
                    console.log("录音失败:" + msg);
                    this.rec.close(); //可以通过stop方法的第3个参数来自动调用close
                    this.rec = null;
                });
            },
            handleItemClick(e,index) {
                // this.$refs.musicHandler.forEach((item, key)=> {
                //     item.style.display = 'none'
                // })
                let element = this.$refs.musicHandler[index]
                console.log(element.style)
                console.log(element.style.cssText)
                element.style.display = element.style.display == "none" ? "block": "none";
            },
            handleRecClick (index) {
                this.fileIndex = parseInt(index) + 1
                this.recopen(() => {
                    this.recStart();
                    this.timer = setTimeout(() => {
                        this.recStop()
                    }, 10000);
                })
            },
            ok() {
                this.isConfirmShow = false
                this.recStop()
                clearTimeout(this.timer)
            },
            cancel() {
                this.isConfirmShow = false;
                this.recBreak()
                clearTimeout(this.timer)
            },
            handlePlayClick (index) {
                let value = this.value / 100 
                this.$set(this['SL'], 'SL', ['on', index, value])
                this.send(JSON.stringify(this["SL"]));
            }
        },
    }
</script>

<style scoped>
    .switch-bar {
        height: .8rem;
        background: #19497d;
        display: flex;
        box-sizing: border-box;
        padding: 0 .3rem;
        justify-content: space-between;
    }

    .switch-text {
        line-height: 0.8rem;
        color: #ffffff;
    }
    .displayObj{
        display: none;
    }

    .wheel-img {
        line-height: 0.8rem;
    }

    .img-ok {
        width: 1.07rem;
        height: .47rem;
        position: relative;
        top: 0;
        left: 0;
    }

    .area {
        padding: .2rem;
        background: #063261;
        margin-top: 2rem;
        position: relative;
        display: flex;
    }

    .wrapper {
        width: 100%;
        height: 100%;
        display: flex;
    }

    .content {
        width: 80%;
        /* overflow: hidden; */
        display: flex;
        flex-direction: column;
    }

    .list {
        /* overflow: hidden; */
    }

    .item {
        width: 20%;
        position: relative;
        /* overflow: hidden; */
        padding-bottom: 25%;
        float: left;
        height: 0;
        position: relative;
    }

    .positionDivAu {
        position: absolute;
        top: -1rem;
        padding-bottom: 70%;
        width: 100%;
    }

    .positionDivPy {
        position: absolute;
        top: -2rem;
        padding-bottom: 70%;
        width: 100%;
    }

    .item-img {
        position: absolute;
        top: 0;
        left: 0;
        bottom: .44rem;
        right: 0;
        box-sizing: border-box;
        padding: .05rem;
    }

    .item-img-content {
        height: 100%;
        display: block;
        margin: 0 auto;
    }

    .item-desc {
        position: absolute;
        right: 0;
        left: 0;
        bottom: 0;
        height: .4rem;
        line-height: .4rem;
        color: #fff;
        text-align: center;
        font-size: .12rem;
    }

    .volumn {
        flex: 1;
        box-sizing: border-box;
        padding: .1rem .1rem 0 .4rem;
        position: relative;

    }

    .volumn-icon {
        position: absolute;
        left: 0.03rem;
        top: .1rem;
    }

    .volumn-icon-img {
        width: 80%;
    }

    .custom-dot {
        width: 100%;
    }

    .menu {
        flex: 1;
        display: flex;
        flex-direction: column;
    }

    .menu-height {
        height: 25%;
        text-align: center;
    }

    .menu-icon {
        height: 50%;
        text-align: center;
    }

    .menu-img {
        height: 100%;
    }

    .menu-img-rotate {
        transform: rotate(180deg);
    }
</style>