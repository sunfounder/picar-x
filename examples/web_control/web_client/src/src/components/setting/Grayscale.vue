<template>
    <div>
        <div class="content">
            <div class="switch-bar">
                <div class="switch-text">
                    Grayscale
                </div>
                <div class="servo-img-ok">
                    <!-- <img class="img-ok" src="../../assets/img/OK.png" alt=""> -->
                </div>
            </div>
            <div class="area">
                <div class="input-wrapper">
                    <div class="line">
                        line Reference: <input v-model="line" class="line-input" type="number" />
                    </div>
                    <div class="cliff">
                        cliff Reference: <input v-model="cliff" class="cliff-input" type="number" />
                    </div>
                </div>
                <div class="img-wrapper">
                    <div class="list">
                        <div class="item">
                            <img v-show="isShow1" class="item-img-line" src="../../assets/img/red-warning.png" alt="">
                            <img v-show="isShow1_" class="item-img-cliff" src="../../assets/img/warning.png" alt="">
                        </div>
                        <div class="item">
                            <img v-show="isShow2" class="item-img-line" src="../../assets/img/red-warning.png" alt="">
                            <img v-show="isShow2_" class="item-img-cliff" src="../../assets/img/warning.png" alt="">
                        </div>
                        <div class="item">
                            <img v-show="isShow3" class="item-img-line" src="../../assets/img/red-warning.png" alt="">
                            <img v-show="isShow3_" class="item-img-cliff" src="../../assets/img/warning.png" alt="">
                        </div>
                    </div>
                    <div class="number-list">
                        <div class="number paddingLeft">Grayscale value:{{gsData[0]}}</div>
                        <div class="number paddingLeft">Grayscale value:{{gsData[1]}}</div>
                        <div class="number">Grayscale value:{{gsData[2]}}</div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
    import {
        mapState,
        mapGetters,
        mapActions,
        mapMutations
    } from 'vuex'
    export default {
        name: 'SettingGrayscale',
        data() {
            return {
                "TL": {"TL": ['off', 950]},
                "CD": {"CD": ['off', 110]},
                "GS": {"GS": 'on'},
                line: 950,
                cliff: 110,
                gsValue0: 0,
                gsValue1: 0,
                gsValue2: 0
            }
        },
        computed: {
            ...mapGetters(['msgObj']),
            gsData () {
                if (this.msgObj) {
                    this.gsValue0 = this.msgObj['GS'][0]
                    this.gsValue1 = this.msgObj['GS'][1]
                    this.gsValue2 = this.msgObj['GS'][2]
                    return this.msgObj["GS"]
                }else {
                    this.gsValue0 = 0
                    this.gsValue1 = 0
                    this.gsValue2 = 0
                    return [0, 0, 0]
                }
            },
            isShow1 () {
                if ((this.line > this.gsData[0]) && this.gsData[0] > this.cliff) {
                    return true
                }else {
                    return false
                }
            },
            isShow1_ () {
                if (this.cliff > this.gsData[0]) {
                    return true
                }else {
                    return false
                }
            },
            isShow2 () {
                if ((this.line > this.gsData[1]) && this.gsData[1] > this.cliff) {
                    return true
                }else {
                    return false
                }
            },
            isShow2_ () {
                if (this.cliff > this.gsData[1]) {
                    return true
                }else {
                    return false
                }
            },
            isShow3 () {
                if ((this.line > this.gsData[2]) && this.gsData[2] > this.cliff) {
                    return true
                }else {
                    return false
                }
            },
            isShow3_ () {
                if (this.cliff > this.gsData[2]) {
                    return true
                }else {
                    return false
                }
            }
        },
        watch: {
            line () {
                this.$set(this["TL"], 'TL', ['off', this.line])
                this.send(JSON.stringify(this["TL"]))
                // console.log(this.line)
                this.setLine(this.line)
            },
            cliff () {
                this.$set(this["CD"], 'CD', ['off', this.cliff])
                this.send(JSON.stringify(this["CD"]))
                this.setCliff(this.cliff)
            }
        },
        methods: {
            ...mapActions(["send"]),
            ...mapMutations(['setLine', "setCliff"]),
            initSend () {
                this.send(JSON.stringify(this['GS']));
            },
            // handleLineChange () {
            //     console.log(this.line)
            // },
            // handleCliffChange () {
            //     console.log(this.cliff)
            // }
        },
        mounted() {
            this.initSend();
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
        flex-direction: column;
    }

    .input-wrapper {
        display: flex;
        line-height: 1rem;
    }

    .line,
    .cliff {
        width: 50%;
        color: #ffffff;
    }

    .line-input,
    .cliff-input {
        width: 50%;
    }

    .img-wrapper {
        padding-bottom: 40%;
        height: 0;
        width: 100%;
        position: relative;
    }

    .list {
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        bottom: 0;
        background: #777777;
        opacity: 0.5;
        width: 80%;
        height: 90%;
        border-radius: 0.1rem;
        margin: 0 auto;
        margin-top: 0.2rem;
        display: flex;
    }

    .item {
        width: 33.3%;
        background: url('../../assets/img/line_of_inspection.png') no-repeat center;
        background-size: 60%;
        position: relative;
    }

    .item-img-line {
        width: 100%;
        height: 100%;
    }

    .item-img-cliff {
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        bottom: 0;
        margin: auto;
        width: 65%;
    }
    .number-list {
        position: absolute;
        bottom: 0;
        color: #ffffff;
        display: flex;
        right: 0;
        left: 0;
        margin: 0 auto;
        width: 80%;
    }
    .number {
        width: 33.3%;
        font-size: .14rem;
        box-sizing: border-box;
        padding-left: 0.2rem;
    }
</style>