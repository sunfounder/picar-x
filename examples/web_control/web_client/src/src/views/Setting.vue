<template>
    <div>
        <SettingHeader></SettingHeader>
        <div class="content">
            <SettingSidebar @changeSide="handleChangeSide"></SettingSidebar>
            <div class="controll-wrapper">
                <component :is="isComponent"></component>
            </div>
        </div>
    </div>
</template>

<script>
    import SettingHeader from '@/components/setting/Header'
    import SettingSidebar from '@/components/setting/Sidebar'
    import SettingFaceRecognition from '@/components/setting/FaceRecognition'
    import SettingUltrasound from '@/components/setting/Ultrasound'
    import SettingHorn from '@/components/setting/Horn'
    import SettingGimbal from '@/components/setting/Gimbal'
    import SettingWheel from '@/components/setting/Wheel'
    import SettingServo from '@/components/setting/Servo'
    import SettingGrayscale from '@/components/setting/Grayscale'
    export default {
        name: 'Setting',
        components: {
            SettingHeader,
            SettingSidebar,
            SettingFaceRecognition,
            SettingUltrasound,
            SettingHorn,
            SettingGimbal,
            SettingWheel,
            SettingServo,
            SettingGrayscale
        },
        data () {
            return {
                isComponent: 'SettingFaceRecognition'
            }
        },
        methods: {
            handleChangeSide (isComponent) {
                this.isComponent = isComponent
            }
        }
    }
</script>

<style scoped>
    .content {
        position: fixed;
        top: 1rem;
        right: 0;
        left: 0;
        bottom: 0;
        overflow: hidden;
        display: flex;
    }
    .controll-wrapper {
        flex: 1;
        background: #112944;
        padding: .2rem;
    }
</style>