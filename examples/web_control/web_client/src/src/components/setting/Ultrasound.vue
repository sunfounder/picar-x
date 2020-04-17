<template>
    <div>
        <div class="content">
            <div class="switch-bar">
                <div class="face-switch">
                    <span class="text">Ultrasonic Test Switch</span>
                </div>
                <div class="distance">
                    Distance:
                    <div class="distance-number">{{distance}}</div>
                    mm
                </div>
                <div @click="handleUsClick" class="distance-img">
                    <img class="switch-img-on" :src="UltrasonicOnOrOff" alt="">
                </div>
            </div>
            <div class="area">
                <div class="area-img-content">
                    <img class="area-img" src="../../assets/img/Ultrasound_dis.png" alt="">
                </div>
            </div>
        </div>
    </div>
</template>

<script>
    import { mapState, mapActions, mapGetters, } from 'vuex'
    export default {
        name: 'SettingUltrasound',
        data () {
            return {
                usData: {'US': 'on'},
                usFlag: true,
                UltrasonicOnOrOff: require('../../assets/img/OFF.png')
            }
        },
        computed: {
            ...mapGetters(['msgObj']),
            distance () {
                if (this.msgObj) {
                    return this.msgObj['US']
                }
            }
        },
        methods: {
            ...mapActions(['send']),
            handleUsClick () {
                if (this.msgObj && this.usFlag) {
                    this.UltrasonicOnOrOff = require('../../assets/img/ON.png')
                    this.send(JSON.stringify(this.usData))
                    this.$set(this.usData, 'US', 'off')
                    this.usFlag = false
                } else {
                    this.UltrasonicOnOrOff = require('../../assets/img/OFF.png')
                    this.send(JSON.stringify(this.usData))
                    this.$set(this.usData, 'US', 'on')
                    this.usFlag = true;
                }
            }
        }
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

    .distance {
        flex: 1;
        color: #fff;
        line-height: 0.8rem;
        box-sizing: border-box;
        text-align: center;
    }

    .distance-number {
        display: inline-block;
        width: 0.8rem;
        height: 0.5rem;
        background: #fff;
        text-align: center;
        color: aqua;
        line-height: .5rem;
    }

    .distance-img {
        line-height: .8rem;
    }

    .switch-img-on {
        width: .96rem;
        height: .39rem;
        position: relative;
        top: -2px;
        left: 0;
    }




    .area {
        padding: .2rem;
        background: #063261;
        margin-top: .4rem;
        position: relative;
    }

    .area-img-content {
        height: 0;
        overflow: hidden;
        padding-bottom: 50%;
        text-align: center;
    }
    .area-img {
        width: 60%;
    }
</style>