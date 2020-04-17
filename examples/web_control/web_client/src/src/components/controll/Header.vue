<template>
    <div>
        <div class="header-wrapper">
            <div @click="handleBackClick" class="header-back">
                <img  class="header-back-img" src="../../assets/img/header-back.png" alt="">
            </div>
            <div class="header-logo">
                {{type}}
            </div>
            <ul class="list">
                <li class="item" ref="controllSwitch" v-for="(item, index) of list" :key='item.id'
                    @click="handleClick(item.name, index)">
                    <div class="item-img">
                        <img class="item-img-content" :src="item.imgUrl" alt="">
                    </div>
                    <p class="item-desc">{{item.desc}}</p>
                </li>
            </ul>
        </div>
    </div>
</template>

<script>
    import {
        mapState,
        mapActions,
        mapMutations,
        mapGetters
    } from 'vuex'
    export default {
        name: 'ControllHeader',
        data() {
            return {
                list: [{
                    id: '0001',
                    imgUrl: require('../../assets/img/header-setting.png'),
                    desc: 'Setting',
                    name: 'setting'
                }, {
                    id: '0002',
                    imgUrl: require('../../assets/img/Facerecognition.png'),
                    desc: 'Face',
                    name: 'HT'
                }, {
                    id: '0003',
                    imgUrl: require('../../assets/img/Facetracking.png'),
                    desc: 'Tracking',
                    name: 'HF'
                }, {
                    id: '0004',
                    imgUrl: require('../../assets/img/Colorrecognition.png'),
                    desc: 'Color',
                    name: 'CT'
                }, {
                    id: '0005',
                    imgUrl: require('../../assets/img/Colortracking.png'),
                    desc: 'Color Tracking',
                    name: 'CF'
                }, {
                    id: '0006',
                    imgUrl: require('../../assets/img/Avoidance.png'),
                    desc: 'Obstacle Avoidance',
                    name: 'OA'
                }, {
                    id: '0007',
                    imgUrl: require('../../assets/img/Ultrasound.png'),
                    desc: 'Ultrasonic',
                    name: 'US',
                }, {
                    id: '0008',
                    imgUrl: require('../../assets/img/Grayscale.png'),
                    desc: 'Grayscale',
                    name: 'GS'
                }, {
                    id: '0009',
                    imgUrl: require('../../assets/img/inspection_icon.png'),
                    desc: 'Line Tracking',
                    name: 'TL'
                }, {
                    id: '0010',
                    imgUrl: require('../../assets/img/cliff.png'),
                    desc: 'Cliff Detection',
                    name: 'CD'
                }, ],
                sendDatasOff: {
                    'JA': {
                        'JA': [0, 0]
                    },
                    'JB': {
                        'JB': [0, 0]
                    },
                    'SS': {
                        'SS': ['off', 0, 0.5]
                    },
                    'SM': {
                        'SM': ['off', 0, 0.5]
                    },
                    'SL': {
                        'SL': ['off', 0, 0.5]
                    },
                    'TT': {
                        'TT': ['off', 'you']
                    },
                    'US': {
                        'US': 'off'
                    },
                    'GS': {
                        'GS': "off"
                    },
                    'OA': {
                        'OA': 'off'
                    },
                    'TL': {
                        "TL": ['off', 400]
                    },
                    'CD': {
                        'CD': ['off', 110]
                    },
                    'CA': {
                        'CA': 'off'
                    },
                    'HT': {
                        'HT': 'off'
                    },
                    'HF': {
                        'HF': 'off'
                    },
                    'CT': {
                        'CT': 'off'
                    },
                    'CF': {
                        'CF': 'off'
                    },
                    'MS': {
                        'MS': ['off', 0, 0]
                    },
                    'DO': {
                        'DO': 0
                    },
                    'PO': {
                        'PO': 0
                    },
                    'TO': {
                        'TO': 0
                    },
                    'CC': {
                        'CC': 'blue'
                    },
                },
                sendDatasOn: {
                    'JA': {
                        'JA': [0, 0]
                    },
                    'JB': {
                        'JB': [0, 0]
                    },
                    'SS': {
                        'SS': ['on', 0, 0.5]
                    },
                    'SM': {
                        'SM': ['on', 0, 0.5]
                    },
                    'SL': {
                        'SL': ['on', 0, 0.5]
                    },
                    'TT': {
                        'TT': ['on', 'you']
                    },
                    'US': {
                        'US': 'on'
                    },
                    'GS': {
                        'GS': "on"
                    },
                    'OA': {
                        'OA': 'on'
                    },
                    'TL': {
                        "TL": ['on', 400]
                    },
                    'CD': {
                        'CD': ['on', 110]
                    },
                    'CA': {
                        'CA': 'on'
                    },
                    'HT': {
                        'HT': 'on'
                    },
                    'HF': {
                        'HF': 'on'
                    },
                    'CT': {
                        'CT': 'on'
                    },
                    'CF': {
                        'CF': 'on'
                    },
                    'MS': {
                        'MS': ['on', 0, 0]
                    },
                    'DO': {
                        'DO': 0
                    },
                    'PO': {
                        'PO': 0
                    },
                    'TO': {
                        'TO': 0
                    },
                    'CC': {
                        'CC': 'blue'
                    },
                },
                switchFlag: {
                    'USflag': false,
                    'GSflag': false,
                    'OAflag': false,
                    'TLflag': false,
                    'CDflag': false,
                    'HTflag': false,
                    'HFflag': false,
                    'CTflag': false,
                    'CFflag': false
                }
            }
        },
        computed: {
            ...mapGetters(['msgObj','color_', 'line_', 'cliff_']),
            type () {
                if (this.msgObj) {
                    return this.msgObj['TP'] || 'PiCar-X'
                }else {
                    return 'PiCar-X'
                }
            }
        },
        methods: {
            ...mapActions(['send', 'getMessage','closeSocket']),
            handleClick(name, index) {
                if (name == 'setting') {
                    this.$router.push('/setting')
                    return;
                }

                const element = this.$refs.controllSwitch[index]
                console.log(element)
                let dataOn = JSON.stringify(this.sendDatasOn[name])
                let dataOff = JSON.stringify(this.sendDatasOff[name])
                let flag = this.switchFlag[`${name}flag`]
                if (name == 'TL') {
                    if (!this.switchFlag[`${name}flag`]) {
                        this.$set(this.switchFlag, `${name}flag`, true)
                        this.$set(this.sendDatasOn[name], name, ['on', this.line_])
                        this.send(JSON.stringify(this.sendDatasOn[name]))
                        element.style.color = 'red'
                    } else {
                        this.send(dataOff)
                        console.log(dataOff)
                        this.$set(this.switchFlag, `${name}flag`, false)
                        element.style.color = '#fff'
                    }
                    return 
                }
                if (name == 'CD') {
                    if (!this.switchFlag[`${name}flag`]) {
                        this.$set(this.switchFlag, `${name}flag`, true)
                        this.$set(this.sendDatasOn[name], name, ['on', this.cliff_])
                        this.send(JSON.stringify(this.sendDatasOn[name]))
                        element.style.color = 'red'
                    } else {
                        this.send(dataOff)
                        console.log(dataOff)
                        this.$set(this.switchFlag, `${name}flag`, false)
                        element.style.color = '#fff'
                    }
                    return 
                }
                if (!this.switchFlag[`${name}flag`]) {
                    this.send(dataOn)
                    console.log(dataOn)
                    this.$set(this.switchFlag, `${name}flag`, true)
                    element.style.color = 'red'
                } else {
                    this.send(dataOff)
                    console.log(dataOff)
                    this.$set(this.switchFlag, `${name}flag`, false)
                    element.style.color = '#fff'
                }
            },
            handleBackClick () {
                this.reset();
                this.$router.push('/');
            },
            reset () {
                this.sendDatasOff =  {
                    'JA': {
                        'JA': [0, 0]
                    },
                    'JB': {
                        'JB': [0, 0]
                    },
                    'SS': {
                        'SS': ['off', 0, 0.5]
                    },
                    'SM': {
                        'SM': ['off', 0, 0.5]
                    },
                    'SL': {
                        'SL': ['off', 0, 0.5]
                    },
                    'TT': {
                        'TT': ['off', 'you']
                    },
                    'US': {
                        'US': 'off'
                    },
                    'GS': {
                        'GS': "off"
                    },
                    'OA': {
                        'OA': 'off'
                    },
                    'TL': {
                        "TL": ['off', 400]
                    },
                    'CD': {
                        'CD': ['off', 110]
                    },
                    'CA': {
                        'CA': 'off'
                    },
                    'HT': {
                        'HT': 'off'
                    },
                    'HF': {
                        'HF': 'off'
                    },
                    'CT': {
                        'CT': 'off'
                    },
                    'CF': {
                        'CF': 'off'
                    },
                    'MS': {
                        'MS': ['off', 0, 0]
                    },
                    'DO': {
                        'DO': 0
                    },
                    'PO': {
                        'PO': 0
                    },
                    'TO': {
                        'TO': 0
                    },
                    'CC': {
                        'CC': 'blue'
                    },
                },
                this.sendDatasOn =  {
                    'JA': {
                        'JA': [0, 0]
                    },
                    'JB': {
                        'JB': [0, 0]
                    },
                    'SS': {
                        'SS': ['on', 0, 0.5]
                    },
                    'SM': {
                        'SM': ['on', 0, 0.5]
                    },
                    'SL': {
                        'SL': ['on', 0, 0.5]
                    },
                    'TT': {
                        'TT': ['on', 'you']
                    },
                    'US': {
                        'US': 'on'
                    },
                    'GS': {
                        'GS': "on"
                    },
                    'OA': {
                        'OA': 'on'
                    },
                    'TL': {
                        "TL": ['on', 400]
                    },
                    'CD': {
                        'CD': ['on', 110]
                    },
                    'CA': {
                        'CA': 'on'
                    },
                    'HT': {
                        'HT': 'on'
                    },
                    'HF': {
                        'HF': 'on'
                    },
                    'CT': {
                        'CT': 'on'
                    },
                    'CF': {
                        'CF': 'on'
                    },
                    'MS': {
                        'MS': ['on', 0, 0]
                    },
                    'DO': {
                        'DO': 0
                    },
                    'PO': {
                        'PO': 0
                    },
                    'TO': {
                        'TO': 0
                    },
                    'CC': {
                        'CC': 'blue'
                    },
                },
                this.switchFlag =  {
                    'USflag': false,
                    'GSflag': false,
                    'OAflag': false,
                    'TLflag': false,
                    'CDflag': false,
                    'HTflag': false,
                    'HFflag': false,
                    'CTflag': false,
                    'CFflag': false
                }
                let obj = {
                    'JA':[0,0],
                    'JB':[0,0],  
                    'SS':['off',0,0.5], 
                    'SM':['off',0,0.5], 
                    'SL':['off',0,0.5], 
                    'TT':['off','you'],  
                    'US':'off',   
                    'GS':"off",  
                    'OA':'off',  
                    'TL':['off',950], 
                    'CD':['off',110],  
                    'HT':'off', 
                    'HF':'off',  
                    'CT':'off',  
                    'CF':'off',  
                    'MS':['off',0,0],  
                    'DO':['off',0],  
                    'PO':['off',0],  
                    'TO':['off',0] , 
                    'CC': this.color_, 
                }
                this.send(JSON.stringify(obj))
                this.$refs.controllSwitch.forEach((item, key) => {
                    this.$refs.controllSwitch[key].style.color = '#fff'
                })
                // this.closeSocket();
            }
        },
        mounted () {
            this.reset()
        }
    }
</script>

<style scoped>
    .header-wrapper {
        height: 1rem;
        display: flex;
    }

    .header-back {
        float: left;
        padding: 0 .25rem;
        line-height: 1rem;
    }

    .header-logo {
        flex: 1;
        line-height: 1rem;
        font-family: NoirPro-BoldItalic;
        color: #0c77cf;
        font-size: .64rem;
    }

    .header-back-img {
        width: 65%;
    }

    .list {
        min-width: 10rem;
    }

    .item {
        width: 10%;
        position: relative;
        overflow: hidden;
        padding-bottom: 10%;
        float: right;
        height: 0;
        color: #fff;
    }

    .item-img {
        position: absolute;
        top: 0;
        left: 0;
        bottom: .44rem;
        right: 0;
        box-sizing: border-box;
        padding: .05rem;
    }

    .item-img-content {
        height: 100%;
        display: block;
        margin: 0 auto;
    }

    .item-desc {
        position: absolute;
        right: 0;
        left: 0;
        bottom: 0;
        height: .4rem;
        line-height: .4rem;
        text-align: center;
        font-size: .12rem;
    }
</style>