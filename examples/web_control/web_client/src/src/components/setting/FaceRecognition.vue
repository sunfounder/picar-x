<template>
    <div>
        <div class="content">
            <div class="switch-bar">
                <div class="face-switch">
                    <span class="text">Face Detection Switch</span>
                    <div style="display:inline-block" @click="handleFaceClick">
                        <img class="switch-img-on" :src="faceImgOnOrOff" alt="">
                    </div>
                </div>
                <div class="color-switch">
                    <span class="text">Color Detection Switch</span>
                    <div style="display:inline-block" @click="handleColorClick">
                        <img class="switch-img-on" :src="colorImgOnOrOff" alt="">
                    </div>
                    <div class="color-list" @click="handleColorChangeClick">
                        <span class="color-text">{{color_}}</span>
                        <ul class="choose-color" v-show="isColorShow">
                            <li @click="handleChooseClick(item.text)" class="item" v-for="item of colorList"
                                :key="item.id" :style="item.background">
                                {{item.text}}</li>
                        </ul>
                    </div>
                </div>
            </div>
            <div class="area">
                <div class="area-img">
                    <img class="area-img-video" :src="videoSrc" alt="">
                </div>
                <div class="full-btn"  @click="handleFullClick">
                    <img src="../../assets/img/fullscreen.png" alt="">
                </div>
            </div>
        </div>
        <Fullscreen @hidden="handleHidden" v-if='isShow'></Fullscreen>
    </div>
</template>

<script>
    import {
        mapState,
        mapGetters,
        mapActions
    } from 'vuex'
    import Fullscreen from '@/components/common/Fullscreen'
    export default {
        name: 'SettingFaceRecognition',
        components: {
            Fullscreen
        },
        data() {
            return {
                ...mapState(['color']),
                isShow: false,
                isColorShow: false,
                colorList: [{
                    id: '0001',
                    background: "background:blue",
                    text: 'blue'
                }, {
                    id: '0002',
                    background: "background:red",
                    text: 'red'
                }, {
                    id: '0003',
                    background: "background:green",
                    text: 'green'
                }, {
                    id: '0004',
                    background: "background:yellow",
                    text: 'yellow'
                }, {
                    id: '0005',
                    background: "background:orange",
                    text: 'orange'
                }, {
                    id: '0006',
                    background: "background:purple",
                    text: 'purple'
                }, ],
                faceFlag: true,
                faceData: {
                    "HT": 'on'
                },
                colorFlag: true,
                colorData: {
                    "CT": 'on',
                },
                defaultColor: {
                    'CC': 'blue'
                },
                faceImgOnOrOff: require('../../assets/img/OFF.png'),
                colorImgOnOrOff: require('../../assets/img/OFF.png')
            }
        },
        computed: {
            ...mapGetters(['msgObj', 'color_']),
            videoSrc() {
                if (this.msgObj) {
                    return this.msgObj['AD']
                }
            },
        },
        methods: {
            ...mapActions(['send', 'changeColor']),
            handleColorChangeClick() {
                this.isColorShow = !this.isColorShow
            },
            handleFaceClick() {
                if (this.msgObj && this.faceFlag == true) {
                    this.faceImgOnOrOff = require('../../assets/img/ON.png')
                    this.send(JSON.stringify(this.faceData));
                    this.$set(this.faceData, 'HT', 'off')
                    this.faceFlag = false

                } else {
                    this.faceImgOnOrOff = require('../../assets/img/OFF.png')
                    this.send(JSON.stringify(this.faceData));
                    this.$set(this.faceData, 'HT', 'on')
                    this.faceFlag = true

                }
            },
            handleColorClick() {
                if (this.colorFlag == true) {
                    this.colorImgOnOrOff = require('../../assets/img/ON.png')
                    this.send(JSON.stringify(this.colorData))
                    this.$set(this.colorData, 'CT', 'off')
                    this.colorFlag = false

                } else {
                    this.colorImgOnOrOff = require('../../assets/img/OFF.png')
                    this.send(JSON.stringify(this.colorData))
                    this.$set(this.colorData, 'CT', 'on')
                    this.colorFlag = true

                }
            },
            handleChooseClick(text) {
                console.log(text);
                this.changeColor(text)
                this.$set(this.defaultColor, 'CC', text)
                this.send(JSON.stringify(this.defaultColor))
            },
            handleFullClick() {
                this.isShow = true
            },
            handleHidden(hidden) {
                this.isShow = hidden;
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
    }

    .text {
        display: inline-block;
        margin-right: .3rem;
        color: #fff;
    }

    .face-switch {
        float: left;
        line-height: .8rem;
    }

    .switch-img-on {
        width: .96rem;
        height: .39rem;
        position: relative;
        top: -2px;
        left: 0;
    }

    .color-switch {
        float: right;
        line-height: .8rem;
        flex: 1;
        box-sizing: border-box;
        padding-left: 3%;
    }

    .color-list {
        width: 1.3rem;
        height: .5rem;
        border-radius: 0.08rem;
        background: #fff;
        float: right;
        margin-top: 0.12rem;
        line-height: .5rem;
        box-sizing: border-box;
        padding: 0 .1rem;
        position: relative;
    }

    .choose-color {
        position: absolute;
        top: 110%;
        border: 1px solid #cccccc;
        background: #fff;
        width: 100%;
        left: 0;
        border-radius: 0.08rem;
        z-index: 2;
    }

    .item {
        line-height: 0.5rem;
        height: .5rem;
        box-sizing: border-box;
        padding: 0.05rem;
        /* border-radius: .08rem; */
        color: #fff;
    }

    .area {
        padding: .2rem;
        background: #063261;
        margin-top: .4rem;
        position: relative;
    }

    .area-img {
        height: 0;
        overflow: hidden;
        padding-bottom: 50%;
        background: #10243b
    }

    .full-btn {
        position: absolute;
        bottom: .3rem;
        right: .3rem;
    }

    .area-img-video {
        width: 100%;
    }
</style>