<template>
    <div>
        <div class="content">
            <div class="switch-bar">
                <div class="fimbal-switch">
                    Left & Right Test
                    <div class="distance-number">{{leftRightGimbal_}}</div>
                    mm
                </div>
                <div class="distance">
                    Up & Down Test
                    <div class="distance-number">{{upDownGimbal_}}</div>
                    mm
                </div>
                <div class="distance-img">
                    <!-- <img @click="handleGimbalOnOff" class="img-ok" src="../../assets/img/OK.png" alt=""> -->
                </div>
            </div>
            <div class="area">
                <div class="area-left">
                    <div class="area-img-content">
                        <img class="area-img" src="../../assets/img/carModelLookDown.png" alt="">
                    </div>
                    <div class="area-controll-left">
                        <div class="area-controll-img-content">
                            <div @click="handleLeftClick">
                                <img class="area-controll-img" src="../../assets/img/gimbaldirection.png" alt="">
                            </div>
                            <div @click="handleRightClick">
                                <img class="area-controll-img rotate" src="../../assets/img/gimbaldirection.png" alt="">
                            </div>
                        </div>
                    </div>
                </div>
                <div class="area-right">
                    <div class="area-right-img-content">
                        <img class="area-img" src="../../assets/img/carModelLookRight.png" alt="">
                    </div>
                    <div class="area-right-controll-img-content">
                        <div @click="handleUpClick" class="alignCenter">
                            <img class="area-right-controll-img rotataFourFive"
                                src="../../assets/img/gimbaldirection.png" alt="">
                        </div>
                        <div @click="handleDownClick" class="alignCenter">
                            <img class="area-right-controll-img rotate2" src="../../assets/img/gimbaldirection.png"
                                alt="">
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
    import {
        mapState,
        mapActions,
        mapGetters,
    } from 'vuex'
    export default {
        name: 'SettingGimbal',
        data() {
            return {
                upDownData: {
                    "TO": ['on', 0]
                },
                upDownGimbal: 0,
                leftRightGimbal: 0,
                leftRightData: {
                    "PO": ['on', 0]
                },
            }
        },
        computed: {
            ...mapGetters(['msgObj']),
            upDownGimbal_() {
                if (this.msgObj) {
                    return this.msgObj['TO'];
                }
            },
            leftRightGimbal_() {
                if (this.msgObj) {
                    return this.msgObj['PO']
                }
            }
        },
        methods: {
            ...mapActions(['send']),
            handleUpClick() {
                this.upDownGimbal++
                this.$set(this.upDownData, 'TO', ['on', this.upDownGimbal])
                this.send(JSON.stringify(this.upDownData));
            },
            handleDownClick() {
                this.upDownGimbal--;
                this.$set(this.upDownData, 'TO', ['on', this.upDownGimbal])
                this.send(JSON.stringify(this.upDownData));
            },
            handleLeftClick() {
                this.leftRightGimbal--
                this.$set(this.leftRightData, 'PO', ['on', this.leftRightGimbal])
                this.send(JSON.stringify(this.leftRightData));
            },
            handleRightClick() {
                this.leftRightGimbal++
                this.$set(this.leftRightData, 'PO', ['on', this.leftRightGimbal])
                this.send(JSON.stringify(this.leftRightData));
            },
            handleGimbalOnOff() {

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

    .fimbal-switch {
        float: left;
        line-height: .8rem;
        color: #fff;
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
        margin-top: .4rem;
        position: relative;
        display: flex;
    }

    .area-left {
        width: 50%;
        overflow: hidden;
        display: flex;
    }

    .area-img-content {
        overflow: hidden;
        padding-bottom: 100%;
        height: 0;
        width: 60%;
    }

    .area-img {
        width: 100%;
    }

    .area-controll-left {
        flex: 1;
        box-sizing: border-box;
        padding-left: 0.2rem;
    }

    .area-controll-img {
        width: 90%;
    }

    .area-controll-img-content {
        display: flex;
        flex-direction: column;
        justify-content: space-around;
        height: 100%;
    }

    .rotate2 {
        transform: rotate(270deg);
    }

    .rotate {
        transform: rotate(180deg);
    }

    .rotataFourFive {
        transform: rotate(90deg);
    }

    .area-right {
        width: 50%;
        overflow: hidden;
        display: flex;
        flex-direction: column;
    }

    .area-right-img-content {
        overflow: hidden;
        padding-bottom: 55.5%;
        height: 0;
        width: 100%;
    }

    .area-right-controll-img-content {
        flex: 1;
        display: flex;
        justify-content: space-around;
    }

    .area-right-controll-img {
        width: 65%;
    }

    .alignCenter {
        text-align: center;
        box-sizing: border-box;
        padding-top: .25rem;
    }
</style>