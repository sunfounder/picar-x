<template>
    <div @click="handleClick" class="wrapper">
        <img class="video-img" :src="videoAdress" alt="">
    </div>
</template>

<script>
    import {
        mapGetters,
        mapState
    } from 'vuex'
    export default {
        name: 'Fullscreen',
        data() {
            return {
                hidden: false
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
            handleClick () {
                this.$emit('hidden', this.hidden)
            }
        }
    }
</script>

<style scoped>
    .wrapper {
        position: fixed;
        top: 0;
        right: 0;
        left: 0;
        bottom: 0;
        background: #000;
        z-index: 999999;
    }
    .video-img {
        width: 100%;
    }
</style>