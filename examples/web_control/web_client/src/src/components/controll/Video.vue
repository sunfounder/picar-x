<template>
    <div>
        <div class="video-wrapper">
            <div class="video-content">
                <img class="video-content-img" :src="videoAdress" alt="">
            </div>
            <div @click="handleFullClick" class="fullScreen-btn">
                <img class="fullScreen-btn-img" src="../../assets/img/fullscreen.png" alt="">
            </div>
        </div>
        <Fullscreen @hidden="handleHidden" v-if="isShow"></Fullscreen>
    </div>
</template>

<script>
    import {
        mapGetters,
        mapState
    } from 'vuex'
    import Fullscreen from '@/components/common/Fullscreen'
    export default {
        name: 'ControllVideo',
        components: {
            Fullscreen
        },
        data() {
            return {
                isShow: false
            }
        },
        computed: {
            ...mapGetters(['msgObj']),
            videoAdress() {
                if (this.msgObj) {
                    return this.msgObj['AD']
                }
            }
        },
        methods: {
            handleFullClick() {
                console.log('handleFullClick')
                this.isShow = true;
            },
            handleHidden (hidden) {
                this.isShow = hidden;
            }
        },

    }
</script>

<style scoped>
    .video-wrapper {
        width: 40%;
        height: 4.36rem;
        float: left;
        padding: 0.08rem;
        background: #10243b;
        margin: 0.42rem 0.2rem 0 0.1rem;
        position: relative;
    }

    .video-content {
        width: 100%;
        height: 100%;
    }

    .fullScreen-btn {
        position: absolute;
        bottom: 0.2rem;
        right: 0.2rem;
    }

    .fullScreen-btn-img {
        width: .34rem;
        height: .34rem;
    }

    .video-content-img {
        width: 100%;
    }

    @media screen and (min-width: 650px) and (max-width: 750px) {
        .fullScreen-btn {
            bottom: .6rem;
        }
    }
</style>