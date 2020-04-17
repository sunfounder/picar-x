<template>
    <div>
        <div class="ls-content">
            <div class="ls-img-wrapper">
                <img class="ls-img" src="../../assets/img/lineinspection.png" alt="">
            </div>
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
        name: 'ControllLineinspection',
        data() {
            return {
                gsValue0: 0,
                gsValue1: 0,
                gsValue2: 0
            }
        },
        computed: {
            ...mapGetters(['msgObj', 'line_', 'cliff_']),
            gsData() {
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
            isShow1() {
                if ((this.line_ > this.gsData[0]) && this.gsData[0] > this.cliff_) {
                    return true
                } else {
                    return false
                }
            },
            isShow1_() {
                if (this.cliff_ > this.gsData[0]) {
                    return true
                } else {
                    return false
                }
            },
            isShow2() {
                if ((this.line_ > this.gsData[1]) && this.gsData[1] > this.cliff_) {
                    return true
                } else {
                    return false
                }
            },
            isShow2_() {
                if (this.cliff_ > this.gsData[1]) {
                    return true
                } else {
                    return false
                }
            },
            isShow3() {
                if ((this.line_ > this.gsData[2]) && this.gsData[2] > this.cliff_) {
                    return true
                } else {
                    return false
                }
            },
            isShow3_() {
                if (this.cliff_ > this.gsData[2]) {
                    return true
                } else {
                    return false
                }
            }
        },
    }
</script>

<style scoped>
    .ls-content {
        width: 25%;
        height: 4rem;
        float: left;
        margin-top: 0.3rem;
        position: relative;
    }

    .ls-img-wrapper {
        height: 0;
        padding-bottom: 109.1%;
    }

    .ls-img {
        width: 100%;
    }

    .list {
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        bottom: -.1rem;
        background: #777777;
        opacity: 0.5;
        width: 100%;
        height: 100%;
        border-radius: 0.1rem;
        margin: 0 auto;
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
</style>