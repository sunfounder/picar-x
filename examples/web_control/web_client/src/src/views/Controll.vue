<template>
    <div>
        <div class="controll-wrapper">
            <controll-header></controll-header>
            <div class="content">
                <ControllUltrasound></ControllUltrasound>
                <ControllVideo></ControllVideo>
                <ControllLineinspection></ControllLineinspection>
                <div class="joystick-right">
                    <ControllJoystick :mode="JA"></ControllJoystick>
                </div>
                <div class="music-content">
                    <controllMusic></controllMusic>
                </div>
                <div class="joystick-left">
                    <ControllJoystick :mode="JB"></ControllJoystick>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
    import {
        mapState,
        mapMutations,
        mapActions,
        mapGetters
    } from 'vuex'
    import ControllHeader from '@/components/controll/Header'
    import ControllUltrasound from '@/components/controll/Ultrasound'
    import ControllVideo from '@/components/controll/Video'
    import ControllLineinspection from '@/components/controll/Lineinspection'
    import ControllJoystick from '@/components/common/Joystick'
    import controllMusic from '@/components/controll/Music'
    export default {
        name: "Controll",
        components: {
            ControllHeader,
            ControllUltrasound,
            ControllVideo,
            ControllLineinspection,
            ControllJoystick,
            controllMusic
        },
        data() {
            return {
                "JB": "JB",
                "JA": "JA",
            }
        },
        computed: {
            ...mapGetters(['isClose_'])
        },
        methods: {

        }
    }
</script>

<style scoped>
    .controll-wrapper {
        width: 100%;
        padding-bottom: 56.22%;
        height: 0;
        overflow: hidden;
        background: url('../assets/img/common_bg.jpg') no-repeat;
        background-size: cover;
        background-attachment: fixed;
    }

    @media screen and (min-width: 810px) and (max-width: 1024px) {
        .controll-wrapper {
            padding-bottom: 46.18%;
        }
    }

    @media screen and (min-width: 1024px) {
        .controll-wrapper {
            padding-bottom: 75%;
        }
    }

    .content {
        overflow: hidden;
        width: 100%;
        box-sizing: border-box;
    }

    .joystick-right {
        position: absolute;
        bottom: 0;
        left: 0.6rem;
        height: 3rem;
        width: 3rem;
    }

    .joystick-left {
        position: absolute;
        bottom: 0;
        right: 0.6rem;
        height: 3rem;
        width: 3rem;
    }

    .music-content {
        position: absolute;
        width: 6rem;
        height: 1.7rem;
        background: #10243b;
        bottom: .3rem;
        left: 4.55rem;
    }

    @media screen and (min-width: 650px) and (max-width: 735px) {
        .music-content {
            left: 4rem;
        }
    }
    @media screen and (min-width: 737px) {
        .music-content {
            left: 5.1rem;
        }
    }
</style>