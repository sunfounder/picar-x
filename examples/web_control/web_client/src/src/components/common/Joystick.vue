<template>
    <div>
        <div id="joystick" ref="joystick">

        </div>
    </div>
</template>

<script>
    import Nipples from 'nipplejs'
    import { mapState, mapActions, mapMutations } from 'vuex'
    export default {
        name: "ControllJoystick",
        props: {
            mode: String,
            wheelData: Object,
            wheelChoose: Number
        },
        data () {
            return {
                'JA': {"JA": [0, 0]},
                'JB': {"JB": [0, 0]},
                "MS": this.wheelData
            }
        },
        methods: {
            ...mapActions(['send']),
            handleJoystick(cate) {
                var this_ = this
                this.manger.on('move', function (evt, nipple) {
                    // console.log(evt,nipple,cate);
                    let x = Math.floor(parseFloat(nipple.vector.x) * 100)
                    let y = Math.floor(parseFloat(nipple.vector.y) * 100)
                    // console.log(x, y)
                    this_.$set(this_[cate], cate, [x, y])
                    console.log(this_[cate])
                    if (cate == 'JA') {
                        this_.send(JSON.stringify(this_[cate]))
                    }else if(cate == 'JB') {
                        this_.send(JSON.stringify(this_[cate]))
                    }else {
                        this_.$set(this_[cate], cate, ['on',this_.wheelChoose, y])
                        this_.send(JSON.stringify(this_[cate]))
                    }
                })
                this.manger.on('end', function(evt, nipple) {
                    
                    if (cate == 'JA') {
                        this_.$set(this_[cate], cate, [0, 0])
                        this_.send(JSON.stringify(this_[cate]))
                    }else if(cate == 'JB') {
                        this_.$set(this_[cate], cate, [0, 0])
                        this_.send(JSON.stringify(this_[cate]))
                    }else {
                        this_.$set(this_[cate], cate, ['on',0, 0])
                        this_.send(JSON.stringify(this_[cate]))
                    }
                })
            }
        },
        mounted() {
            this.JoystickOption = {
                zone: this.$refs.joystick,
                color: "red",
                mode: "static",
                position: {
                    left: '50%',
                    top: '50%'
                },
                size: 150,
            }
            this.manger = Nipples.create(this.JoystickOption)
            this.handleJoystick(this.mode)
        }
    }
</script>

<style>
    .back {
        background: #fff !important;
        opacity: 1!important;
    }
    .front {
        background: #0f77d0 !important;
    }
</style>