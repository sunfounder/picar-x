<template>
    <div>
        <div class="ultrasound-wrapper">
            <div class="ultrasound-content">
                <img class="ultrasound-img" src="../../assets/img/Ultrasound_dis.png" alt="">
            </div>
            <div class="ultrasound-dis-desc">
                Distance:
                <span class="ultrasound-dis-number">{{distanceNumber}}</span>
                mm
            </div>
        </div>
    </div>
</template>

<script>
    import { mapState, mapGetters } from 'vuex'
    export default {
        name: 'ControllUltrasound',
        data () {
            return {
                data: '',
                ...mapState(['msg', 'socket'])
            }
        },
        computed: {
            ...mapGetters(['msgObj']),
            distanceNumber () {
                if (this.msgObj) {
                    return this.msgObj['US']
                }
            }
        },
        methods: {
            setDistance () {
                
            }
        },
        mounted () {
            // console.log(this.socket);
        }
    }
</script>

<style scoped>
    .ultrasound-wrapper {
        width: 30%;
        float: left;
        margin-top: 0.42rem;
    }

    .ultrasound-content {
        height: 0;
        overflow: hidden;
        padding-bottom: 67%;
        text-align: center;
    }

    .ultrasound-img {
        width: 80%;
    }

    .ultrasound-dis-desc {
        padding: .1rem;
        text-align: center;
        color: #ffffff;
        font-size: 0.26rem;
        background: #10243b;
        border-radius: 0.08rem;
        margin-top: 0.2rem;
    }
    .ultrasound-dis-number {
        display: inline-block;
        line-height: 0.44rem;
        background: #1f8efa;
        color: #000;
        padding: 0.05rem;
    }
</style>