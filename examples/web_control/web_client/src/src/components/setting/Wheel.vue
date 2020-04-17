<template>
    <div>
        <div class="content">
            <div class="switch-bar">
                <div class="switch-text">
                    Wheel Test
                </div>
                <div class="wheel-img">
                    <!-- <img class="img-ok" src="../../assets/img/OK.png" alt=""> -->
                </div>
            </div>
            <div class="area">
                <div class="wheel-left">
                    <div class="wheel-left-img-content">
                        <img class="wheel-left-img" src="../../assets/img/wheel-model.png" alt="">
                        <div :style="isRightShow" @click="handleRightClick" class="right-wheel"></div>
                        <div :style="isLeftShow" @click="handleLeftClick" class="left-wheel"></div>
                    </div>
                </div>
                <div class="wheel-center">
                    <div class="wheel-center-title border-bottom">{{wheelTitle}}</div>
                    <!-- <div class="wheel-center-number-title">POWER</div>
                    <div class="wheel-center-number">{{value}}%</div>
                    <div class="wheel-center-slider">
                        <vue-slider v-model="value" :tooltip="'none'">
                            <template v-slot:dot>
                                <img src="../../assets/img/wheel-power-icon.png" class="custom-dot" />
                            </template>
                        </vue-slider>
                    </div> -->
                </div>
                <div class="wheel-right">
                    <ControllJoystick :mode="MS" :wheelData="wheelData" :wheelChoose="wheelChoose"></ControllJoystick>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
    import VueSlider from 'vue-slider-component'
    import 'vue-slider-component/theme/default.css'
    import ControllJoystick from '@/components/common/Joystick'
    import { mapState, mapActions, mapGetters, } from 'vuex'
    export default {
        name: 'SettingWheel',
        components: {
            VueSlider,
            ControllJoystick
        },
        data () {
            return {
                value: 50,
                'MS': 'MS',
                isRightShow: {
                    opacity: 0.5
                },
                isLeftShow: {
                    opacity: 0
                },
                wheelTitle: 'Left rear wheel',
                wheelData: {"MS": ['on',2,0]},
                wheelChoose: 2
            }
        },
        methods: {
            ...mapActions(['send']),
            handleRightClick () {
                this.isRightShow = {
                    opacity: 0.5
                }
                this.isLeftShow = {
                    opacity: 0
                }
                this.wheelTitle = "Right rear wheel"
                this.$set(this.wheelData, 'MS', ['on', 2, 0])
                this.send(JSON.stringify(this.wheelData))
                this.wheelChoose = 2
            },
            handleLeftClick () {
                this.isLeftShow = {
                    opacity: 0.5
                }
                this.isRightShow = {
                    opacity: 0
                }
                this.wheelTitle = 'Left rear wheel'
                this.$set(this.wheelData, 'MS', ['on', 1, 0])
                this.send(JSON.stringify(this.wheelData))
                this.wheelChoose = 1
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
        justify-content: space-between;
    }

    .switch-text {
        line-height: 0.8rem;
        color: #ffffff;
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
        margin-top: .4rem;
        position: relative;
        display: flex;
    }

    .wheel-left {
        width: 40%;
        height: 100%;
        text-align: center;
    }
    .wheel-left-img-content {
        position: relative;
    }

    .right-wheel {
        position: absolute;
        bottom: .66rem;
        padding-bottom: 34%;
        height: 0;
        overflow: hidden;
        background: red;
        width: 16%;
        right: .44rem;
        opacity: 0.5;
    }

    .left-wheel {
        position: absolute;
        bottom: .66rem;
        padding-bottom: 34%;
        height: 0;
        overflow: hidden;
        background: red;
        width: 16%;
        left: .44rem;
        opacity: 0.5;
    }

    .wheel-center {
        width: 25%;
        height: 100%;
        box-sizing: border-box;
        padding: 0.2rem 0 0 0;
    }

    .wheel-right {
        width: 35%;
        height: 100%;
    }

    .wheel-left-img {
        width: 80%;
    }

    .wheel-center-title {
        text-align: center;
        font-size: .48rem;
        color: #ffffff;
        padding: 0.1rem;
    }

    .wheel-center-number-title {
        text-align: center;
        color: #ffffff;
        padding: 0.1rem;
        font-size: .32rem;
    }

    .wheel-center-number {
        text-align: center;
        font-size: .9rem;
        color: #ffffff;
        margin-top: .7rem;
    }

    .wheel-center-slider {
        margin-top: .7rem;
    }
    .custom-dot {
        width: 100%;
        position: relative;
        top: -.1rem;
        left: 0;
    }
    .wheel-right {
        position: relative;
        padding-bottom: 50%;
    }
</style>