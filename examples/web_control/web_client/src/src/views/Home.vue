<template>
    <div>
        <div class="home">
            <home-connection></home-connection>
        </div>
    </div>
</template>

<script>
    import HomeConnection from '@/components/home/Connection.vue'
    export default {
        name: 'Home',
        components: {
            HomeConnection
        }
    }
</script>

<style scoped>
    .home {
        width: 100%;
        padding-bottom: 56.22%;
        height: 0;
        overflow: hidden;
        background: url('../assets/img/home_bg.jpg') no-repeat;
        background-size: cover;
        background-attachment: fixed;
        max-height: 375;
    }

    @media screen and (min-width: 810px) and (max-width: 1024px) {
        .home {
            padding-bottom: 46.18%;
        }
    }
    @media screen and (min-width: 1024px){
        .home {
            padding-bottom: 75%;
        }
    }
</style>