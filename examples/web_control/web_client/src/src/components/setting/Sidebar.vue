<template>
    <div class="side">
        <ul class="list">
            <li class="item" v-for="item of list" :key="item.id" @click="handleSideClick(item.isComponent)">
                <img class="item-img" :src="item.imgUrl" alt="">
                <span>{{item.desc}}</span>
            </li>
        </ul>
    </div>
</template>

<script>
    export default {
        name: 'SettingSidebar',
        data () {
            return {
                list: [{
                    id: '0001',
                    imgUrl: require('../../assets/img/setting_facereco.png'),
                    desc: 'Face Detection',
                    isComponent: 'SettingFaceRecognition'
                },{
                    id: '0002',
                    imgUrl: require('../../assets/img/setting_Ultrasound.png'),
                    desc: 'Ultrasonic',
                    isComponent: "SettingUltrasound"
                },{
                    id: '0004',
                    imgUrl: require('../../assets/img/setting_gimbal.png'),
                    desc: 'Pan-and-Tilt',
                    isComponent: "SettingGimbal"
                },{
                    id: '0005',
                    imgUrl: require('../../assets/img/setting_wheel.png'),
                    desc: 'Wheel',
                    isComponent: "SettingWheel"
                },{
                    id: '0006',
                    imgUrl: require('../../assets/img/setting_servo.png'),
                    desc: 'Servo',
                    isComponent: "SettingServo"
                },
                {
                    id: '0007',
                    imgUrl: require('../../assets/img/line.png'),
                    desc: 'Grayscale',
                    isComponent: "SettingGrayscale"
                },]
            }
        },
        methods: {
            handleSideClick (isComponent) {
                console.log(isComponent)
                this.$emit('changeSide', isComponent)
            }
        }
    }
</script>

<style scoped>
    .side {
        width: 3.5rem;
        background: #0b131b;
        height: 100%;
    }

    .item {
        line-height: .8rem;
        height: .8rem;
        box-sizing: border-box;
        padding: 0 .2rem;
        color: #536986;
    }

    .item-img {
        margin: 0 .3rem;
        width: .4rem;
        height: .4rem;
    }
</style>