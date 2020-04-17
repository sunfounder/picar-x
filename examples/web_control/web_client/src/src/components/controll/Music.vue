<template>
    <div class="wrapper">
        <div class="content">
            <ul class="list border-right">
                <li @click="handlePlayClick(index, item.cate)" class="item" v-for="(item, index) of musicList[imgIndex]"
                    :key="item.id">
                    <div v-show="item.cate !== 'TT'">
                        <div class="item-img">
                            <img class="item-img-content" :src="item.imgUrl" alt="">
                        </div>
                        <p class="item-desc">{{item.text}}</p>
                    </div>
                    <div class="tts" v-show="item.cate == 'TT'">
                        <textarea v-model="ttsValue" class="tts-area"></textarea>
                        <div @click.self="handleTtsClick(item.cate)">
                            <img class="tts-img" :src="item.imgUrl" alt="">
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
            <div @click="handleAdd" class="menu-arrow-up menu-height">
                <img class="menu-img" src="../../assets/img/menu-arrow.png" alt="">
            </div>
            <div class="menu-icon">
                <img class="menu-img" :src="imgList[imgIndex]" alt="">
            </div>
            <div @click="handleSub" class="menu-arrow-down menu-height">
                <img class="menu-img menu-img-rotate" src="../../assets/img/menu-arrow.png" alt="">
            </div>
        </div>
    </div>
</template>

<script>
    import VueSlider from 'vue-slider-component'
    import 'vue-slider-component/theme/default.css'
    import Recorder from 'recorder-core/recorder.mp3.min'
    import axios from 'axios'
    import {
        mapState,
        mapGetters,
        mapActions
    } from 'vuex'
    export default {
        name: 'controllMusic',
        components: {
            VueSlider,
        },
        data() {
            return {
                value: 30,
                rec: null,
                musicList: [
                    [{
                        id: '0001',
                        imgUrl: require('../../assets/img/menu-yingyue.png'),
                        text: 'music1',
                        cate: 'SM'
                    }, {
                        id: '0002',
                        imgUrl: require('../../assets/img/menu-yingyue.png'),
                        text: 'music2',
                        cate: 'SM'
                    }, {
                        id: '0003',
                        imgUrl: require('../../assets/img/menu-yingyue.png'),
                        text: 'music3',
                        cate: 'SM'
                    }, {
                        id: '0004',
                        imgUrl: require('../../assets/img/menu-yingyue.png'),
                        text: 'music4',
                        cate: 'SM'
                    }, {
                        id: '0005',
                        imgUrl: require('../../assets/img/menu-yingyue.png'),
                        text: 'music5',
                        cate: 'SM'
                    }],
                    [{
                        id: '0001',
                        imgUrl: require('../../assets/img/menu-yingxiao.png'),
                        text: 'sound1',
                        cate: 'SS'
                    }, {
                        id: '0002',
                        imgUrl: require('../../assets/img/menu-yingxiao.png'),
                        text: 'sound2',
                        cate: 'SS'
                    }, {
                        id: '0003',
                        imgUrl: require('../../assets/img/menu-yingxiao.png'),
                        text: 'sound3',
                        cate: 'SS'
                    }, {
                        id: '0004',
                        imgUrl: require('../../assets/img/menu-yingxiao.png'),
                        text: 'sound4',
                        cate: 'SS'
                    }, {
                        id: '0005',
                        imgUrl: require('../../assets/img/menu-yingxiao.png'),
                        text: 'sound5',
                        cate: 'SS'
                    }, ],
                    [{
                        id: '0001',
                        imgUrl: require('../../assets/img/play.png'),
                        text: 'tts',
                        cate: 'TT'
                    }]
                ],
                imgList: [
                    require('../../assets/img/menu-yingyue.png'),
                    require('../../assets/img/menu-yingxiao.png'),
                    require('../../assets/img/menu-luying.png'),
                    require('../../assets/img/tts.png'),
                ],
                imgIndex: 0,
                datas: [{
                    "SM": ['off', 0, 0.5]
                }, {
                    'SS': ['off', 0, 0.5]
                }, {
                    'SL': ['off', 0, 0.5]
                }],
                ttsdata: {
                    "TT": ['off', 'you']
                },
                ttsValue: '',
                switchFlag: {
                    'SM': true,
                    'SS': true,
                    'SL': true,
                },
                currentMusic: -1,
            }
        },
        computed: {
            ...mapGetters(['msgObj']),
            fileAdress() {
                if (this.msgObj) {
                    return this.msgObj['FD']
                }
            }
        },
        methods: {
            ...mapActions(['send']),
            handleAdd() {
                this.imgIndex++
                if (this.imgIndex > 2) {
                    this.imgIndex = 0
                }

            },
            handleSub() {
                this.imgIndex--
                if (this.imgIndex < 0) {
                    this.imgIndex = 2
                }

            },
            handleRecClick() {
                this.recopen(() => {
                    this.rec.start();
                    setTimeout(this.recStop, 10000);
                })
            },
            handlePlayClick(index, cate) {
                if (cate == 'TT') {
                    return;
                }
                // this.currentMusic = index
                let value = this.value / 100
                if (cate == 'SM') {
                    if (this.currentMusic == index) {
                        if (this.switchFlag[cate]) {
                            this.currentMusic = index
                            this.$set(this.datas[this.imgIndex], cate, ['on', index, value])
                            this.send(JSON.stringify(this.datas[this.imgIndex]));
                            this.switchFlag[cate] = false;
                            console.log(this.datas[this.imgIndex])
                        } else {
                            this.$set(this.datas[this.imgIndex], cate, ['off', index, value])
                            this.send(JSON.stringify(this.datas[this.imgIndex]));
                            this.switchFlag[cate] = true;
                            console.log(this.datas[this.imgIndex])
                        }
                    } else {
                        this.currentMusic = index
                        this.$set(this.datas[this.imgIndex], cate, ['on', index, value])
                        this.send(JSON.stringify(this.datas[this.imgIndex]));
                        this.switchFlag[cate] = false;
                        console.log(this.datas[this.imgIndex])
                    }

                } else {
                    console.log(this.datas[this.imgIndex])
                    this.$set(this.datas[this.imgIndex], cate, ['on', index, value])
                    this.send(JSON.stringify(this.datas[this.imgIndex]));
                }

            },
            handleTtsClick(cate) {
                let value = this.ttsValue
                this.$set(this.ttsdata, "TT", ['on', value])
                this.send(JSON.stringify(this.ttsdata));
                console.log(this.ttsValue);
            }
        },
    }
</script>

<style scoped>
    .wrapper {
        width: 100%;
        height: 100%;
        display: flex;
    }

    .content {
        width: 80%;
        overflow: hidden;
        display: flex;
        flex-direction: column;
    }

    .list {
        overflow: hidden;
    }

    .item {
        width: 20%;
        position: relative;
        padding-bottom: 25%;
        float: left;
        height: 0;
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

    .tts {
        width: 500%;
        position: absolute;
        padding-bottom: 125%;
        height: 100%;
        display: flex;
    }

    .tts-area {
        width: 80%;
        height: 100%;
        resize: none;
    }

    .tts-img {
        flex: 1;
        height: 80%;
        margin-top: .12rem;
    }
</style>