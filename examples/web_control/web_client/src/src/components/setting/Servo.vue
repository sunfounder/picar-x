<template>
    <div>
        <div class="content">
            <div class="switch-bar">
                <div class="switch-text">
                    Servo Test
                </div>
                <div class="servo-img-ok">
                    <!-- <img class="img-ok" src="../../assets/img/OK.png" alt=""> -->
                </div>
            </div>
            <div class="area">
                <div class="servo-left">
                    <img class="servo-img" src="../../assets/img/servo-img.png" alt="">
                </div>
                <div class="servo-right">
                    <div class="servo-right-title">
                        Deviation Value
                    </div>
                    <div class="servo-right-distance">
                        {{servoValue_}}
                    </div>
                    <div class="servo-right-controll">
                        <div style="width:50%;height:100%;display:inline-block" @click="handleLeftClick">
                            <img class="servo-right-controll-img marginRight" src="../../assets/img/gimbaldirection.png"
                                alt="">
                        </div>
                        <div style="width:50%;height:100%;display:inline-block" @click="handleRightClick">
                            <img class="servo-right-controll-img rotate" src="../../assets/img/gimbaldirection.png"
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
        name: 'SettingServo',
        data() {
            return {
                servoValue: 0,
                servoDate: {
                    "DO": ['on', 0]
                },
            }
        },
        computed: {
            ...mapGetters(['msgObj']),
            servoValue_() {
                if (this.msgObj) {
                    return this.msgObj['DO'];
                }
            },
        },
        methods: {
            ...mapActions(['send']),
            handleLeftClick() {
                this.servoValue--
                this.$set(this.servoDate, 'DO', ['on', this.servoValue])
                this.send(JSON.stringify(this.servoDate));
            },
            handleRightClick() {
                this.servoValue++
                this.$set(this.servoDate, 'DO', ['on', this.servoValue])
                this.send(JSON.stringify(this.servoDate));
            },
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

    .servo-img-ok {
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

    .servo-left {
        width: 50%;
        text-align: center;
    }

    .servo-right {
        width: 50%;
        text-align: center;
    }

    .servo-img {
        width: 65%;
    }

    .servo-right-title {
        font-size: 0.6rem;
        color: #ffffff;
        text-align: center;
        margin-top: 0.3rem;
    }

    .servo-right-distance {
        display: inline-block;
        padding: 0.3rem .8rem;
        background: #ffffff;
        text-align: center;
        margin-top: .3rem;
    }

    .servo-right-controll {
        margin-top: .3rem;
    }

    .servo-right-controll-img {
        width: 90%;
    }

    .marginRight {
        margin-right: .12rem;
    }

    .rotate {
        transform: rotate(180deg);
        margin-left: .12rem;
    }
</style>